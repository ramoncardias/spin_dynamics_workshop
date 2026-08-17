# Source and provenance

This repository is derived from the spin-dynamics component of
[`coteo-cbpf/dft_sd_workshop`](https://github.com/coteo-cbpf/dft_sd_workshop).

## Imported source

- Source file: `notebook-sd/spin_dynamics_workshop_tutorial.ipynb`
- Source repository commit: [`d862627cf274f83fe81b975b090e37d38cb5a924`](https://github.com/coteo-cbpf/dft_sd_workshop/commit/d862627cf274f83fe81b975b090e37d38cb5a924)
- Source notebook blob: `2e25d3d65ab8af63f3dd6fff4834a969862fd13f`
- Original author recorded by GitHub: Ramon Cardias
- Import date: 2026-08-16
- Exact import commit in this repository: [`4f76597a18145d486cba9a0703cf98789d2f3f5c`](https://github.com/ramoncardias/spin_dynamics_workshop/commit/4f76597a18145d486cba9a0703cf98789d2f3f5c)

The import commit preserves the notebook byte-for-byte. The following commit turns it
into a standalone workshop, so every textual and scientific change remains reviewable
as a normal Git diff.

## Changes in the standalone edition

- removed references and dependencies unrelated to spin dynamics;
- moved the workshop notebook to the repository root;
- documented local, Binder, and Colab launch paths;
- retained only the packages imported by the workshop;
- cleared stored outputs and execution counts for reproducibility;
- corrected the DMI contribution to the effective field so it is consistent with
  $\mathbf{H}^{\mathrm{eff}}_i=-\partial E/\partial\mathbf{S}_i$;
- added a finite-difference energy-gradient test;
- wrote the Gilbert prefactor $1/(1+\alpha^2)$ explicitly in the LLG torque;
- increased the introductory relaxation from one step to a short visible trajectory;
- normalized Markdown math delimiters and added recursive formatting validation.

## License

The source repository is licensed under the GNU General Public License version 3.
This derivative repository retains GPL-3.0 and includes the complete license in
`LICENSE`. Modified-source notices and dates are recorded above and in the notebook.

