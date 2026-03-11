#!/usr/bin/env python3
"""Build script: renders src/template.html with src/content.yaml into dist/index.html."""

import os
import shutil

import yaml
from jinja2 import Environment, FileSystemLoader

SRC_DIR = os.path.join(os.path.dirname(__file__), "src")
DIST_DIR = os.path.join(os.path.dirname(__file__), "dist")


def build():
    # Load resume data
    with open(os.path.join(SRC_DIR, "content.yaml"), encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Render template
    env = Environment(loader=FileSystemLoader(SRC_DIR))
    template = env.get_template("template.html")
    html = template.render(**data)

    # Write output
    os.makedirs(DIST_DIR, exist_ok=True)
    output_path = os.path.join(DIST_DIR, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {output_path}")

    # Copy static assets
    for filename in ("style.css",):
        src = os.path.join(SRC_DIR, filename)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(DIST_DIR, filename))
            print(f"Copied {filename}")

    # Copy img directory if present
    img_src = os.path.join(SRC_DIR, "img")
    img_dst = os.path.join(DIST_DIR, "img")
    if os.path.exists(img_src):
        if os.path.exists(img_dst):
            shutil.rmtree(img_dst)
        shutil.copytree(img_src, img_dst)
        print(f"Copied img/")


if __name__ == "__main__":
    build()
