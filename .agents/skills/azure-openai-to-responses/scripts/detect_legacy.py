#!/usr/bin/env python3
"""Detect legacy Azure OpenAI Chat Completions patterns in a Python codebase.

Usage:
    python detect_legacy.py <directory>
    python detect_legacy.py .                  # current directory
    python detect_legacy.py src/ tests/        # multiple directories

Scans for legacy OpenAI Chat Completions API usage, deprecated Azure client
constructors, response shape access patterns, deprecated parameters, and
test infrastructure that needs updating for the Responses API migration.

Exit codes:
    0 — no legacy patterns found
    1 — legacy patterns found (migration needed)
"""

import argparse
import re
import sys
from pathlib import Path

# Legacy patterns grouped by category
# Each entry: (regex_pattern, description, category)
PATTERNS: list[tuple[str, str, str]] = [
    # Legacy API calls
    (r"chat\.completions\.create", "Chat Completions API call", "api-call"),
    (r"ChatCompletion\.create", "Legacy ChatCompletion.create", "api-call"),
    (r"Completion\.create", "Legacy Completion.create", "api-call"),
    # Deprecated Azure client constructors
    (r"AzureOpenAI\(", "Deprecated AzureOpenAI constructor", "client"),
    (r"AsyncAzureOpenAI\(", "Deprecated AsyncAzureOpenAI constructor", "client"),
    # Response shape access patterns
    (r"choices\[0\]\.message\.content", "Chat Completions response access", "response-shape"),
    (r"choices\[0\]\.delta\.content", "Chat Completions streaming access", "response-shape"),
    (r"choices\[0\]\.message\.function_call", "Legacy function_call access", "response-shape"),
    (r"choices\[0\]\.message\.tool_calls", "Legacy tool_calls access", "response-shape"),
    (r"choices\[0\]", "Generic choices[0] access", "response-shape"),
    # Deprecated parameters
    (r"\bmax_tokens\b", "Deprecated max_tokens (use max_output_tokens)", "parameter"),
    (r"\bmax_completion_tokens\b", "Azure o-series max_completion_tokens (use max_output_tokens)", "parameter"),
    (r"""['"]seed['"]""" , "Unsupported seed parameter", "parameter"),
    (r"\bresponse_format\b", "Legacy response_format (use text.format)", "parameter"),
    (r"\breasoning_effort\b", "O-series reasoning_effort (migrate to reasoning={'effort': ...})", "parameter"),
    (r"\btop_p\b", "top_p parameter (not supported on o-series models)", "parameter"),
    # Deprecated env vars
    (r"AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION", "Deprecated api_version env var", "env-var"),
    (r"AZURE_OPENAI_CLIENT_ID", "Should be AZURE_CLIENT_ID", "env-var"),
    # GitHub Models (not supported by Responses API — must remove)
    (r"models\.github\.ai|models\.inference\.ai\.azure", "GitHub Models endpoint (Responses API not supported — remove)", "github-models"),
    # Framework-level legacy patterns
    (r"OpenAIChatCompletionClient", "MAF OpenAIChatCompletionClient (uses Chat Completions; replace with OpenAIChatClient in 1.0.0+)", "framework"),
    # Test infrastructure
    (r"ChatCompletionChunk", "Legacy mock type in tests", "test"),
    (r"AsyncCompletions\.create", "Legacy mock patch path in tests", "test"),
    (r"_azure_ad_token_provider", "Legacy Azure AD assertion in tests", "test"),
    (r"prompt_filter_results", "Azure-specific filter mock in tests", "test"),
    (r"content_filter_results", "Azure-specific filter mock in tests", "test"),
]

SKIP_DIRS = {
    ".git", ".venv", "venv", "__pycache__", "node_modules",
    ".tox", ".mypy_cache", ".pytest_cache", "dist", "build",
    ".github",  # don't scan the agent definition
    "skills",   # don't scan the skill itself
}

# Files that reference legacy patterns intentionally (docs, tooling)
SKIP_FILES = {
    "README.md",
    "migrate.py",
    "find_legacy_openai_repos.py",
    "detect_legacy.py",
    "bulk_migrate.py",
}

EXTENSIONS = {".py", ".env", ".toml", ".cfg", ".ini", ".txt", ".md", ".yml", ".yaml", ".bicep", ".json"}


def scan_file(path: Path) -> list[tuple[int, str, str, str]]:
    """Scan a single file for legacy patterns. Returns list of (line_no, line, description, category)."""
    hits: list[tuple[int, str, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return hits

    for line_no, line in enumerate(text.splitlines(), start=1):
        for pattern, description, category in PATTERNS:
            if re.search(pattern, line):
                hits.append((line_no, line.strip(), description, category))
    return hits


def scan_directory(root: Path) -> dict[str, list[tuple[int, str, str, str]]]:
    """Walk a directory tree and return {filepath: [(line, text, desc, cat), ...]}."""
    results: dict[str, list[tuple[int, str, str, str]]] = {}
    for path in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        if path.is_file() and path.suffix in EXTENSIONS:
            hits = scan_file(path)
            if hits:
                results[str(path)] = hits
    return results


def print_report(all_results: dict[str, list[tuple[int, str, str, str]]]) -> int:
    """Print a grouped report and return total hit count."""
    total = 0
    categories: dict[str, list[tuple[str, int, str, str]]] = {}

    for filepath, hits in all_results.items():
        for line_no, line_text, description, category in hits:
            categories.setdefault(category, []).append((filepath, line_no, line_text, description))
            total += 1

    if total == 0:
        print("[PASS] No legacy Chat Completions patterns found.")
        return 0

    category_labels = {
        "api-call": "Legacy API Calls (must rewrite)",
        "client": "Deprecated Azure Client Constructors (must replace)",
        "response-shape": "Response Shape Access (must update)",
        "parameter": "Deprecated Parameters (must remove/rename)",
        "env-var": "Deprecated Environment Variables (must clean up)",
        "test": "Test Infrastructure (must update)",
    }

    print(f"[SCAN] Found {total} legacy pattern(s) across {len(all_results)} file(s):\n")

    for cat_key in ["api-call", "client", "response-shape", "parameter", "env-var", "test"]:
        items = categories.get(cat_key, [])
        if not items:
            continue
        print(f"## {category_labels[cat_key]} ({len(items)} hit(s))\n")
        for filepath, line_no, line_text, description in items:
            print(f"  {filepath}:{line_no}")
            print(f"    {description}")
            print(f"    > {line_text[:120]}")
            print()

    print(f"---\nTotal: {total} legacy pattern(s) in {len(all_results)} file(s).")
    print("Run the migration skill to fix these.")
    return total


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Detect legacy Azure OpenAI Chat Completions patterns."
    )
    parser.add_argument(
        "directories",
        nargs="+",
        help="Directories to scan",
    )
    args = parser.parse_args()

    all_results: dict[str, list[tuple[int, str, str, str]]] = {}
    for d in args.directories:
        root = Path(d)
        if not root.is_dir():
            print(f"Warning: {d} is not a directory, skipping.", file=sys.stderr)
            continue
        all_results.update(scan_directory(root))

    total = print_report(all_results)
    sys.exit(1 if total > 0 else 0)


if __name__ == "__main__":
    main()
