#!/usr/bin/env python3
"""
Sync course content from Notion.

This script fetches the course structure and content from Notion
and updates the local manifest.json file.

Usage:
    python scripts/sync_from_notion.py

Environment variables:
    NOTION_API_KEY: Notion integration token (required)
    NOTION_ROOT_PAGE_ID: Root page ID for the course (optional)
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Check for required environment variable
NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
if not NOTION_API_KEY:
    print("Error: NOTION_API_KEY environment variable not set")
    print("Create a Notion integration at https://www.notion.so/my-integrations")
    sys.exit(1)

# Course root page ID (from manifest or environment)
MANIFEST_PATH = Path("course_manifest/manifest.json")
ROOT_PAGE_ID = os.environ.get("NOTION_ROOT_PAGE_ID", "2dc342cf7cc8807b9122dc79f2781d1e")


def load_manifest() -> dict:
    """Load existing manifest or create empty one."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return {"course_title": "", "modules": [], "pages": []}


def save_manifest(manifest: dict) -> None:
    """Save manifest to file."""
    manifest["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Saved manifest to {MANIFEST_PATH}")


def main():
    print("=== Notion Sync ===")
    print()
    print(f"Root page: {ROOT_PAGE_ID}")
    print()

    # TODO: Implement Notion API integration
    # This would use the official Notion SDK or REST API to:
    # 1. Fetch the root page and its children
    # 2. Extract page titles, content, and structure
    # 3. Update the manifest with new content

    print("Note: Full Notion sync requires Notion API integration.")
    print("Current manifest was generated from Notion using Claude MCP tools.")
    print()
    print("To manually update:")
    print("1. Export content from Notion")
    print("2. Update course_manifest/manifest.json")
    print("3. Run 'make gen-from-manifest'")


if __name__ == "__main__":
    main()
