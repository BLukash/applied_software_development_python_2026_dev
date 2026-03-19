# Data Model: Notebook Cell Insertion Map

No traditional data entities — this feature adds cells to an existing Jupyter notebook.

## Cell Insertion Points

### Async Enhancement (Section 1)

**Insert after**: `cell-8` (sync→async conversion example, before async meme `cell-9`)

| Cell ID | Type | Subsection | Content Summary |
|---------|------|------------|-----------------|
| async-threads-intro | markdown | 1.4 | Thread primer + GIL explanation + comparison table |
| async-threads-code | code | 1.4 | Side-by-side threading vs asyncio demo |
| async-threads-visual | markdown | 1.4 | Diagram + FastAPI design connection |

### MCP Lifecycle Enhancement (Section 4)

**Insert after**: `cell-24` (LLM client configs, before verification `cell-25`)

| Cell ID | Type | Subsection | Content Summary |
|---------|------|------------|-----------------|
| mcp-lifecycle-intro | markdown | 4.4 | "How does the MCP client run the server?" intro |
| mcp-lifecycle-diagram | markdown | 4.4 | Lifecycle diagram + step-by-step explanation |
| mcp-lifecycle-config | markdown | 4.5 | Annotated config JSON |
| mcp-transport-table | markdown | 4.5 | stdio vs SSE/HTTP comparison table |

### Subsection Renumbering

After insertion, the MCP section subsections become:
- 4.1 Встановлення keep-mcp (existing)
- 4.2 Автентифікація (existing)
- 4.3 Конфігурація LLM-клієнта (existing)
- **4.4 Як MCP-клієнт запускає сервер? (NEW)**
- **4.5 Транспорт: stdio vs SSE (NEW)**
- 4.6 Перевірка з'єднання (was 4.4)
- 4.7 Усунення проблем (was 4.5)

## New Assets

| File | Type | Size Target | Description |
|------|------|-------------|-------------|
| `assets/threads-vs-asyncio.png` | Diagram | ~800×400px | Side-by-side timeline: threads vs event loop |
| `assets/mcp-lifecycle.png` | Diagram | ~600×500px | Sequence diagram: host spawns and communicates with MCP server |
