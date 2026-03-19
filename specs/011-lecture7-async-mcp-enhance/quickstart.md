# Quickstart: Verification Checklist

## Pre-flight

- [ ] On branch `011-lecture7-async-mcp-enhance`
- [ ] Existing notebook `lectures/07-integrations-async-mcp/lecture-07.ipynb` is present and unbroken

## Async Enhancement Verification

- [ ] New subsection 1.4 exists with thread primer and GIL explanation
- [ ] Comparison table has at least 5 dimensions (scheduling, memory, GIL, best use, race conditions)
- [ ] Runnable code cell compares `threading` vs `asyncio.gather` — both produce ~1 second for 3 tasks
- [ ] Diagram `assets/threads-vs-asyncio.png` exists and is referenced in notebook
- [ ] Connection to FastAPI design (why `async def`) is explained
- [ ] Content is in Ukrainian with English terms in parentheses

## MCP Lifecycle Verification

- [ ] New subsection 4.4 explains subprocess lifecycle (not a traditional server)
- [ ] Lifecycle diagram `assets/mcp-lifecycle.png` exists and is referenced
- [ ] Annotated config JSON explains `command`, `args`, `env` fields
- [ ] Transport comparison table has at least 4 dimensions (stdio vs SSE/HTTP)
- [ ] Clarification that "server" ≠ traditional network server is present
- [ ] Content is in Ukrainian with English terms in parentheses

## Integration Verification

- [ ] All notebook cells execute sequentially in clean kernel without errors
- [ ] No duplicate content with existing cells
- [ ] Subsection numbering is consistent throughout Section 1 and Section 4
- [ ] Emoji usage: max 1–2 per new subsection
- [ ] Total estimated lecture duration: 85–100 minutes
