import urllib.request
import ssl
import re
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

outdir = r"d:\applied_software_development_python_2026\temp_imgs"

def fetch_page(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=15)
        return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"ERROR: {e}"

def extract_images(html, base_url=""):
    # Find all image references
    patterns = [
        r'src="([^"]*\.(?:png|jpg|jpeg|webp|gif|svg)[^"]*)"',
        r"src='([^']*\.(?:png|jpg|jpeg|webp|gif|svg)[^']*)'",
        r'data-src="([^"]*\.(?:png|jpg|jpeg|webp|gif|svg)[^"]*)"',
        r'data-lazy-src="([^"]*\.(?:png|jpg|jpeg|webp|gif|svg)[^"]*)"',
        r'srcset="([^"]*\.(?:png|jpg|jpeg|webp|gif|svg)[^ "]*)',
    ]
    urls = set()
    for pat in patterns:
        for match in re.findall(pat, html, re.IGNORECASE):
            if any(skip in match.lower() for skip in ['logo', 'icon', 'avatar', 'favicon', 'emoji', 'ads', 'tracking', 'pixel', 'badge', 'footer', 'header', 'nav']):
                continue
            if match.startswith('//'):
                match = 'https:' + match
            elif match.startswith('/'):
                from urllib.parse import urlparse
                parsed = urlparse(base_url)
                match = f"{parsed.scheme}://{parsed.netloc}{match}"
            urls.add(match)
    return urls

def check_url(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        ct = resp.headers.get('Content-Type', '')
        cl = resp.headers.get('Content-Length', '?')
        return resp.status, ct, cl
    except Exception as e:
        return 0, str(e)[:50], '0'

# Scrape specific pages for relevant images
pages = [
    # Exception hierarchy focused pages
    ("https://rollbar.com/blog/python-built-in-exceptions/", "rollbar exceptions"),
    ("https://www.pythonforbeginners.com/exceptions/exception-handling-in-python", "pythonforbeginners exceptions"),
    ("https://www.toppr.com/guides/python-guide/tutorials/python-exceptions/python-exception-hierarchy/", "toppr exception hierarchy"),

    # Docstring focused
    ("https://www.datacamp.com/tutorial/docstrings-python", "datacamp docstrings"),

    # Import focused
    ("https://www.pythontutorial.net/python-basics/python-import/", "pythontutorial import"),

    # Name main focused
    ("https://www.freecodecamp.org/news/if-name-main-python/", "freecodecamp name main"),

    # Broader tutorial sites with images
    ("https://www.softwaretestinghelp.com/python/python-exception-handling/", "softwaretestinghelp exceptions"),
    ("https://www.boardinfinity.com/blog/python-exception-hierarchy/", "boardinfinity exception hierarchy"),
]

print("=== Scraping pages for images ===")
for url, desc in pages:
    print(f"\n--- {desc} ({url}) ---")
    html = fetch_page(url)
    if html.startswith("ERROR"):
        print(f"  {html}")
        continue
    images = extract_images(html, url)
    for img in sorted(images):
        if 'http' in img:
            status, ct, cl = check_url(img)
            if status == 200 and 'image' in str(ct):
                print(f"  OK {cl:>10s} | {ct:30s} | {img}")

# Also check more specific image URLs from known sources
print("\n=== Checking specific known URLs ===")
specific_urls = [
    # Rollbar
    ("https://rollbar.com/wp-content/uploads/2022/10/python-exception-class-hierarchy-1024x652.png", "exception hierarchy - rollbar"),
    ("https://rollbar.com/wp-content/uploads/2022/10/python-exception-class-hierarchy.png", "exception hierarchy full - rollbar"),

    # Board Infinity
    ("https://www.boardinfinity.com/blog/content/images/2023/01/Python-Exception-Hierarchy.png", "exception hierarchy - boardinfinity"),

    # Software Testing Help
    ("https://www.softwaretestinghelp.com/wp-content/qa/uploads/2021/04/Python-Exception-Hierarchy.png", "exception hierarchy - sth"),

    # FreeCodeCamp
    ("https://www.freecodecamp.org/news/content/images/2022/09/name-main-python.png", "name main - freecodecamp"),
    ("https://www.freecodecamp.org/news/content/images/2022/09/name-main.png", "name main 2 - freecodecamp"),
    ("https://www.freecodecamp.org/news/content/images/size/w2000/2022/09/If-__name__-__main__-in-Python.png", "name main 3 - freecodecamp"),

    # Additional sources
    ("https://www.tutorialsteacher.com/Content/images/python/exception-classes.png", "exception classes - tutorialsteacher"),
    ("https://www.tutorialsteacher.com/Content/images/python/python-exception-heirarchy.png", "exception hierarchy - tutorialsteacher"),
    ("https://www.tutorialsteacher.com/Content/images/python/module1.png", "module - tutorialsteacher"),
    ("https://www.tutorialsteacher.com/Content/images/python/import.png", "import - tutorialsteacher"),
    ("https://www.tutorialsteacher.com/Content/images/python/docstring.png", "docstring - tutorialsteacher"),
    ("https://www.tutorialsteacher.com/Content/images/python/package.png", "package - tutorialsteacher"),

    # Simplified Python
    ("https://simplifiedpython.net/wp-content/uploads/2018/10/Python-Exception-Hierarchy.png", "exception hierarchy - simplifiedpython"),

    # BeginnersBook
    ("https://beginnersbook.com/wp-content/uploads/2019/03/Python_Exception_Handling_flow.jpg", "exception flow - beginnersbook"),
    ("https://beginnersbook.com/wp-content/uploads/2018/05/Python_packages.jpg", "packages - beginnersbook"),
    ("https://beginnersbook.com/wp-content/uploads/2018/03/python_if_name_main_example.jpg", "name main - beginnersbook"),
]

for url, desc in specific_urls:
    status, ct, cl = check_url(url)
    if status == 200 and 'image' in str(ct):
        print(f"  OK {cl:>10s} | {ct:30s} | {desc:50s} | {url}")
    else:
        print(f"  FAIL {status} | {desc}")
