# Spin Dynamics Workshop

[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ramoncardias/spin_dynamics_workshop/73e8ff8cd03c217f360c9c01405ef957b790b7db?urlpath=lab/tree/spin_dynamics_workshop_tutorial.ipynb)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ramoncardias/spin_dynamics_workshop/blob/73e8ff8cd03c217f360c9c01405ef957b790b7db/spin_dynamics_workshop_tutorial.ipynb)

## About

This is a hands-on introduction to **atomistic spin dynamics** in Python. The workshop
builds a minimal simulation code from small, readable routines so that each connection
between the magnetic Hamiltonian, the effective field, and the spin trajectory remains
visible.

The material is intended for students and researchers who want to understand how a
spin-dynamics calculation works before moving to larger simulation packages. Everything
needed for the workshop is contained in a single Jupyter notebook.

## Scientific notes

The model uses classical unit spins with exchange, Dzyaloshinskii–Moriya, and Zeeman
interactions:

$$
E=-\sum_{i<j}J_{ij}\,\mathbf{S}_i\cdot\mathbf{S}_j-\sum_{i<j}\mathbf{D}_{ij}\cdot\left(\mathbf{S}_i\times\mathbf{S}_j\right)-\sum_i\mathbf{B}\cdot\mathbf{S}_i.
$$

The effective field is obtained directly from the energy,

$$
\mathbf{H}^{\mathrm{eff}}_i=-\frac{\partial E}{\partial\mathbf{S}_i},
$$

and the spin trajectories are propagated with the Gilbert form of the
Landau–Lifshitz–Gilbert equation using a Heun predictor–corrector integrator. A numerical
finite-difference test checks the analytical effective field, while spin normalization
is monitored throughout the dynamics.

The parameters are expressed in dimensionless code units unless stated otherwise. The
examples emphasize physical interpretation and transparent implementation rather than
large-scale numerical performance.

## Examples

1. **Periodic nanochain** — introduces the input format, exchange and DMI interactions,
   effective fields, energy evaluation, LLG integration, and basic spin visualization.

2. **Square-lattice skyrmion** — explores how interfacial DMI and a perpendicular
   magnetic field influence a seeded skyrmion under periodic boundary conditions.

3. **Kagomé antiferromagnet** — illustrates frustration, chiral DMI, and relaxation
   toward a non-collinear three-sublattice state with approximately $120^\circ$
   nearest-neighbor angles.

Each example reuses the routines introduced earlier, allowing the notebook to progress
naturally from a small one-dimensional model to two-dimensional non-collinear textures.

## Installation

### Run online

Use the **Binder** or **Open in Colab** badge at the top of this page. Binder may take a
few minutes on the first launch while it builds the environment.

### Run locally

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

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

The notebook generates its own lattice and interaction files, so no external dataset,
DFT code, or dedicated spin-dynamics package is required.

