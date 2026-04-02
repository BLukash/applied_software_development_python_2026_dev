# Quickstart: Restructure Lectures 6, 7 & Add Lecture 8

**Feature**: 013-lecture-mcp-restructure
**Date**: 2026-04-02

## Prerequisites

- Git repository cloned and on branch `013-lecture-mcp-restructure`
- Python 3.13+ installed
- Jupyter Notebook / JupyterLab installed
- pipx installed (for keep-mcp verification in L8)

## Verification Steps

### 1. Verify Directory Renames

```bash
# These should exist:
ls lectures/06-web-fastapi/lecture-06.ipynb
ls lectures/07-async-testing/lecture-07.ipynb
ls lectures/08-mcp/lecture-08.ipynb

# These should NOT exist:
ls lectures/06-web-fastapi-mcp/    # Should fail
ls lectures/07-integrations-async-mcp/    # Should fail
```

### 2. Verify MCP Content Removal from L6

```bash
# Should return 0 matches (excluding forward-references to L8):
grep -c "keep-mcp\|Model Context Protocol" lectures/06-web-fastapi/lecture-06.ipynb
# Should return 0:
grep -c "host/client/server.*MCP\|tools/resources/prompts" lectures/06-web-fastapi/lecture-06.ipynb
```

### 3. Verify MCP Content Removal from L7

```bash
# Should return 0 matches for practical MCP content:
grep -c "pipx run keep-mcp\|Google Master Token\|UNSAFE_MODE\|safe mode.*unsafe mode" lectures/07-async-testing/lecture-07.ipynb
```

### 4. Verify L6 Has 3 Exercises

Open `lectures/06-web-fastapi/lecture-06.ipynb` in Jupyter and verify:
- Exercise 1: Book schema with Pydantic validation
- Exercise 2: GET /notes/{note_id} endpoint
- Exercise 3: DELETE /notes/{note_id} endpoint (NEW)

### 5. Verify L7 Testing Expansion

Open `lectures/07-async-testing/lecture-07.ipynb` in Jupyter and verify:
- pytest fixtures section exists
- @pytest.mark.parametrize section exists
- Error case testing (404, 422) section exists
- Testing exercise (write 3-4 tests) exists

### 6. Verify L8 Content Completeness

Open `lectures/08-mcp/lecture-08.ipynb` in Jupyter and verify:
- 8 main sections (Intro, Architecture, Lifecycle, Setup, Safety, Testing, Project, Summary)
- 2 exercises (primitive identification + keep-mcp hands-on)
- mcp-lifecycle.png loads correctly from assets/
- At least 3 diagrams visible
- At least 2 memes present
- "What's Next" previews L9 (Docker + PostgreSQL)

### 7. Verify Asset Migration

```bash
# Should exist in L8:
ls lectures/08-mcp/assets/mcp-lifecycle.png

# Should still exist in L7 (async content):
ls lectures/07-async-testing/assets/threads-vs-asyncio.png

# Should NOT exist in old location:
ls lectures/07-integrations-async-mcp/assets/mcp-lifecycle.png    # Should fail
```

### 8. Verify No clients/ Directory

```bash
# Should fail (directory removed):
ls lectures/06-web-fastapi/notes-api/app/clients/
```

### 9. Run All Notebooks

```bash
# Each notebook should execute without errors:
jupyter nbconvert --to notebook --execute lectures/06-web-fastapi/lecture-06.ipynb
jupyter nbconvert --to notebook --execute lectures/07-async-testing/lecture-07.ipynb
jupyter nbconvert --to notebook --execute lectures/08-mcp/lecture-08.ipynb
```

### 10. Verify Cross-References

Check these specific cells:
- L6 "What's Next": mentions async, httpx, testing (NOT MCP)
- L7 "What's Next": mentions MCP (L8), Docker + PostgreSQL (L9)
- L8 Prerequisites: mentions L6 (FastAPI, REST) and L7 (async, httpx, testing)
- L8 "What's Next": mentions L9 Docker + PostgreSQL

## Notes

- The notes-api project code is NOT modified by this feature
- L8 is a standalone notebook with no project code changes
- If L8 notebook cells reference keep-mcp operations, those cells are documentation-only (not executable without a configured Google account)
