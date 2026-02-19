import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

outdir = r"d:\applied_software_development_python_2026\temp_imgs"

downloads = [
    # Intellipaat docstring images
    ("ip_docstring1.png", "https://images.intellipaat.com/wp-content/uploads/2025/04/Docstrings-in-Python-1.png"),
    ("ip_why_docstrings.png", "https://images.intellipaat.com/wp-content/uploads/2025/04/Why-Use-Docstrings-in-Python.png"),
    ("ip_func_docstring.png", "https://images.intellipaat.com/wp-content/uploads/2025/04/Function-Method-Docstrings.png"),
    ("ip_class_docstring.png", "https://images.intellipaat.com/wp-content/uploads/2025/04/Class-Docstrings.png"),
    ("ip_help_func.jpg", "https://images.intellipaat.com/wp-content/uploads/2025/05/docstrings-in-Python-help-function.jpg"),
    ("ip_doc_attr.jpg", "https://images.intellipaat.com/wp-content/uploads/2025/05/python-docstrings-with-doc-function.jpg"),
    ("ip_data_validation.png", "https://images.intellipaat.com/wp-content/uploads/2025/04/to-document-a-data-validation-utility.png"),

    # Intellipaat modules images
    ("ip_mod1.png", "https://intellipaat.com/blog/wp-content/uploads/2025/01/9-6.png"),
    ("ip_mod2.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/Screenshot-2025-02-18-202113.png"),
    ("ip_mod3.png", "https://intellipaat.com/blog/wp-content/uploads/2025/01/10-3.png"),
    ("ip_mod4.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/Screenshot-2025-02-18-204124.png"),
    ("ip_mod5.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/Screenshot-2025-02-18-210541.png"),
    ("ip_mod6.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/Screenshot-2025-02-18-211442.png"),
    ("ip_mod7.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/Screenshot-2025-02-18-212719-2.png"),

    # Wikimedia Python images
    ("wm_python_script.svg", "https://upload.wikimedia.org/wikipedia/commons/b/b8/Python_script.svg"),
    ("wm_batteries.jpg", "https://upload.wikimedia.org/wikipedia/commons/6/68/Python_batteries_included.jpg"),
    ("wm_build_install.png", "https://upload.wikimedia.org/wikipedia/commons/7/7e/Python_build_and_install.png"),

    # GitHub Python tutorial modules
    ("gh_modules.png", "https://raw.githubusercontent.com/Akuli/python-tutorial/master/images/modules.png"),
]

for fname, url in downloads:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=15)
        data = resp.read()
        path = os.path.join(outdir, fname)
        with open(path, 'wb') as f:
            f.write(data)
        print(f"OK {len(data):>8d} bytes  {fname}")
    except Exception as e:
        print(f"FAIL {fname}: {e}")
