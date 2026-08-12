from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def slugify(text: str) -> str:
    lowered = text.strip().lower()
    cleaned = re.sub(r"[^a-z0-9]+", "-", lowered)
    collapsed = re.sub(r"-+", "-", cleaned).strip("-")
    return collapsed or "notebook"


def find_repo_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    return start


def load_template(skill_dir: Path, kind: str) -> dict[str, Any]:
    asset_name = "experiment-template.ipynb" if kind == "experiment" else "tutorial-template.ipynb"
    template_path = skill_dir / "assets" / asset_name
    if not template_path.exists():
        raise SystemExit(f"Missing template: {template_path}")
    with template_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit(f"Unexpected template shape: {template_path}")
    return data


def update_title(notebook: dict[str, Any], kind: str, title: str) -> None:
    prefix = "Experiment" if kind == "experiment" else "Tutorial"
    expected = f"# {prefix}: {title}\n"

    cells = notebook.get("cells")
    if not isinstance(cells, list) or not cells:
        raise SystemExit("Template notebook has no cells")

    first_cell = cells[0]
    if not isinstance(first_cell, dict) or first_cell.get("cell_type") != "markdown":
        raise SystemExit("Template notebook must start with a markdown title cell")

    source = first_cell.get("source", [])
    if isinstance(source, str):
        source_lines = [source]
    elif isinstance(source, list):
        source_lines = [str(line) for line in source]
    else:
        source_lines = []

    if source_lines:
        source_lines[0] = expected
    else:
        source_lines = [expected]

    first_cell["source"] = source_lines

    metadata = notebook.setdefault("metadata", {})
    if not isinstance(metadata, dict):
        raise SystemExit("Notebook metadata must be a mapping")

    language_info = metadata.setdefault("language_info", {})
    if isinstance(language_info, dict):
        language_info.setdefault("name", "python")
        language_info.setdefault("version", "3.12")


def default_output(repo_root: Path, title: str) -> Path:
    filename = f"{slugify(title)}.ipynb"
    return repo_root / "output" / "jupyter-notebook" / filename


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold a Jupyter notebook for experiments or tutorials.")
    parser.add_argument(
        "--kind",
        choices=["experiment", "tutorial"],
        default="experiment",
        help="Notebook style to scaffold (default: experiment).",
    )
    parser.add_argument(
        "--title",
        required=True,
        help="Human-readable notebook title used in the first markdown cell.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path for the notebook. Defaults to output/jupyter-notebook/<slug>.ipynb.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    script_path = Path(__file__).resolve()
    skill_dir = script_path.parents[1]
    repo_root = find_repo_root(skill_dir)

    notebook = load_template(skill_dir, args.kind)
    update_title(notebook, args.kind, args.title)

    out_path = args.out or default_output(repo_root, args.title)
    out_path = out_path.resolve()

    if out_path.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {out_path}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2)
        f.write("\n")

    print(f"Wrote {out_path} using kind={args.kind}.")


if __name__ == "__main__":
    main()
