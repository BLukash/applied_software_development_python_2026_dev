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
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
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
    for pat in patterns:
        for m in re.findall(pat, html, re.IGNORECASE):
            full_url = urljoin(base_url, m)
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

# 1. Scrape Intellipaat Python pages (they work!)
print("=== Intellipaat Pages ===")
intellipaat_pages = [
    "https://intellipaat.com/blog/tutorial/python-tutorial/python-exception-handling/",
    "https://intellipaat.com/blog/tutorial/python-tutorial/python-modules/",
    "https://intellipaat.com/blog/tutorial/python-tutorial/python-packages/",
    "https://intellipaat.com/blog/python-docstring/",
    "https://intellipaat.com/blog/if-name-main-in-python/",
    "https://intellipaat.com/blog/python-import-statement/",
]

for page_url in intellipaat_pages:
    print(f"\n--- {page_url} ---")
    html = fetch_page(page_url)
    if html.startswith("ERROR"):
        print(f"  {html}")
        continue
    imgs = find_all_images(html, page_url)
    skip = ['logo', 'icon', 'footer', 'header', 'ytimg', 'avatar', 'badge', 'cert', 'play', 'check']
    for img in imgs:
        if any(s in img.lower() for s in skip):
            continue
        if 'intellipaat.com' in img or 'cloudfront' in img:
            fname = img.split('/')[-1][:60].replace('?', '_').replace('&', '_')
            ok, size, ct = check_download(img, f"ip_{fname}")
            if ok:
                print(f"  OK {size:>8d} | {ct:25s} | {img}")

# 2. Try Wikimedia API for Python-related educational images
print("\n=== Wikimedia Commons API ===")
search_terms = [
    "python+programming+exception",
    "python+programming+module",
    "python+programming+package",
    "python+programming+import",
    "python+programming+docstring",
    "python+programming+standard+library",
]
import json
for term in search_terms:
    try:
        api_url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={term}&srnamespace=6&srlimit=5&format=json"
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        data = json.loads(resp.read())
        for result in data.get('query', {}).get('search', []):
            title = result['title']
            if any(ext in title.lower() for ext in ['.png', '.jpg', '.svg']):
                # Get actual image URL
                info_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.request.quote(title)}&prop=imageinfo&iiprop=url|size&format=json"
                req2 = urllib.request.Request(info_url, headers={'User-Agent': 'Mozilla/5.0'})
                resp2 = urllib.request.urlopen(req2, context=ctx, timeout=10)
                info = json.loads(resp2.read())
                pages = info.get('query', {}).get('pages', {})
                for page in pages.values():
                    imageinfo = page.get('imageinfo', [{}])[0]
                    img_url = imageinfo.get('url', '')
                    img_size = imageinfo.get('size', 0)
                    if img_url and img_size > 1000:
                        print(f"  {term}: {title} -> {img_url} ({img_size} bytes)")
    except Exception as e:
        print(f"  Error searching {term}: {e}")

# 3. Try GitHub search for educational Python images
print("\n=== GitHub Content Search ===")
github_repos = [
    "https://api.github.com/repos/Akuli/python-tutorial/contents/images",
    "https://api.github.com/repos/jerry-git/learn-python3/contents/images",
    "https://api.github.com/repos/trekhleb/learn-python/contents",
]
for repo_url in github_repos:
    try:
        req = urllib.request.Request(repo_url, headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/vnd.github.v3+json'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        files = json.loads(resp.read())
        for f in files:
            if isinstance(f, dict) and any(f.get('name', '').lower().endswith(ext) for ext in ['.png', '.jpg', '.svg']):
                print(f"  {f['name']} -> {f.get('download_url', '')}")
    except Exception as e:
        print(f"  Error: {e}")
