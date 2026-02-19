import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

outdir = r"d:\applied_software_development_python_2026\temp_imgs"

downloads = [
    ("guru99_exc1.png", "https://www.guru99.com/images/Pythonnew/Python18.1.png"),
    ("guru99_exc2.png", "https://www.guru99.com/images/Pythonnew/Python18.2.png"),
    ("guru99_exc3.png", "https://www.guru99.com/images/Pythonnew/Python18.3.png"),
    ("guru99_exc4.png", "https://www.guru99.com/images/Pythonnew/Python18.4.png"),
    ("guru99_exc5.png", "https://www.guru99.com/images/Pythonnew/Python18.5.png"),
    ("guru99_exc6.png", "https://www.guru99.com/images/Pythonnew/Python18.6.png"),
    ("guru99_exc7.png", "https://www.guru99.com/images/Pythonnew/Python18.7.png"),
    ("guru99_doc1.png", "https://www.guru99.com/images/Pythonnew/Python14.1.png"),
    ("guru99_doc2.png", "https://www.guru99.com/images/Pythonnew/Python14.2.png"),
    ("guru99_mod1.png", "https://www.guru99.com/images/Pythonnew/Python15.1.png"),
    ("guru99_mod2.png", "https://www.guru99.com/images/Pythonnew/Python15.2.png"),
    ("guru99_mod3.png", "https://www.guru99.com/images/Pythonnew/Python15.3.png"),
    ("programiz_pkg.png", "https://cdn.programiz.com/sites/tutorial2program/files/packages-in-python.png"),
    ("programiz_pkgmod.jpg", "https://cdn.programiz.com/sites/tutorial2program/files/PackageModuleStructure.jpg"),
    ("intellipaat1.png", "https://intellipaat.com/blog/wp-content/uploads/2018/12/7.png"),
    ("intellipaat2.jpg", "https://intellipaat.com/mediaFiles/2018/12/2.jpg"),
    ("intellipaat3.png", "https://intellipaat.com/blog/wp-content/uploads/2018/12/6.png"),
    ("dotnet79.png", "https://dotnettutorials.net/wp-content/uploads/2020/02/word-image-79.png"),
    ("dotnet80.png", "https://dotnettutorials.net/wp-content/uploads/2020/02/word-image-80.png"),
    ("dotnet81.png", "https://dotnettutorials.net/wp-content/uploads/2020/02/word-image-81.png"),
    ("wikimedia_embed.png", "https://upload.wikimedia.org/wikipedia/commons/c/c5/Python-embedding-and-extending.png"),
    ("pydocs_pathlib.png", "https://docs.python.org/3/_images/pathlib-inheritance.png"),
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
