#!/usr/bin/env python3
"""Validate notebook code, Markdown structure, and LaTeX delimiters."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "spin_dynamics_workshop_tutorial.ipynb"
MARKDOWN_FILES = [ROOT / "README.md"]

LATEX_WORDS = re.compile(
    r"(?<!\\)\b("
    r"alpha|beta|gamma|partial|sum|frac|mathbf|mathrm|operatorname|"
    r"times|cdot|left|right|neq|leq|geq|lesssim|gtrsim|"
    r"langle|rangle|lVert|rVert|Delta|bmod|longrightarrow"
    r")\b"
)


def without_code(text: str) -> str:
    text = re.sub(r"\x60\x60\x60.*?\x60\x60\x60", "", text, flags=re.DOTALL)
    return re.sub(r"\x60[^\x60\n]*\x60", "", text)


def dollar_math_segments(text: str, label: str) -> list[tuple[str, str]]:
    """Return dollar-delimited math while checking delimiters and braces."""
    segments: list[tuple[str, str]] = []
    i = 0
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] != "$":
            i += 1
            continue

        delimiter = "$$" if text.startswith("$$", i) else "$"
        start = i
        i += len(delimiter)
        body_start = i
        brace_depth = 0

        while i < len(text):
            if text[i] == "\\":
                i += 2
                continue
            if text[i] == "{":
                brace_depth += 1
                i += 1
                continue
            if text[i] == "}":
                brace_depth -= 1
                assert brace_depth >= 0, f"{label}: unmatched closing brace near {start}"
                i += 1
                continue
            if text.startswith(delimiter, i):
                assert brace_depth == 0, f"{label}: unbalanced braces near {start}"
                segments.append((delimiter, text[body_start:i]))
                i += len(delimiter)
                break
            i += 1
        else:
            raise AssertionError(f"{label}: unclosed {delimiter} delimiter near {start}")

    return segments


def validate_markdown(text: str, label: str) -> None:
    controls = [
        (index, ord(char))
        for index, char in enumerate(text)
        if ord(char) < 32 and char != "\n"
    ]
    assert not controls, f"{label}: disallowed control characters {controls}"
    assert text.count("\x60\x60\x60") % 2 == 0, (
        f"{label}: unbalanced fenced-code markers"
    )

    prose = without_code(text)
    assert prose.count(r"\[") == prose.count(r"\]"), f"{label}: unbalanced display math"
    assert prose.count(r"\(") == prose.count(r"\)"), f"{label}: unbalanced inline math"

    display_segments = re.findall(r"\$\$(.*?)\$\$", prose, flags=re.DOTALL)
    multiline = [segment for segment in display_segments if "\n" in segment.strip()]
    assert not multiline, (
        f"{label}: display-math bodies must stay on one source line for "
        "Jupyter/GitHub/Pandoc compatibility"
    )

    for delimiter, segment in dollar_math_segments(prose, label):
        assert "\n" not in segment.strip(), (
            f"{label}: {delimiter} math body spans source lines"
        )
        malformed = sorted(set(LATEX_WORDS.findall(segment)))
        assert not malformed, (
            f"{label}: probable LaTeX commands missing backslashes: {malformed}"
        )


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    assert notebook["cells"], "Notebook contains no cells"

    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    markdown_cells = [
        cell for cell in notebook["cells"] if cell["cell_type"] == "markdown"
    ]
    assert code_cells, "Notebook contains no code cells"
    assert markdown_cells, "Notebook contains no Markdown cells"

    for index, cell in enumerate(code_cells):
        assert cell.get("execution_count") is None, f"Code cell {index} has an execution count"
        assert not cell.get("outputs"), f"Code cell {index} contains stored output"
        source = "".join(cell.get("source", []))
        ast.parse(source, filename=f"{NOTEBOOK.name}:code-cell-{index}")

    for index, cell in enumerate(markdown_cells):
        validate_markdown(
            "".join(cell.get("source", [])),
            f"{NOTEBOOK.name}:markdown-cell-{index}",
        )

    for path in MARKDOWN_FILES:
        validate_markdown(path.read_text(encoding="utf-8"), path.name)

    text = "\n".join(
        "".join(cell.get("source", [])) for cell in notebook["cells"]
    )
    required_markers = [
        "finite_difference_field",
        "prefactor = -gamma / (1.0 + alpha**2)",
        "cross(spins[j], Dij[i, j])",
        "cross(spins[j], Dvec)",
        r"\mathbf{H}^{\mathrm{eff}}_i",
        r"\frac{\gamma}{1+\alpha^2}",
    ]
    missing = [marker for marker in required_markers if marker not in text]
    assert not missing, f"Missing required markers: {missing}"

    print(
        f"Validated {NOTEBOOK.name}: {len(notebook['cells'])} cells, "
        f"{len(code_cells)} code cells, {len(markdown_cells)} Markdown cells"
    )
    print(f"Validated repository Markdown: {len(MARKDOWN_FILES)} files")


if __name__ == "__main__":
    main()
