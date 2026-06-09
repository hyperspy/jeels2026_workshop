# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "hyperspy-gui-anywidget @ git+https://github.com/hyperspy/hyperspy_gui_anywidget",
#     "hyperspy",
#     "marimo>=0.23.8",
# ]
#
# [tool.uv.sources]
# hyperspy = { git = "https://github.com/hyperspy/hyperspy.git", branch = "JEELS2026" }
#
# [tool.uv]
# override-dependencies = ["hyperspy>=2.4.1.dev0"]
# ///

import marimo

__generated_with = "0.23.8"
app = marimo.App(
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Introduction to EELS deconvolution

        This notebook introduces the data used in the deconvolution practical.
        Six datasets are provided:

        - **measured.hspy** — The experimentally measured core-loss EELS spectrum.
        - **ll_for_fr.hspy** — The low-loss spectrum, used by the Fourier-ratio deconvolution.
        - **zlp.hspy** — The zero-loss peak, extracted from the low-loss.
        - **cl_k_edge.hspy** — The chlorine K-edge cross section.
        - **cl_l_edge.hspy** — The chlorine L-edge cross section.
        - **ssd_ground_truth.hspy** — The "ground truth" single-scattering distribution.

        We will load each file and inspect its properties.
        """
    )
    return


@app.cell
def _():
    import marimo as mo

    import hyperspy.api as hs
    import hyperspy_gui_anywidget  # noqa: F401
    import numpy as np
    import matplotlib.pyplot as plt

    hs.preferences.GUIs.enable_traitsui_gui = False
    hs.preferences.GUIs.enable_anywidget_gui = True
    hs.preferences.GUIs.enable_ipywidgets_gui = False
    return hs, mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    import os
    import urllib.request

    data_dir = "."
    files = [
        "measured.hspy",
        "ll_for_fr.hspy",
        "zlp.hspy",
        "cl_k_edge.hspy",
        "cl_l_edge.hspy",
        "ssd_ground_truth.hspy",
    ]
    base_url = (
        "https://raw.githubusercontent.com/hyperspy/jeels2026_workshop/main"
        "/notebooks/3%20-%20Deconvolution/"
    )
    for fname in files:
        path = os.path.join(data_dir, fname)
        if not os.path.exists(path):
            url = base_url + fname
            urllib.request.urlretrieve(url, path)
            print(f"Downloaded {fname}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `measured.hspy` — The core-loss spectrum""")
    return


@app.cell
def _(hs):
    s_measured = hs.load("measured.hspy")
    s_measured
    return (s_measured,)


@app.cell
def _(s_measured):
    s_measured.axes_manager
    return


@app.cell
def _(s_measured):
    s_measured.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `ll_for_fr.hspy` — The low-loss spectrum""")
    return


@app.cell
def _(hs):
    s_ll = hs.load("ll_for_fr.hspy")
    s_ll
    return (s_ll,)


@app.cell
def _(s_ll):
    s_ll.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `zlp.hspy` — The zero-loss peak""")
    return


@app.cell
def _(hs):
    s_zlp = hs.load("zlp.hspy")
    s_zlp
    return (s_zlp,)


@app.cell
def _(s_zlp):
    s_zlp.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `cl_k_edge.hspy` — The Cl K-edge cross section""")
    return


@app.cell
def _(hs):
    s_cl_k = hs.load("cl_k_edge.hspy")
    s_cl_k
    return (s_cl_k,)


@app.cell
def _(s_cl_k):
    s_cl_k.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `cl_l_edge.hspy` — The Cl L-edge cross section""")
    return


@app.cell
def _(hs):
    s_cl_l = hs.load("cl_l_edge.hspy")
    s_cl_l
    return (s_cl_l,)


@app.cell
def _(s_cl_l):
    s_cl_l.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `ssd_ground_truth.hspy` — The ground-truth single-scattering distribution""")
    return


@app.cell
def _(hs):
    s_ssd = hs.load("ssd_ground_truth.hspy")
    s_ssd
    return (s_ssd,)


@app.cell
def _(s_ssd):
    s_ssd.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        All six datasets are now loaded. You can use the interactive navigator
        in each `plot()` to explore the signals.
        """
    )
    return


if __name__ == "__main__":
    app.run()
