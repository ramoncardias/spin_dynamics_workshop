# Spin Dynamics Workshop

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Notebook validation](https://github.com/ramoncardias/spin_dynamics_workshop/actions/workflows/validate-notebook.yml/badge.svg)](https://github.com/ramoncardias/spin_dynamics_workshop/actions/workflows/validate-notebook.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ramoncardias/spin_dynamics_workshop/main?labpath=spin_dynamics_workshop_tutorial.ipynb)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ramoncardias/spin_dynamics_workshop/blob/main/spin_dynamics_workshop_tutorial.ipynb)

A self-contained, hands-on workshop in atomistic spin dynamics. Participants build a
minimal Python implementation from small, testable routines and use it to study three
systems:

1. a periodic ferromagnetic nanochain;
2. a square-lattice skyrmion with interfacial DMI and a Zeeman field;
3. a frustrated Kagomé antiferromagnet with chiral $120^\circ$ order.

## Physics covered

The notebook implements classical unit spins with exchange, Dzyaloshinskii–Moriya,
and Zeeman interactions,

$$
E = -\sum_{i<j}J_{ij}\,\mathbf{S}_i\cdot\mathbf{S}_j -\sum_{i<j}\mathbf{D}_{ij}\cdot \left(\mathbf{S}_i\times\mathbf{S}_j\right) -\sum_i\mathbf{B}\cdot\mathbf{S}_i.
$$

It then integrates the Gilbert form of the LLG equation with a Heun
predictor–corrector scheme. A finite-difference test verifies

$$
\mathbf{H}^{\mathrm{eff}}_i = -\frac{\partial E}{\partial\mathbf{S}_i}.
$$

## Run locally

Python 3.10 or newer is recommended.

```bash
git clone https://github.com/ramoncardias/spin_dynamics_workshop.git
cd spin_dynamics_workshop
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab spin_dynamics_workshop_tutorial.ipynb
```

On Windows PowerShell, activate the environment with
`.venv\Scripts\Activate.ps1`.

The notebook generates all of its own interaction and lattice files. No DFT code,
UppASD installation, or external dataset is required.

## Repository contents

- `spin_dynamics_workshop_tutorial.ipynb`: complete workshop
- `requirements.txt` and `runtime.txt`: reproducible Python environment
- `scripts/validate_notebook.py`: structural, Markdown, LaTeX, and Python checks
- `SOURCE.md`: source commit, attribution, and modification record
- `CHANGELOG.md`: user-facing changes
- `CITATION.cff`: citation metadata
- `LICENSE`: GNU GPL version 3

## Provenance and license

This standalone edition derives from
[`coteo-cbpf/dft_sd_workshop`](https://github.com/coteo-cbpf/dft_sd_workshop),
specifically `notebook-sd/spin_dynamics_workshop_tutorial.ipynb` at commit
[`d862627`](https://github.com/coteo-cbpf/dft_sd_workshop/commit/d862627cf274f83fe81b975b090e37d38cb5a924).
The original notebook and this adaptation are by Ramon Cardias. The original file was
first imported unchanged in this repository so that subsequent modifications remain
visible in Git history. See [SOURCE.md](SOURCE.md) for exact hashes.

Distributed under the [GNU General Public License v3.0](LICENSE).


