import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

outdir = r"d:\applied_software_development_python_2026\temp_imgs"

def check_and_download(url, filename):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=15)
        ct = resp.headers.get('Content-Type', '')
        data = resp.read()
        if 'image' in ct and len(data) > 500:
            path = os.path.join(outdir, filename)
            with open(path, 'wb') as f:
                f.write(data)
            print(f"  OK {len(data):>8d} bytes | {ct:25s} | {filename:40s} | {url}")
            return True
        else:
            print(f"  SKIP (ct={ct}, size={len(data)}) | {url}")
            return False
    except Exception as e:
        print(f"  FAIL {str(e)[:60]:60s} | {url}")
        return False

urls = [
    # TutorialsTeacher - different URL patterns
    ("https://www.tutorialsteacher.com/Content/images/python/exception-classes.png", "tt_exc_classes.png"),
    ("https://www.tutorialsteacher.com/Content/images/python/python-exception-heirarchy.png", "tt_exc_hierarchy.png"),
    ("https://www.tutorialsteacher.com/Content/images/python/module.png", "tt_module.png"),
    ("https://www.tutorialsteacher.com/Content/images/python/import-module.png", "tt_import.png"),
    ("https://www.tutorialsteacher.com/Content/images/python/python-package.png", "tt_package.png"),

    # Simplified Python exception hierarchy
    ("https://simplifiedpython.net/wp-content/uploads/2018/10/Python-Exception-Hierarchy.png", "sp_exc_hierarchy.png"),

    # Toppr
    ("https://assets.toppr.com/v2/content/python-exception-hierarchy.png", "toppr_exc.png"),

    # Try AskPython which typically has good images
    ("https://journaldev.nyc3.cdn.digitaloceanspaces.com/2019/02/python-exception-handling-flowchart.png", "jd_exc_flow.png"),

    # DigitalOcean tutorials
    ("https://journaldev.nyc3.cdn.digitaloceanspaces.com/2019/07/python-import-module.png", "jd_import.png"),
    ("https://journaldev.nyc3.cdn.digitaloceanspaces.com/2019/02/Python-Exception-Hierarchy.png", "jd_exc_hierarchy.png"),

    # AskPython
    ("https://www.askpython.com/wp-content/uploads/2019/06/python-exception-handling-1-768x512.png", "ap_exc.png"),
    ("https://www.askpython.com/wp-content/uploads/2019/06/python-module-import.png", "ap_import.png"),
    ("https://www.askpython.com/wp-content/uploads/2019/07/python-package-structure.png", "ap_package.png"),
    ("https://www.askpython.com/wp-content/uploads/2019/06/python-import.png", "ap_import2.png"),
    ("https://www.askpython.com/wp-content/uploads/2019/06/Python-name-main.png", "ap_name_main.png"),
    ("https://www.askpython.com/wp-content/uploads/2019/06/python-docstring.png", "ap_docstring.png"),

    # Python-course.eu
    ("https://python-course.eu/images/python-tutorial/exception_hierarchy.png", "pc_exc_hierarchy.png"),
    ("https://python-course.eu/images/python-tutorial/modules_and_modular_programming.png", "pc_modules.png"),

    # BeginnersBook alt URLs
    ("https://beginnersbook.com/wp-content/uploads/2019/03/Python_exception_handling.jpg", "bb_exc.jpg"),
    ("https://beginnersbook.com/wp-content/uploads/2018/03/python_if_name_main.jpg", "bb_name_main.jpg"),

    # Scaler Topics (d1g0iq4cbcvjcd.cloudfront.net)
    ("https://www.scaler.com/topics/images/python-exception-hierarchy.webp", "sc_exc.webp"),

    # LogRocket
    ("https://blog.logrocket.com/wp-content/uploads/2022/11/Python-exception-class-hierarchy.png", "lr_exc_hierarchy.png"),

    # Medium / Towards Data Science images (hash-based)
    ("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zE_MsMYeOJV6YaFJLGWKzg.png", "med_exc.png"),

    # Programiz alternatives
    ("https://cdn.programiz.com/cdn/farfuture/7-WGCD8LXFnYSNjTlPDljYS_QLwAw9a_utUemHIGDY/mtime:1612782174/sites/tutorial2program/files/PackageModuleStructure.jpg", "prg_pkg_alt.jpg"),
    ("https://cdn.programiz.com/sites/tutorial2program/files/working-of-python-import.png", "prg_import.png"),
    ("https://cdn.programiz.com/sites/tutorial2program/files/python-import-statement.png", "prg_import2.png"),
    ("https://cdn.programiz.com/sites/tutorial2program/files/python-package-structure.png", "prg_pkg_struct.png"),
    ("https://cdn.programiz.com/sites/tutorial2program/files/ModuleStructure.jpg", "prg_mod_struct.jpg"),

    # W3Resource
    ("https://www.w3resource.com/w3r_images/python-docstring-image.png", "w3r_docstring.png"),
]

for url, filename in urls:
    check_and_download(url, filename)
