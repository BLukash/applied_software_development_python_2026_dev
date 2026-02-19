#!/bin/bash
# Check a comprehensive list of educational Python image URLs

check_url() {
    local url="$1"
    local desc="$2"
    code=$(curl -sI -o /dev/null -w "%{http_code}" -L "$url" 2>/dev/null)
    if [ "$code" = "200" ]; then
        ctype=$(curl -sI -L "$url" 2>/dev/null | grep -i "^content-type:" | head -1 | tr -d '\r')
        echo "OK $code | $ctype | $desc | $url"
    else
        echo "FAIL $code | $desc | $url"
    fi
}

# Exception Hierarchy
check_url "https://www.trytoprogram.com/images/python_exception.jpg" "exception hierarchy - trytoprogram"
check_url "https://intellipaat.com/blog/wp-content/uploads/2018/12/7.png" "exception handling - intellipaat"
check_url "https://intellipaat.com/mediaFiles/2018/12/2.jpg" "exception handling - intellipaat 2"
check_url "https://intellipaat.com/blog/wp-content/uploads/2018/12/6.png" "exception handling - intellipaat 3"
check_url "https://www.w3schools.com/python/img_tryexcept.png" "try except - w3schools"

# Package Structure
check_url "https://cdn.programiz.com/sites/tutorial2program/files/packages-in-python.png" "package structure - programiz"
check_url "https://cdn.programiz.com/sites/tutorial2program/files/PackageModuleStructure.jpg" "package module structure - programiz"

# Python Docs
check_url "https://docs.python.org/3/_images/pathlib-inheritance.png" "pathlib inheritance - python docs"
check_url "https://docs.python.org/3/_images/logging_flow.png" "logging flow - python docs"
check_url "https://docs.python.org/3/_static/py.svg" "python logo - python docs"

# Wikimedia
check_url "https://upload.wikimedia.org/wikipedia/commons/c/c5/Python-embedding-and-extending.png" "embedding extending - wikimedia"
check_url "https://upload.wikimedia.org/wikipedia/commons/1/1f/Python_logo_01.svg" "python logo - wikimedia"
check_url "https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg" "python wordmark - wikimedia"
check_url "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/1200px-Python_logo_and_wordmark.svg.png" "python wordmark png - wikimedia"

# Various Tutorial Sites
check_url "https://www.w3resource.com/w3r_images/python-docstring-image.png" "docstring - w3resource"
check_url "https://static.javatpoint.com/python/images/python-exception-handling.png" "exception handling - javatpoint"
check_url "https://static.javatpoint.com/python/images/python-exception-handling2.png" "exception handling 2 - javatpoint"
check_url "https://static.javatpoint.com/python/images/python-modules.png" "modules - javatpoint"
check_url "https://static.javatpoint.com/python/images/python-packages.png" "packages - javatpoint"

# Specific known blog images
check_url "https://i.imgur.com/VBo28yN.png" "python exception hierarchy - imgur"
check_url "https://www.guru99.com/images/Pythonnew/Python18.1.png" "exception - guru99"
check_url "https://www.guru99.com/images/Pythonnew/Python18.2.png" "exception 2 - guru99"

# GitHub raw content
check_url "https://raw.githubusercontent.com/python/cpython/main/Doc/images/pathlib-inheritance.svg" "pathlib inheritance svg - github cpython"
check_url "https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100-python.png" "python exercises - github"

# W3Schools
check_url "https://www.w3schools.com/python/img_python.png" "python - w3schools"
check_url "https://www.w3schools.com/python/trypython_default.png" "try python - w3schools"
