# JEElS 2026 Workshop — exspy & HyperSpy

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/francisco-dlp/jeels2026_workshop/HEAD)

Materials for the exspy workshop at the JEElS 2026 conference.

This repository contains an introductory notebook to get you started with
[HyperSpy](https://hyperspy.org/) and [exspy](https://github.com/userexternal/exspy)
for multi-dimensional electron microscopy data analysis.

## Contents

- `examples/introductory_example.ipynb` — a first look at multi-dimensional
  `Signal2D` data with HyperSpy and exspy
- `binder/requirements.txt` — pinned dependencies for the Binder environment

## Launch on Binder

Click the badge above to launch this repository in a cloud-based Jupyter
environment with all dependencies pre-installed. No local setup required.

## Local Setup

If you prefer to run locally:

```bash
python -m venv venv
source venv/bin/activate
pip install -r binder/requirements.txt
jupyter lab
```
