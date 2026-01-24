# Research: Лекція 1 — Вступ до Python

**Date**: 2026-01-24
**Status**: Complete

## 1. Python History & Overview Content

### Decision
Include brief history focusing on practical relevance: Guido van Rossum (1991), "batteries included" philosophy, Python 2 vs 3 transition (completed), current dominance in data science/ML/web.

### Rationale
Students benefit from understanding Python's design philosophy ("readability counts") as it explains many language decisions they'll encounter.

### Key Points to Include
- Created by Guido van Rossum, first released 1991
- Named after Monty Python (not the snake) - good meme opportunity
- "Batteries included" = rich standard library
- Python 2 end-of-life was January 2020 - only use Python 3
- TIOBE Index rankings, Stack Overflow survey popularity

### References
- [Python.org History](https://docs.python.org/3/faq/general.html#why-is-it-called-python)
- [Python Enhancement Proposals (PEPs)](https://peps.python.org/)
- [The Zen of Python (PEP 20)](https://peps.python.org/pep-0020/)

---

## 2. Installation Instructions Research

### Decision
Provide platform-specific instructions for Windows, macOS, and Linux with emphasis on Windows (most common among students).

### Windows Installation
- Download from python.org/downloads
- **CRITICAL**: Check "Add Python to PATH" during installation
- Verify: `python --version` or `py --version`
- Common issue: Microsoft Store Python vs python.org version

### macOS Installation
- Use Homebrew: `brew install python@3.12`
- Or download from python.org
- Verify: `python3 --version`
- Note: macOS comes with Python 2 (deprecated) - don't use it

### Linux Installation
- Most distros: `sudo apt install python3` (Debian/Ubuntu)
- Or: `sudo dnf install python3` (Fedora)
- Verify: `python3 --version`

### References
- [Python Downloads](https://www.python.org/downloads/)
- [Python Setup and Usage](https://docs.python.org/3/using/index.html)

---

## 3. IDE Recommendations Research

### Decision
Recommend VS Code as primary (free, cross-platform, excellent Python support) with PyCharm as alternative for students who prefer full IDE experience.

### VS Code Setup
**Extensions to recommend**:
1. Python (Microsoft) - essential
2. Pylance - type checking, IntelliSense
3. Python Debugger - debugging support
4. Jupyter - notebook support
5. (Optional) Black Formatter, Ruff

### PyCharm Setup
- Community Edition is free and sufficient
- Professional has more features but not needed for this course
- Built-in virtual environment management

### References
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [PyCharm Documentation](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)

---

## 4. Virtual Environment Best Practices

### Decision
Teach `venv` (built-in) as primary method. Mention `uv` as modern alternative per constitution.

### venv Commands (cross-platform)
```bash
# Create
python -m venv .venv

# Activate (Windows cmd)
.venv\Scripts\activate.bat

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate (macOS/Linux)
source .venv/bin/activate

# Deactivate (all platforms)
deactivate
```

### Common Issues
- PowerShell execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Wrong Python version in venv: specify with `python3.12 -m venv .venv`

### References
- [venv Documentation](https://docs.python.org/3/library/venv.html)
- [uv - Fast Python Package Installer](https://github.com/astral-sh/uv)

---

## 5. pip Basics Research

### Decision
Cover essential commands: install, list, freeze, requirements.txt workflow.

### Essential Commands
```bash
pip install package_name        # Install package
pip install package==1.2.3      # Install specific version
pip list                        # Show installed packages
pip freeze > requirements.txt   # Export dependencies
pip install -r requirements.txt # Install from file
pip uninstall package_name      # Remove package
pip show package_name           # Package info
```

### References
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [PyPI - Python Package Index](https://pypi.org/)

---

## 6. REPL vs Script vs Notebook Comparison

### Decision
Create comparison table for when to use each approach.

| Approach | Best For | Limitations |
|----------|----------|-------------|
| REPL | Quick experiments, testing ideas, learning | No persistence, hard to share |
| Script (.py) | Automation, production code, CLI tools | No inline visualization |
| Notebook (.ipynb) | Data analysis, teaching, documentation | Less suitable for production apps |

### References
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Python REPL Tips](https://docs.python.org/3/tutorial/interpreter.html)

---

## 7. Meme Sources Research

### Decision
Use popular programming memes that are:
1. Appropriate for educational context
2. Related to Python or programming in general
3. Available in good quality
4. Not copyrighted (or with permissive licenses)

### Meme Ideas for Lecture 1
1. **Python naming meme**: Monty Python vs actual snake confusion
2. **Indentation meme**: "Python programmers when they see a missing indent"
3. **"It just works" meme**: Python simplicity vs other languages
4. **Virtual environment meme**: "My code works on my machine"

### Sources
- Create original memes using meme generators
- Use royalty-free meme templates
- Reference popular programmer humor (with attribution if needed)

---

## 8. Code Examples Planning

### Decision
Design 5+ progressive code examples that build on each other.

### Planned Examples

1. **Hello World** (print basics)
```python
print("Hello, World!")
print("Привіт, Світе!")
```

2. **Variables and Types**
```python
name = "Python"
version = 3.12
is_awesome = True
print(type(name), type(version), type(is_awesome))
```

3. **User Input**
```python
name = input("Як тебе звати? ")
print(f"Привіт, {name}!")
```

4. **Basic Arithmetic**
```python
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
```

5. **F-string Formatting**
```python
price = 199.99
quantity = 3
total = price * quantity
print(f"Товар: {quantity} шт. × {price:.2f} грн = {total:.2f} грн")
```

---

## 9. Exercises Planning

### Exercise 1: Greeting Program
**Task**: Write a program that asks for the user's name and age, then prints a greeting with their birth year.

**Skills tested**: input(), print(), f-strings, basic arithmetic

### Exercise 2: Simple Calculator
**Task**: Create a program that takes two numbers and an operator (+, -, *, /) and prints the result.

**Skills tested**: input(), type conversion, operators, f-strings

---

## 10. Additional References (Non-Russian)

### Official Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

### English Resources
- [Real Python](https://realpython.com/) - tutorials and articles
- [Python for Beginners](https://www.pythonforbeginners.com/)
- [W3Schools Python](https://www.w3schools.com/python/)

### Ukrainian Resources
- [Prometheus Python Course](https://courses.prometheus.org.ua/) - if available
- [DOU.ua Python Articles](https://dou.ua/lenta/tags/Python/)

### Video Resources
- [Corey Schafer YouTube](https://www.youtube.com/c/Coreyms) - excellent Python tutorials
- [Tech With Tim](https://www.youtube.com/c/TechWithTim) - beginner-friendly

---

## Summary

All research items resolved. No NEEDS CLARIFICATION remaining. Ready for Phase 1 design.
