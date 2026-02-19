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
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=20)
        return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"ERROR: {e}"

def find_content_images(html, base_url):
    """Find likely content images (not logos/icons)"""
    from urllib.parse import urlparse, urljoin
    patterns = [
        r'(?:src|data-src|data-lazy-src|data-original|data-srcset)=["\']([^"\']*\.(?:png|jpg|jpeg|webp|gif|svg)(?:\?[^"\']*)?)["\']',
    ]
    imgs = set()
    for pat in patterns:
        for m in re.findall(pat, html, re.IGNORECASE):
            skip_words = ['logo', 'icon', 'avatar', 'favicon', 'emoji', 'pixel', 'tracking', 'ad-', 'ads/', 'banner', 'badge', 'play-button', 'share', 'social', 'footer', 'header', 'menu', 'nav-', 'arrow', 'close', 'search']
            if any(w in m.lower() for w in skip_words):
                continue
            full_url = urljoin(base_url, m)
            imgs.add(full_url)
    return imgs

def check_image(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        ct = resp.headers.get('Content-Type', '')
        data = resp.read()
        if ('image' in ct or url.endswith('.svg')) and len(data) > 1000:
            return True, ct, len(data)
        return False, ct, len(data)
    except Exception as e:
        return False, str(e)[:50], 0

# Pages to scrape - focusing on sites that serve images in HTML
pages = {
    # Python exception handling and hierarchy
    "https://www.pythonforbeginners.com/exceptions/exception-handling-in-python": "pfb_exc",
    "https://www.geeksforgeeks.org/python-exception-hierarchy/": "gfg_exc_hier",  # try anyway
    "https://www.pythontutorial.net/python-basics/python-exception-handling/": "ptn_exc",
    "https://overiq.com/python-101/exception-handling-in-python/": "overiq_exc",
    "https://www.pythontutorial.net/python-basics/python-try-except/": "ptn_tryexc",

    # Python modules and imports
    "https://www.pythontutorial.net/python-basics/python-module/": "ptn_mod",
    "https://www.pythontutorial.net/python-basics/python-packages/": "ptn_pkg",

    # Python __name__ == __main__
    "https://www.pythontutorial.net/python-basics/python-main/": "ptn_main",

    # Docstrings
    "https://www.pythontutorial.net/python-basics/python-docstrings/": "ptn_docs",

    # Broader Python tutorials with images
    "https://www.pythoncheatsheet.org/cheatsheet/exception-handling": "pcs_exc",
    "https://www.educba.com/python-exception-hierarchy/": "educba_exc",
    "https://www.analyticsvidhya.com/blog/2020/12/exception-handling-in-python/": "av_exc",
    "https://www.shiksha.com/online-courses/articles/exception-hierarchy-in-python/": "shiksha_exc",
}

for url, prefix in pages.items():
    print(f"\n=== {prefix}: {url} ===")
    html = fetch_page(url)
    if html.startswith("ERROR"):
        print(f"  {html}")
        continue
    if len(html) < 5000:
        print(f"  Too small ({len(html)} bytes) - likely JS-rendered or blocked")
        continue

    images = find_content_images(html, url)
    for img_url in sorted(images):
        ok, ct, size = check_image(img_url)
        if ok:
            print(f"  OK {size:>8d} | {ct:25s} | {img_url}")
