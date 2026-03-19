# Research: Enhance Lecture 7 — Deeper Asyncio & MCP Lifecycle

## R1: Threading vs Asyncio — Best Practices for Teaching

**Decision**: Use a "3 simulated network calls" demo where both `threading` and `asyncio` produce ~1 second wall time (vs 3 seconds sequential), then explain *why* asyncio is preferred for I/O despite both being fast.

**Rationale**:
- Students need to see that threads *also* solve the concurrency problem for I/O — the question is *why choose async instead*
- The GIL makes threads useless for CPU-bound parallelism, but for I/O-bound work threads DO work (GIL is released during I/O)
- The real advantages of async for web servers: lower memory per connection (~KB vs ~MB per thread), no race conditions on shared state (single-threaded), deterministic scheduling (cooperative vs preemptive)
- Keep it honest: don't claim "threads are bad" — say "async is a better fit for web servers handling many concurrent I/O operations"

**Alternatives considered**:
- Using `concurrent.futures.ThreadPoolExecutor` instead of raw `threading` — rejected: adds abstraction layer, hides what threads are
- Including `multiprocessing` comparison — rejected: out of scope per spec, too much content
- Using real HTTP calls for the demo — rejected: network variability makes timing unreliable in classroom

### Comparison Table Dimensions (5+)

| Dimension | Threading | Asyncio |
|-----------|-----------|---------|
| Scheduling model | Preemptive (OS decides when to switch) | Cooperative (you decide with `await`) |
| Memory per task | ~1–8 MB per thread (stack) | ~KB per coroutine (heap object) |
| GIL impact | GIL released during I/O, held during CPU | No GIL concern (single thread) |
| Best for | I/O-bound (with caveats), CPU-bound (with multiprocessing) | I/O-bound: network, disk, DB |
| Race conditions | Yes — shared mutable state needs locks | Minimal — single thread, explicit yield points |
| Error handling | Exceptions in threads are silently lost unless joined | Normal try/except, `asyncio.gather(return_exceptions=True)` |
| Scalability | Hundreds of threads (OS limit) | Tens of thousands of coroutines |
| FastAPI connection | `def` endpoints run in thread pool | `async def` endpoints run in event loop |

### GIL Explanation (for students)

Core message: "GIL (Global Interpreter Lock) — це замок, який дозволяє лише ОДНОМУ потоку виконувати Python-код одночасно. Для I/O це не проблема (потоки чекають мережу, не CPU), але async дає ті самі переваги без накладних витрат потоків."

Key visual: Thread execution shows OS switching between threads unpredictably; async shows event loop switching at explicit `await` points — predictable, debuggable.

## R2: MCP Transport & Lifecycle Details

**Decision**: Focus on stdio transport as the primary/default mode. Explain that the host (LLM client) spawns the MCP server as a **child process**, communicates via stdin/stdout using JSON-RPC 2.0, and manages the server's full lifecycle.

**Rationale**:
- The official MCP spec defines two transport mechanisms: stdio and HTTP+SSE
- stdio is the default for local tools (Claude Desktop, Cursor, Claude Code)
- Students see `"command": "pipx", "args": ["run", "keep-mcp"]` in the config — this IS the subprocess command
- The key insight: "MCP server" is misleading if you think of a web server — it's more like a plugin that the host runs on demand

**Alternatives considered**:
- Deep dive into JSON-RPC 2.0 protocol format — rejected: too low-level for this lecture
- Covering HTTP+SSE transport in equal depth — rejected: students only use local tools, SSE is a brief mention
- Building a custom MCP server — rejected: out of scope for this enhancement

### MCP Lifecycle Steps

1. **Host starts** (e.g., Claude Desktop launches)
2. **Host reads config** (`claude_desktop_config.json`) — finds `"keep-mcp"` entry
3. **Host spawns subprocess**: `pipx run keep-mcp` with env vars (`GOOGLE_MASTER_TOKEN`, `GOOGLE_EMAIL`)
4. **Initialization**: Host sends `initialize` request via stdin → server responds with capabilities via stdout
5. **Operation**: Host sends JSON-RPC requests (tool calls) via stdin → server responds via stdout
6. **Shutdown**: Host sends `shutdown` notification → server exits cleanly
7. **Process terminates**: When host closes or user disconnects, subprocess is killed

### Transport Comparison Table

| Dimension | stdio (Local) | HTTP+SSE (Remote) |
|-----------|---------------|-------------------|
| How server starts | Host spawns as subprocess | Server runs independently (separate process/machine) |
| Communication | stdin/stdout (JSON-RPC) | HTTP POST (client→server) + Server-Sent Events (server→client) |
| Network required | No (same machine) | Yes (can be different machines) |
| Config format | `"command"` + `"args"` | `"url"` (e.g., `"http://mcp.example.com:3000"`) |
| Typical use case | Desktop tools (Claude Desktop, Cursor) | Shared team servers, cloud deployments |
| Lifecycle management | Host manages (start/stop) | Server managed independently (systemd, Docker, etc.) |

### Annotated Config JSON

```json
{
  "mcpServers": {
    "keep-mcp": {                    // Ім'я сервера (довільне)
      "command": "pipx",             // Команда для запуску (що запустити)
      "args": ["run", "keep-mcp"],   // Аргументи команди (як запустити)
      "env": {                       // Змінні середовища для subprocess
        "GOOGLE_MASTER_TOKEN": "...",
        "GOOGLE_EMAIL": "..."
      }
    }
  }
}
```

Key teaching point: This is NOT a URL. It's a **shell command** that the host executes. The host becomes the "parent process" and the MCP server becomes the "child process."

## R3: Diagram Specifications

### threads-vs-asyncio.png

Layout: Two timeline diagrams side by side.

**Left (Threads)**:
- 3 horizontal lanes (Thread 1, Thread 2, Thread 3)
- Each shows: [start] → [I/O wait (gray)] → [done]
- All three run simultaneously
- OS scheduler arrows showing preemptive switching
- Total time: ~1 second
- Label: "3 потоки × 1 MB кожен = 3 MB RAM"

**Right (Asyncio)**:
- 1 horizontal lane (Event Loop)
- Shows: [Task 1 start → await] [Task 2 start → await] [Task 3 start → await] [Task 1 done] [Task 2 done] [Task 3 done]
- Cooperative switching at `await` points (marked with arrows)
- Total time: ~1 second
- Label: "3 корутини × ~KB кожна = ~KB RAM"

### mcp-lifecycle.png

Layout: Vertical sequence diagram.

**Participants**: Host (Claude Desktop) | MCP Server (keep-mcp subprocess)

Steps:
1. Host → [spawn subprocess: `pipx run keep-mcp`]
2. Host ←→ Server: `initialize` (capabilities exchange)
3. Host → Server: `tools/call` (e.g., `find` notes)
4. Server → Host: result (JSON)
5. Host → Server: `shutdown`
6. Server exits (process terminates)

Show stdin/stdout arrows between host and server.
