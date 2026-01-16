#!/usr/bin/env python3
"""
Sync course manifest from Notion to local JSON file.

This script pulls the latest course structure from Notion and updates
the local manifest.json file with any changes.
"""

import json
from pathlib import Path

# Notion page IDs discovered from search
NOTION_PAGES = {
    # New primer pages (not in current manifest)
    "python-primer": {
        "id": "python-primer",
        "notion_id": "6416c20b-3d33-4153-9697-ca0edbfb11ec",
        "title": "Day 0.5: Python Primer for Absolute Beginners",
        "parent_id": None,
        "order": 0.5,
        "language": "python",
        "week": "foundations",
        "notion_url": "https://www.notion.so/6416c20b3d3341539697ca0edbfb11ec",
        "sections": [
            "Purpose",
            "Setup Verification",
            "Core Concepts",
            "Exercises",
            "Common Beginner Mistakes",
            "Self-Assessment Checklist",
            "Python vs. R vs. MATLAB Quick Reference"
        ],
        "learning_objectives": [
            "Run Python code interactively and from scripts",
            "Declare variables and understand Python's dynamic typing",
            "Write functions that take parameters and return values",
            "Use basic control flow (if/else, for loops, while loops)",
            "Work with lists and dictionaries",
            "Import and use modules",
            "Read Python error messages without panic"
        ],
        "tasks": []
    },
    "cpp-primer": {
        "id": "cpp-primer",
        "notion_id": "025d4011-a8d3-4710-a6dc-71d362a7a987",
        "title": "Day 7.5: C++ Primer for Absolute Beginners",
        "parent_id": None,
        "order": 7.5,
        "language": "cpp",
        "week": "foundations",
        "notion_url": "https://www.notion.so/025d4011a8d34710a6dc71d362a7a987",
        "sections": [
            "Purpose",
            "Setup Verification",
            "Core Concepts",
            "Compilation Basics",
            "Exercises",
            "Self-Assessment Checklist"
        ],
        "learning_objectives": [
            "Compile and run a simple C++ program",
            "Declare variables with proper types",
            "Write functions that take parameters and return values",
            "Use basic control flow (if/else, for loops, while loops)",
            "Understand what #include, std::, and main() mean",
            "Read the compiler error messages without panic"
        ],
        "tasks": []
    }
}


def load_manifest():
    """Load existing manifest from JSON file."""
    manifest_path = Path(__file__).parent / "course_manifest" / "manifest.json"
    with open(manifest_path, 'r') as f:
        return json.load(f)


def save_manifest(manifest):
    """Save updated manifest to JSON file."""
    manifest_path = Path(__file__).parent / "course_manifest" / "manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"✓ Manifest saved to {manifest_path}")


def add_new_pages(manifest):
    """Add new primer pages to manifest."""
    new_pages_added = []

    for page_key, page_data in NOTION_PAGES.items():
        # Check if page already exists
        existing = next((p for p in manifest["pages"] if p["notion_id"] == page_data["notion_id"]), None)

        if not existing:
            manifest["pages"].append(page_data)
            new_pages_added.append(page_data["title"])
            print(f"  + Added: {page_data['title']}")

    return new_pages_added


def sort_pages(manifest):
    """Sort pages by order field."""
    manifest["pages"] = sorted(manifest["pages"], key=lambda x: x.get("order", 999))


def main():
    print("=" * 60)
    print("Syncing course manifest from Notion...")
    print("=" * 60)

    # Load existing manifest
    print("\n1. Loading existing manifest...")
    manifest = load_manifest()
    print(f"   Current pages: {len(manifest['pages'])}")

    # Add new pages
    print("\n2. Adding new pages from Notion...")
    new_pages = add_new_pages(manifest)

    if new_pages:
        print(f"\n   Added {len(new_pages)} new page(s)")
    else:
        print("   No new pages to add")

    # Sort pages by order
    print("\n3. Sorting pages by order...")
    sort_pages(manifest)
    print("   ✓ Pages sorted")

    # Save updated manifest
    print("\n4. Saving updated manifest...")
    save_manifest(manifest)

    print("\n" + "=" * 60)
    print("Sync complete!")
    print("=" * 60)

    if new_pages:
        print("\nNew pages added:")
        for page in new_pages:
            print(f"  • {page}")


if __name__ == "__main__":
    main()
