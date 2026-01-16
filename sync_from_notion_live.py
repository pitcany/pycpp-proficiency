#!/usr/bin/env python3
"""
Live sync script: Pull course structure from Notion and update manifest.json

This script connects to Notion using the integration token and dynamically
fetches all course pages, extracting metadata to update the local manifest.

Setup:
    1. Install dependencies:
       pip install notion-client

    2. Load Notion API key:
       source ~/Credentials/.secrets

Usage:
    python sync_from_notion_live.py

Requirements:
    - Python 3.7+
    - notion-client package
    - NOTION_API_KEY environment variable set
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

try:
    from notion_client import Client
except ImportError:
    print("Error: notion-client not installed")
    print("Install with: pip install notion-client")
    exit(1)


# Notion configuration
NOTION_TOKEN = os.getenv("NOTION_API_KEY")
if not NOTION_TOKEN:
    print("Error: NOTION_API_KEY environment variable not set")
    print("Please set it by running: source ~/Credentials/.secrets")
    exit(1)

ROOT_PAGE_ID = "2dc342cf-7cc8-807b-9122-dc79f2781d1e"  # Main course page


class NotionCourseSync:
    """Sync course structure from Notion to local manifest."""

    def __init__(self, token: str):
        self.client = Client(auth=token)
        self.pages_cache = {}

    def get_child_pages(self, page_id: str) -> List[str]:
        """Recursively get all child page IDs from a parent page."""
        clean_id = page_id.replace("-", "")

        try:
            # Get child blocks
            blocks = self.client.blocks.children.list(block_id=clean_id)
            child_page_ids = []

            for block in blocks.get("results", []):
                # Check if block is a child page
                if block.get("type") == "child_page":
                    child_id = block.get("id", "")
                    child_page_ids.append(child_id)

                    # Recursively get children of this page
                    grandchildren = self.get_child_pages(child_id)
                    child_page_ids.extend(grandchildren)

            return child_page_ids

        except Exception as e:
            print(f"    ⚠ Error getting children of {clean_id}: {e}")
            return []

    def search_course_pages(self) -> List[Dict]:
        """Get all course pages by traversing from root page."""
        print("  Fetching course pages from root...")

        # Start from root page and get all children
        child_ids = self.get_child_pages(ROOT_PAGE_ID)
        print(f"  Found {len(child_ids)} child pages")

        # Fetch metadata for each child page
        pages = []
        for child_id in child_ids:
            try:
                page = self.client.pages.retrieve(page_id=child_id)
                pages.append(page)
            except Exception as e:
                print(f"    ⚠ Error fetching page {child_id}: {e}")

        return pages

    def get_page_content(self, page_id: str) -> Dict:
        """Fetch full page content including blocks."""
        # Remove dashes from page_id if present
        clean_id = page_id.replace("-", "")

        # Get page metadata
        page = self.client.pages.retrieve(page_id=clean_id)

        # Get page blocks (content)
        blocks = self.client.blocks.children.list(block_id=clean_id)

        return {
            "metadata": page,
            "blocks": blocks.get("results", [])
        }

    def extract_page_metadata(self, page_data: Dict) -> Optional[Dict]:
        """Extract relevant metadata from a Notion page."""
        metadata = page_data.get("metadata", {})
        blocks = page_data.get("blocks", [])

        # Get page ID and title
        page_id = metadata.get("id", "")
        title_obj = metadata.get("properties", {}).get("title", {})
        title_content = title_obj.get("title", [])

        if not title_content:
            return None

        title = title_content[0].get("plain_text", "")

        # Determine page type and order from title
        page_info = self._parse_title(title)
        if not page_info:
            return None

        # Extract sections from headings in blocks
        sections = self._extract_sections(blocks)

        # Extract learning objectives
        learning_objectives = self._extract_learning_objectives(blocks)

        # Extract tasks/exercises
        tasks = self._extract_tasks(blocks, title)

        return {
            "id": page_info["id"],
            "notion_id": page_id.replace("-", ""),
            "title": title,
            "parent_id": page_info.get("parent_id"),
            "order": page_info["order"],
            "language": page_info["language"],
            "week": page_info["week"],
            "notion_url": f"https://www.notion.so/{page_id.replace('-', '')}",
            "sections": sections,
            "learning_objectives": learning_objectives,
            "tasks": tasks
        }

    def _parse_title(self, title: str) -> Optional[Dict]:
        """Parse title to extract page metadata."""
        # Day patterns
        day_match = re.match(r"Day (\d+(?:\.\d+)?):?\s*(.+)", title)
        if day_match:
            day_num = float(day_match.group(1))

            # Determine language and week
            if day_num < 1:
                language = "python" if "Python" in title else "mixed"
                week = "foundations"
            elif 1 <= day_num <= 7:
                language = "python"
                week = "week1"
            elif 7 < day_num <= 14:
                language = "cpp"
                week = "week2"
            else:
                language = "mixed"
                week = "week3"

            return {
                "id": f"day-{day_num:02.0f}" if day_num == int(day_num) else f"day-{day_num}",
                "order": int(day_num) if day_num == int(day_num) else day_num,
                "language": language,
                "week": week,
                "parent_id": None
            }

        # Setup/Foundation pages
        if "Setup" in title and "Day 0" in title:
            return {
                "id": "setup-day-0",
                "order": 0,
                "language": "mixed",
                "week": "foundations",
                "parent_id": None
            }

        if "Algorithmic Thinking" in title:
            return {
                "id": "algorithmic-thinking",
                "order": 1,
                "language": "theory",
                "week": "foundations",
                "parent_id": None
            }

        # Primer pages
        if "Python Primer" in title:
            return {
                "id": "python-primer",
                "order": 0.5,
                "language": "python",
                "week": "foundations",
                "parent_id": None
            }

        if "C++ Primer" in title:
            return {
                "id": "cpp-primer",
                "order": 7.5,
                "language": "cpp",
                "week": "foundations",
                "parent_id": None
            }

        return None

    def _extract_sections(self, blocks: List[Dict]) -> List[str]:
        """Extract section headings from page blocks."""
        sections = []

        for block in blocks:
            block_type = block.get("type", "")

            # Look for heading_2 blocks (## in markdown)
            if block_type == "heading_2":
                heading_obj = block.get("heading_2", {})
                rich_text = heading_obj.get("rich_text", [])
                if rich_text:
                    section_title = rich_text[0].get("plain_text", "")
                    if section_title and section_title not in ["Overview", "Exercises", "Resources"]:
                        sections.append(section_title)

        return sections

    def _extract_learning_objectives(self, blocks: List[Dict]) -> List[str]:
        """Extract learning objectives from page content."""
        objectives = []
        in_objectives_section = False

        for block in blocks:
            block_type = block.get("type", "")

            # Check if we're in Learning Objectives section
            if block_type == "heading_2":
                heading = block.get("heading_2", {}).get("rich_text", [])
                if heading and "Learning Objectives" in heading[0].get("plain_text", ""):
                    in_objectives_section = True
                    continue
                else:
                    in_objectives_section = False

            # Extract bullet points in objectives section
            if in_objectives_section and block_type == "bulleted_list_item":
                bullet_obj = block.get("bulleted_list_item", {})
                rich_text = bullet_obj.get("rich_text", [])
                if rich_text:
                    objective = rich_text[0].get("plain_text", "")
                    if objective:
                        objectives.append(objective)

        return objectives

    def _extract_tasks(self, blocks: List[Dict], title: str) -> List[Dict]:
        """Extract tasks/exercises from page content."""
        tasks = []

        # Check if this is a capstone page
        if "Capstone" in title:
            # Extract capstone task
            if "Python" in title:
                tasks.append({
                    "level": "capstone",
                    "id": "python-capstone",
                    "title": "Statistical Analysis Pipeline",
                    "expected_time": "90-120 minutes"
                })
            elif "C++" in title:
                tasks.append({
                    "level": "capstone",
                    "id": "cpp-capstone",
                    "title": "Gaussian Mixture Model Fitting Library",
                    "expected_time": "4-6 hours"
                })

        # Look for exercise sections
        # This would require more sophisticated parsing of exercise blocks
        # For now, we'll keep the existing tasks from the manifest

        return tasks

    def sync_manifest(self) -> Dict:
        """Main sync function: fetch from Notion and update manifest."""
        print("\n" + "="*60)
        print("Syncing from Notion (Live)...")
        print("="*60)

        # 1. Search for course pages
        print("\n1. Searching for course pages...")
        search_results = self.search_course_pages()

        # 2. Filter to relevant pages (Days 0-20, primers, foundational)
        print("\n2. Filtering course lesson pages...")
        lesson_pages = []
        for page in search_results:
            title_obj = page.get("properties", {}).get("title", {})
            title_content = title_obj.get("title", [])
            if title_content:
                title = title_content[0].get("plain_text", "")
                # Filter to lesson pages
                if any(pattern in title for pattern in [
                    "Day ", "Setup", "Algorithmic", "Primer"
                ]):
                    lesson_pages.append(page)
                    print(f"  ✓ {title}")

        print(f"\n  Found {len(lesson_pages)} lesson pages")

        # 3. Fetch detailed content for each page
        print("\n3. Fetching page content...")
        pages_data = []
        for i, page in enumerate(lesson_pages, 1):
            page_id = page["id"]
            title = page.get("properties", {}).get("title", {}).get("title", [{}])[0].get("plain_text", "")
            print(f"  [{i}/{len(lesson_pages)}] {title}...")

            try:
                content = self.get_page_content(page_id)
                metadata = self.extract_page_metadata(content)
                if metadata:
                    pages_data.append(metadata)
            except Exception as e:
                print(f"    ⚠ Error: {e}")

        print(f"\n  Successfully parsed {len(pages_data)} pages")

        # 4. Load existing manifest
        print("\n4. Loading existing manifest...")
        manifest = self._load_manifest()
        print(f"  Current pages: {len(manifest.get('pages', []))}")

        # 5. Merge with existing manifest
        print("\n5. Merging changes...")
        updated_count = self._merge_pages(manifest, pages_data)
        print(f"  Updated/added {updated_count} pages")

        # 6. Sort and save
        print("\n6. Sorting and saving...")
        manifest["pages"] = sorted(manifest["pages"], key=lambda x: x.get("order", 999))
        manifest["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        self._save_manifest(manifest)

        print("\n" + "="*60)
        print("Sync complete!")
        print("="*60)

        return manifest

    def _load_manifest(self) -> Dict:
        """Load existing manifest."""
        manifest_path = Path(__file__).parent / "course_manifest" / "manifest.json"
        with open(manifest_path, 'r') as f:
            return json.load(f)

    def _save_manifest(self, manifest: Dict):
        """Save updated manifest."""
        manifest_path = Path(__file__).parent / "course_manifest" / "manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        print(f"  ✓ Saved to {manifest_path}")

    def _normalize_notion_id(self, notion_id: str) -> str:
        """Normalize notion ID by removing dashes."""
        return notion_id.replace("-", "")

    def _merge_pages(self, manifest: Dict, new_pages: List[Dict]) -> int:
        """Merge new pages with existing manifest."""
        updated_count = 0

        # Create lookup by normalized notion_id
        existing_pages = {}
        for p in manifest.get("pages", []):
            normalized_id = self._normalize_notion_id(p.get("notion_id", ""))
            existing_pages[normalized_id] = p

        for new_page in new_pages:
            # Normalize both for comparison
            new_notion_id = new_page["notion_id"]
            normalized_new_id = self._normalize_notion_id(new_notion_id)

            if normalized_new_id in existing_pages:
                # Update existing page (keep tasks if not in new data)
                old_page = existing_pages[normalized_new_id]

                # Preserve tasks from old page if new page doesn't have them
                if not new_page.get("tasks"):
                    new_page["tasks"] = old_page.get("tasks", [])

                # Preserve the original notion_id format (with dashes if it had them)
                if "-" in old_page.get("notion_id", ""):
                    # Convert back to dashed format
                    new_page["notion_id"] = old_page["notion_id"]

                # Replace old page
                idx = manifest["pages"].index(old_page)
                manifest["pages"][idx] = new_page
                print(f"  ↻ Updated: {new_page['title']}")
            else:
                # Add new page
                manifest["pages"].append(new_page)
                print(f"  + Added: {new_page['title']}")

            updated_count += 1

        return updated_count


def main():
    """Run the sync."""
    syncer = NotionCourseSync(NOTION_TOKEN)
    syncer.sync_manifest()


if __name__ == "__main__":
    main()
