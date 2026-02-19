"""Download all lecture images locally."""
import json
import re
import os
import urllib.request
import urllib.error
import time
import hashlib

NOTEBOOK = "lectures/04-functions-modules-errors-oop/lecture-04.ipynb"
ASSETS_DIR = "lectures/04-functions-modules-errors-oop/assets/diagrams"

with open(NOTEBOOK, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Extract all images
images = []
for cell in nb["cells"]:
    if cell["cell_type"] == "markdown":
        src = cell["source"][0] if isinstance(cell["source"], list) else cell["source"]
        for match in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", src):
            images.append({"alt": match.group(1), "url": match.group(2)})

os.makedirs(ASSETS_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "image/webp,image/png,image/jpeg,image/*,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}

results = {}
for i, img in enumerate(images):
    alt = img["alt"]
    url = img["url"]

    # Create safe filename from alt text
    safe_name = re.sub(r"[^\w\-]", "-", alt.lower()).strip("-")
    safe_name = re.sub(r"-+", "-", safe_name)

    # Determine extension
    if ".webp" in url:
        ext = ".webp"
    elif ".gif" in url:
        ext = ".gif"
    elif ".png" in url:
        ext = ".png"
    elif ".svg" in url:
        ext = ".svg"
    else:
        ext = ".jpg"

    filename = f"{i+1:02d}-{safe_name[:40]}{ext}"
    filepath = os.path.join(ASSETS_DIR, filename)

    try:
        req = urllib.request.Request(url, headers=HEADERS)
        resp = urllib.request.urlopen(req, timeout=15)
        data = resp.read()
        content_type = resp.headers.get("Content-Type", "")

        # Verify it's actually an image
        if len(data) < 500:
            print(f"{i+1:2}. SKIP  {alt[:35]:35} too small ({len(data)} bytes)")
            results[url] = None
            continue

        # Check if response is HTML (error page) instead of image
        if b"<!DOCTYPE" in data[:200] or b"<html" in data[:200]:
            print(f"{i+1:2}. SKIP  {alt[:35]:35} got HTML instead of image")
            results[url] = None
            continue

        with open(filepath, "wb") as f:
            f.write(data)

        size_kb = len(data) / 1024
        print(f"{i+1:2}. OK    {alt[:35]:35} {size_kb:.0f}KB -> {filename}")
        results[url] = filename

    except Exception as e:
        print(f"{i+1:2}. FAIL  {alt[:35]:35} {str(e)[:60]}")
        results[url] = None

    time.sleep(0.3)  # Be polite

# Summary
ok = sum(1 for v in results.values() if v is not None)
fail = sum(1 for v in results.values() if v is None)
print(f"\nDownloaded: {ok}/{len(results)} ({fail} failed)")

# Save mapping for later use
with open("lectures/04-functions-modules-errors-oop/image_mapping.json", "w") as f:
    json.dump(results, f, indent=2)
