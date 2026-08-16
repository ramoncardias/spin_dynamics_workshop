#!/usr/bin/env python3
"""Validate the workshop notebook without executing long simulations."""

from __future__ import annotations

import ast
import json
from pathlib import Path

NOTEBOOK = Path(__file__).resolve().parents[1] / "spin_dynamics_workshop_tutorial.ipynb"


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    assert notebook["cells"], "Notebook contains no cells"

    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    assert code_cells, "Notebook contains no code cells"

    for index, cell in enumerate(code_cells):
        assert cell.get("execution_count") is None, f"Code cell {index} has an execution count"
        assert not cell.get("outputs"), f"Code cell {index} contains stored output"
        source = "".join(cell.get("source", []))
        ast.parse(source, filename=f"{NOTEBOOK.name}:code-cell-{index}")

    text = NOTEBOOK.read_text(encoding="utf-8")
    required_markers = [
        "d862627cf274f83fe81b975b090e37d38cb5a924",
        "finite_difference_field",
        "prefactor = -gamma / (1.0 + alpha**2)",
        "cross(spins[j], Dij[i, j])",
        "cross(spins[j], Dvec)",
    ]
    missing = [marker for marker in required_markers if marker not in text]
    assert not missing, f"Missing required markers: {missing}"

    print(
        f"Validated {NOTEBOOK.name}: "
        f"{len(notebook['cells'])} cells, {len(code_cells)} code cells"
    )


if __name__ == "__main__":
    main()

