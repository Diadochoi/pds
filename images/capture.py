import os
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))

jobs = [
    ("thumbnail.html", "thumbnail.png", 1080, 1080),
    ("body-1.html", "body-1.png", 1200, None),
    ("body-2.html", "body-2.png", 1200, None),
    ("body-3.html", "body-3.png", 1200, None),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for html_file, png_file, width, height in jobs:
        page = browser.new_page(viewport={"width": width, "height": height or 800})
        page.goto("file:///" + os.path.join(BASE, html_file).replace("\\", "/"))
        if height is None:
            # full page screenshot for variable height content
            page.screenshot(path=os.path.join(BASE, png_file), full_page=True)
        else:
            page.screenshot(path=os.path.join(BASE, png_file))
        page.close()
    browser.close()

print("done")
