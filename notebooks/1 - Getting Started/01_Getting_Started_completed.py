# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "hyperspy-gui-anywidget @ git+https://github.com/hyperspy/hyperspy_gui_anywidget",
#     "hyperspy",
#     "marimo>=0.23.8",
# ]
#
# [tool.uv.sources]
# hyperspy = { git = "https://github.com/francisco-dlp/hyperspy.git", branch = "FIX_mac_shortcuts" }
#
# [tool.uv]
# override-dependencies = ["hyperspy>=2.4.1.dev0"]
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Getting started with HyperSpy

        **Objective:** By the end of this notebook you should be able to import
        HyperSpy, load and visualise data, inspect axes, index signals, and use
        regions of interest — all of which you will need for the EELS tutorial.

        This notebook was adapted from the original HyperSpy workshop material.
        It has been trimmed to the essential concepts required for the EELS
        practicals later in this workshop.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 1. Importing HyperSpy""")
    return


@app.cell
def _():
    import marimo as mo

    import hyperspy.api as hs
    import hyperspy_gui_anywidget  # noqa: F401
    import numpy as np

    hs.preferences.GUIs.enable_traitsui_gui = False
    hs.preferences.GUIs.enable_anywidget_gui = True
    hs.preferences.GUIs.enable_ipywidgets_gui = False
    return hs, mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 2. What is a HyperSpy signal?

        A HyperSpy **signal** is a data container that pairs a multi-dimensional
        array with calibration information. The array dimensions are split into
        two groups:
        - **Navigation axes** — dimensions we iterate over (e.g. x, y scan positions).
        - **Signal axes** — the data dimension(s) recorded at each navigation position
          (e.g. energy loss, diffraction pattern).

        Let us create a simple 1-D signal to see this in action.
        """
    )
    return


@app.cell
def _(hs, np):
    s_demo = hs.signals.Signal1D(np.arange(10))
    s_demo
    return (s_demo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 3. Loading data from a file""")
    return


@app.cell
def _(hs):
    s = hs.load("../2 - EELS/datasets/CuZn_EELS_mapping_tutorial.hspy")
    s
    return (s,)


@app.cell
def _(s):
    s.metadata
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 4. Axis properties""")
    return


@app.cell
def _(s):
    s.axes_manager
    return


@app.cell
def _(s):
    s.axes_manager["Energy loss"].scale
    return


@app.cell
def _(s):
    s.axes_manager["Energy loss"].units
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 5. Visualisation""")
    return


@app.cell
def _(s):
    s.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 6. Indexing""")
    return


@app.cell
def _(s):
    s.inav[25, 12].plot()
    return


@app.cell
def _(s):
    s.isig[930.:1005.].plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""`inav` and `isig` can be chained:""")
    return


@app.cell
def _(s):
    s.inav[25, 12].isig[930.:1005.].plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 7. Regions of interest (ROIs)""")
    return


@app.cell
def _(hs, s):
    import matplotlib.pyplot as plt

    roi_cu = hs.roi.SpanROI(left=930, right=1005)

    s_cu = roi_cu(s, axes=s.axes_manager.signal_axes)
    s_cu
    return plt, roi_cu, s_cu


@app.cell
def _(hs, plt, roi_cu, s):
    roi_zn = hs.roi.SpanROI(left=1045, right=1145)
    hs.plot.plot_roi_map(s, [roi_cu, roi_zn])
    return (roi_zn,)


@app.cell
def _(plt):
    plt.close("all")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        **You are now ready for the EELS tutorial!**

        Open **`EELS_elemental_mapping.ipynb`** in the `2 - EELS` folder to begin.
        """
    )
    return


if __name__ == "__main__":
    app.run()
