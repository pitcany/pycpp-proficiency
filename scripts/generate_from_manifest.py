#!/usr/bin/env python3
"""
Generate lesson structure from manifest.json.

This script reads the course manifest and generates/updates the lesson
directory structure including README.md and exercises.md files.

Usage:
    python scripts/generate_from_manifest.py [--force]

Options:
    --force     Overwrite existing files (default: skip existing)
"""

import argparse
import json
from pathlib import Path

MANIFEST_PATH = Path("course_manifest/manifest.json")
LESSONS_DIR = Path("lessons")


def load_manifest() -> dict:
    """Load the course manifest."""
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Manifest not found: {MANIFEST_PATH}")
    with open(MANIFEST_PATH) as f:
        return json.load(f)


def get_lesson_path(page: dict) -> Path:
    """Determine the lesson directory path for a page."""
    week = page.get("week", "foundations")
    page_id = page["id"]

    if week == "foundations":
        return LESSONS_DIR / "foundations" / page_id
    elif week == "week1":
        return LESSONS_DIR / "week1" / page_id
    elif week == "week2":
        return LESSONS_DIR / "week2" / page_id
    elif week == "week3":
        return LESSONS_DIR / "week3" / page_id
    else:
        return LESSONS_DIR / "other" / page_id


def generate_readme(page: dict) -> str:
    """Generate README content for a lesson."""
    lines = [
        f"# {page['title']}",
        "",
        f"**Language**: {page.get('language', 'mixed').title()}",
    ]

    if page.get("notion_url"):
        lines.append(f"**Notion Source**: [Link]({page['notion_url']})")

    lines.append("")
    lines.append("## Learning Objectives")
    lines.append("")

    for obj in page.get("learning_objectives", []):
        lines.append(f"- [ ] {obj}")

    lines.append("")
    lines.append("## Sections")
    lines.append("")

    for section in page.get("sections", []):
        lines.append(f"- {section}")

    if page.get("tasks"):
        lines.append("")
        lines.append("## Exercises")
        lines.append("")
        lines.append("See [exercises.md](exercises.md) for practice problems.")

    return "\n".join(lines) + "\n"


def generate_exercises(page: dict) -> str:
    """Generate exercises.md content for a lesson."""
    lines = [
        f"# {page['title']} - Exercises",
        "",
    ]

    tasks = page.get("tasks", [])
    if not tasks:
        lines.append("No exercises defined for this lesson.")
        return "\n".join(lines) + "\n"

    # Group by level
    by_level = {}
    for task in tasks:
        level = task.get("level", "foundational")
        by_level.setdefault(level, []).append(task)

    for level in ["foundational", "proficiency", "mastery", "capstone"]:
        level_tasks = by_level.get(level, [])
        if level_tasks:
            lines.append(f"## {level.title()} Exercises")
            lines.append("")

            for task in level_tasks:
                task_id = task.get("id", "")
                title = task.get("title", "Untitled")
                time = task.get("expected_time", "")

                if task_id:
                    lines.append(f"### Exercise {task_id}: {title}")
                else:
                    lines.append(f"### {title}")

                if time:
                    lines.append(f"**Time**: {time}")

                lines.append("")
                lines.append("TODO: Add exercise description")
                lines.append("")

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate lesson structure from manifest")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    print("=== Generate from Manifest ===")
    print()

    manifest = load_manifest()
    print(f"Course: {manifest['course_title']}")
    print(f"Pages: {len(manifest['pages'])}")
    print()

    created = 0
    skipped = 0

    for page in manifest["pages"]:
        lesson_dir = get_lesson_path(page)
        readme_path = lesson_dir / "README.md"
        exercises_path = lesson_dir / "exercises.md"

        # Create directories
        lesson_dir.mkdir(parents=True, exist_ok=True)
        (lesson_dir / "python").mkdir(exist_ok=True)
        (lesson_dir / "cpp").mkdir(exist_ok=True)

        # Generate README
        if not readme_path.exists() or args.force:
            readme_path.write_text(generate_readme(page))
            print(f"Created: {readme_path}")
            created += 1
        else:
            skipped += 1

        # Generate exercises
        if page.get("tasks"):
            if not exercises_path.exists() or args.force:
                exercises_path.write_text(generate_exercises(page))
                print(f"Created: {exercises_path}")
                created += 1
            else:
                skipped += 1

    print()
    print(f"Created: {created} files")
    print(f"Skipped: {skipped} files (already exist)")


if __name__ == "__main__":
    main()
