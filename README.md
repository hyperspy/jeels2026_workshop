# JEElS 2026 Workshop — exspy & HyperSpy

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hyperspy/jeels2026_workshop/HEAD)

Materials for the exspy workshop at the JEElS 2026 conference.

This repository contains notebooks for learning EELS analysis with
[HyperSpy](https://hyperspy.org/) and [exspy](https://github.com/userexternal/exspy).
Two formats are available: standard Jupyter notebooks (`.ipynb`) and
[Marimo](https://marimo.io/) notebooks (`.py`).

## Contents

| Notebook | Description |
|---|---|
| `1 - Getting Started/01_Getting_Started.*` | Introduction to HyperSpy signals, loading, axes, indexing, and ROIs |
| `2 - EELS/EELS_elemental_mapping.*` | Elemental mapping of Cu/Zn nanoparticles from EELS data |
| `2 - EELS/EELS_finestructure_analysis.*` | EELS fine structure analysis of LaSrMnO₃ thin films |
| `3 - Deconvolution/03_Deconvolution_introduction.*` | Introduction to the EELS deconvolution dataset |
| `binder/requirements.txt` | Pinned dependencies for the Binder environment |

## Launch on Binder

Click the badge above to launch this repository in a cloud-based Jupyter
environment with all dependencies pre-installed. No local setup required.

## Running with molab (cloud-hosted marimo)

The same notebooks are also available as [Marimo](https://marimo.io/) `.py` files.
You can run them directly in your browser on [molab](https://molab.marimo.io/),
a free cloud-hosted marimo notebook service — no local installation required.

Click the badges below to open any notebook:

| Notebook | Open in molab |
|---|---|
| Getting Started | [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/hyperspy/jeels2026_workshop/blob/main/notebooks/1%20-%20Getting%20Started/01_Getting_Started_unfilled.py) |
| EELS Elemental Mapping | [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/hyperspy/jeels2026_workshop/blob/main/notebooks/2%20-%20EELS/EELS_elemental_mapping.py) |
| EELS Fine Structure | [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/hyperspy/jeels2026_workshop/blob/main/notebooks/2%20-%20EELS/EELS_finestructure_analysis.py) |
| Deconvolution Introduction | [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/hyperspy/jeels2026_workshop/blob/main/notebooks/3%20-%20Deconvolution/03_Deconvolution_introduction.py) |

Marimo notebooks are reactive — cells automatically re-run when their inputs
change, and the UI provides a clean, app-like experience.

For a full list of Marimo features, see the [Marimo documentation](https://docs.marimo.io/).

## Local Setup

If you prefer to run locally:

```bash
python -m venv venv
source venv/bin/activate
pip install -r binder/requirements.txt
jupyter lab
```
