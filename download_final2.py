import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

outdir = r"d:\applied_software_development_python_2026\temp_imgs"

downloads = [
    # Intellipaat packages
    ("ip_pkg_what.png", "https://images.intellipaat.com/wp-content/uploads/2025/05/What-is-a-package.png"),
    ("ip_pkg_init.png", "https://images.intellipaat.com/wp-content/uploads/2025/05/init__.py-File-.png"),
    ("ip_pkg_modules.png", "https://images.intellipaat.com/wp-content/uploads/2025/05/Modules.png"),
    ("ip_pkg_subpackages.jpg", "https://images.intellipaat.com/wp-content/uploads/2025/05/Subpackages.jpg"),
    ("ip_pkg_create.png", "https://images.intellipaat.com/wp-content/uploads/2025/05/Step-1-Create-a-Package-Folder.png"),
    ("ip_pkg_add_init.png", "https://images.intellipaat.com/wp-content/uploads/2025/05/Add-the-__init__.py-File.png"),
    ("ip_pkg_add_subpkg.png", "https://images.intellipaat.com/wp-content/uploads/2025/05/Add-your-subpackages-and-Module.png"),
    ("ip_pkg_using.png", "https://images.intellipaat.com/wp-content/uploads/2025/05/Step-5-Using-Your-Package.png"),

    # Intellipaat imports
    ("ip_import_header.webp", "https://intellipaat.com/blog/wp-content/uploads/2026/02/Import-Files-from-Different-Folder-in-Python.webp"),
    ("ip_import_92.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/image-92.png"),
    ("ip_import_93.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/image-93.png"),
    ("ip_import_94.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/image-94.png"),
    ("ip_import_95.png", "https://intellipaat.com/blog/wp-content/uploads/2025/02/image-95.png"),
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
