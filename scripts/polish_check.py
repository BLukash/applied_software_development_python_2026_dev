"""Check notebook for repetitions and polish issues."""
import json, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

with open("lectures/04-functions-modules-errors-oop/lecture-04.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

print("=== CONTENT POLISH CHECK ===\n")

# 1. Check for repeated code blocks across cells
print("1. Checking for duplicated code snippets...")
code_blocks = {}
for i, cell in enumerate(nb["cells"]):
    src = "".join(cell["source"])
    blocks = re.findall(r"```python\n(.*?)```", src, re.DOTALL)
    for block in blocks:
        clean = block.strip()
        if len(clean) > 30:
            key = clean[:60]
            if key in code_blocks:
                print(f"  Possible dup: cells {code_blocks[key]} and {i}: {key[:50]}...")
            else:
                code_blocks[key] = i

# 2. Check for empty or near-empty cells
print("\n2. Checking for empty/minimal cells...")
for i, cell in enumerate(nb["cells"]):
    src = "".join(cell["source"]).strip()
    if not src:
        print(f"  EMPTY: Cell {i} [{cell['cell_type']}]")
    elif len(src) < 10 and cell["cell_type"] == "markdown":
        print(f"  MINIMAL: Cell {i}: '{src}'")

# 3. Check markdown cells that are just "---" separators
print("\n3. Separator cells (---) that could be merged:")
separators = []
for i, cell in enumerate(nb["cells"]):
    src = "".join(cell["source"]).strip()
    if src == "---":
        separators.append(i)
# Check if adjacent cells could be merged (separator followed by markdown)
for sep_idx in separators:
    if sep_idx + 1 < len(nb["cells"]):
        next_cell = nb["cells"][sep_idx + 1]
        next_src = "".join(next_cell["source"]).strip()
        if next_src.startswith("---"):
            print(f"  Cell {sep_idx} and {sep_idx+1}: consecutive separators")

# 4. Check for text diagrams that repeat original cell content
print("\n4. Checking text diagrams for content overlap with code cells...")
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "markdown":
        continue
    src = "".join(cell["source"])
    # Check if a markdown cell has both a code block AND a text table about the same topic
    has_raise_code = "raise " in src and "```" in src
    has_raise_table = "raise" in src.lower() and "|" in src

# 5. Check attribution lines still pointing to correct sources
print("\n5. Checking for broken attribution patterns...")
for i, cell in enumerate(nb["cells"]):
    src = "".join(cell["source"])
    # Attribution should be italic text with link
    for m in re.finditer(r"\*Джерело: \[([^\]]+)\]\(([^)]+)\)\*", src):
        site = m.group(1)
        url = m.group(2)
        if not url.startswith("http"):
            print(f"  Cell {i}: Non-URL attribution: {url[:50]}")

# 6. Check for markdown formatting issues
print("\n6. Checking markdown formatting...")
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "markdown":
        continue
    src = "".join(cell["source"])
    # Check for unclosed code blocks
    if src.count("```") % 2 != 0:
        print(f"  Cell {i}: Unclosed code block")
    # Check for unclosed details
    if "<details>" in src and "</details>" not in src:
        print(f"  Cell {i}: Unclosed <details> tag")
    # Check for unclosed bold/italic
    bold_count = len(re.findall(r"\*\*", src))
    if bold_count % 2 != 0:
        print(f"  Cell {i}: Odd number of ** (unclosed bold)")

# 7. Check code cells for syntax issues
print("\n7. Checking code cells for obvious issues...")
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "code":
        continue
    src = "".join(cell["source"])
    # Check for OOP remnants
    if "class " in src and "ValidationError" not in src and "MyError" not in src:
        if "first_class" not in src and "first-class" not in src:
            print(f"  Cell {i}: Contains 'class' keyword")
    # Check for import of non-stdlib
    imports = re.findall(r"^import (\w+)|^from (\w+)", src, re.MULTILINE)
    stdlib = {"os", "sys", "json", "csv", "re", "math", "random", "datetime",
              "collections", "functools", "itertools", "logging", "pathlib",
              "statistics", "string", "textwrap", "time", "typing", "abc",
              "io", "copy", "operator", "inspect", "unittest", "doctest",
              "importlib", "shutil", "subprocess"}
    for imp in imports:
        mod = imp[0] or imp[1]
        if mod and mod not in stdlib:
            print(f"  Cell {i}: Non-stdlib import: {mod}")

print("\n=== DONE ===")
