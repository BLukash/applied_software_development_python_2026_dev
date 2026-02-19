import urllib.request
import ssl
import re
import os
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

outdir = r"d:\applied_software_development_python_2026\temp_imgs"

def fetch_page(url):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        })
        resp = urllib.request.urlopen(req, context=ctx, timeout=20)
        return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"ERROR: {e}"

def find_all_images(html, base_url):
    from urllib.parse import urljoin
    patterns = [
        r'(?:src|data-src|data-lazy-src|data-original)=["\']([^"\']+\.(?:png|jpg|jpeg|webp|gif)(?:\?[^"\']*)?)["\']',
    ]
    imgs = []
    seen = set()
    for pat in patterns:
        for m in re.findall(pat, html, re.IGNORECASE):
            full_url = urljoin(base_url, m)
            if full_url not in seen:
                seen.add(full_url)
                imgs.append(full_url)
    return imgs

def check_download(url, filename):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=15)
        ct = resp.headers.get('Content-Type', '')
        data = resp.read()
        if 'image' in ct and len(data) > 2000:
            path = os.path.join(outdir, filename)
            with open(path, 'wb') as f:
                f.write(data)
            return True, len(data), ct
        return False, len(data), ct
    except Exception as e:
        return False, 0, str(e)[:50]

# Search more Intellipaat pages
print("=== Intellipaat - More Pages ===")
ip_pages = [
    ("https://intellipaat.com/blog/python-exception-hierarchy/", "ip_exc_hier"),
    ("https://intellipaat.com/blog/python-exceptions/", "ip_exc"),
    ("https://intellipaat.com/blog/tutorial/python-tutorial/python-exception-types/", "ip_exc_types"),
    ("https://intellipaat.com/blog/python-import-module/", "ip_import"),
    ("https://intellipaat.com/blog/python-packages/", "ip_packages"),
    ("https://intellipaat.com/blog/if-name-main-python/", "ip_name_main"),
    ("https://intellipaat.com/blog/__name__-in-python/", "ip_name"),
    ("https://intellipaat.com/blog/python-standard-library/", "ip_stdlib"),
]

for page_url, prefix in ip_pages:
    print(f"\n--- {prefix}: {page_url} ---")
    html = fetch_page(page_url)
    if html.startswith("ERROR"):
        print(f"  {html}")
        continue
    imgs = find_all_images(html, page_url)
    skip = ['logo', 'icon', 'footer', 'header', 'ytimg', 'avatar', 'badge', 'cert', 'play', 'check',
            'Lithin', 'Ayaan', 'Course', 'Banner', 'Training', 'Data-Science', 'IU-Course', 'Job-Focused',
            'Foundaion', 'Full-Stack', 'C-and-Data', 'Python-Course', 'cta']
    for img in imgs:
        if any(s in img for s in skip):
            continue
        if 'intellipaat.com' in img or 'images.intellipaat.com' in img:
            fname = img.split('/')[-1][:60].replace('?', '_').replace('&', '_')
            ok, size, ct = check_download(img, f"{prefix}_{fname}")
            if ok:
                print(f"  OK {size:>8d} | {img}")

# Try more Programiz pages
print("\n=== Programiz - More Pages ===")
prg_pages = [
    ("https://www.programiz.com/python-programming/exception-handling", "prg_exc"),
    ("https://www.programiz.com/python-programming/user-defined-exception", "prg_user_exc"),
    ("https://www.programiz.com/python-programming/if-name-main", "prg_name_main"),
    ("https://www.programiz.com/python-programming/import", "prg_import"),
    ("https://www.programiz.com/python-programming/global-keyword", "prg_global"),
]

for page_url, prefix in prg_pages:
    print(f"\n--- {prefix}: {page_url} ---")
    html = fetch_page(page_url)
    if html.startswith("ERROR"):
        print(f"  {html}")
        continue
    # Look for cdn.programiz.com images
    for m in re.findall(r'(cdn\.programiz\.com/[^"\'> ]*\.(?:png|jpg|jpeg|webp))', html, re.IGNORECASE):
        url = f"https://{m}"
        fname = m.split('/')[-1][:60]
        ok, size, ct = check_download(url, f"{prefix}_{fname}")
        if ok:
            print(f"  OK {size:>8d} | {url}")
    # Also check relative paths
    for m in re.findall(r'src="(/sites/[^"]*\.(?:png|jpg|jpeg|webp))"', html, re.IGNORECASE):
        url = f"https://cdn.programiz.com{m}"
        fname = m.split('/')[-1][:60]
        ok, size, ct = check_download(url, f"{prefix}_{fname}")
        if ok:
            print(f"  OK {size:>8d} | {url}")

# Try Python docs for more diagrams
print("\n=== Python Docs - Searching for all images ===")
doc_pages = [
    "https://docs.python.org/3/reference/import.html",
    "https://docs.python.org/3/tutorial/modules.html",
    "https://docs.python.org/3/library/exceptions.html",
    "https://docs.python.org/3/howto/logging.html",
]
for page_url in doc_pages:
    html = fetch_page(page_url)
    if not html.startswith("ERROR"):
        for m in re.findall(r'_images/([^"\'> ]*\.(?:png|jpg|svg))', html):
            full = f"https://docs.python.org/3/_images/{m}"
            print(f"  {page_url}: {full}")
