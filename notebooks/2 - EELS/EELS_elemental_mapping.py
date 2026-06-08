# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "exspy",
#     "hyperspy-gui-anywidget @ git+https://github.com/hyperspy/hyperspy_gui_anywidget",
#     "marimo>=0.23.8",
#     "matplotlib",
#     "numpy",
# ]
#
# [tool.uv.sources]
# hyperspy = { git = "https://github.com/francisco-dlp/hyperspy.git", branch = "FIX_mac_shortcuts" }
#
# [tool.uv]
# # The git branch builds as a pre-release (2.4.1.dev60+g...) which uv
# # excludes by default when evaluating hyperspy-gui-anywidget's >=2.3.0
# # constraint. This override lets the dev version satisfy it.
# override-dependencies = ["hyperspy>=2.4.1.dev0"]
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting elemental maps from EELS data using eXSpy

    In this tutorial, elemental maps of copper and zinc will be created from electron energy loss spectra (EELS). The data is recorded using a sample of copper and zinc oxide deposited on carbon nanotubes. The particles are likely to be very small, and the carbon is not completely covered. In this sample, the ratio of Zn and Cu is 3:1, and approximately 80 wt% of the sample is carbon. Due to the small amount of copper and zinc, the signal strength is low. To improve the signal strength without lowering the spatial resolution, the spectra were recorded with a high energy dispersion, resulting in low energy resolution. This means that any fine structure is not visible.

    In core loss EELS data such as this, we typically have two major types of features: the plasmon background and the core loss edges. The core loss edges originates from specific elements, and can be used to estimate the amount of that element. The plasmon background originates from collective electron motions in the material, and needs to be removed before the element amount can be estimated. This background removal is typically done by fitting a power law to the region before the core loss edge.

    However, if an EEL spectrum has two or more core loss edges, the intensity from the core loss edge situated at a lower energy must be accounted for somehow if we want to get the intensity from the edge at higher energy.

    In many cases, this can be done by fitting a power law to the region in front of the high energy core loss edge. However, if the two core loss edges are too close to each other, we need to use another approach.

    In this dataset, the Cu (around 930 eV) and Zn edges (around 1040 eV), are too close to estimate the background for the Zn edge. A solution to this problem is to fit the background and edges as shown in this notebook: the model based approach.

    For more information about the material system and how the results of this processing can be used, see the paper: https://doi.org/10.1016/j.cattod.2019.02.045

    This notebook requires `HyperSpy` 2.0 or higher. It also requires `eXSpy` which is a library which contains all of HyperSpy's EELS and EDX functionality.

    The main objective is to show how the functionalities of `HyperSpy` and `eXSpy` can be used to create relative elemental maps from EEL spectra.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Changes

    * 2017/09/27: Initial version by Ida Hjorth
    * 2019/11/14: Update to HyperSpy 1.5, and minor improvements to text by Magnus Nord
    * 2024/3/16: Update to work with HyperSpy 2.0, by Magnus Nord
    * 2025/06/02: Adapted for the ePSIC HyperSpy workshop
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Table of contents

    1. Load data
    2. Fitting Cu and Zn core-loss edges
    3. Display and export elemental maps
    4. Saving and restoring the model
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 1. Load data
    """)
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


@app.cell
def _():
    # Load the "datasets/CuZn_EELS_mapping_tutorial.hspy"
    s = None  # TODO: Use hs.load("datasets/CuZn_EELS_mapping_tutorial.hspy")
    return s,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Visualise the data using `plot()`, and navigate to a region where both edges are visible. For example position `(32, 14)`. Move the navigator in the `EELS Spectrum Image Navigator` either by:

    - left-click and drag the red "box" in the `EELS Spectrum Image Navigator`
    - select the `EELS Spectrum Image Navigator` window/figure and use the `Ctrl` + `Arrow` keys on your keyboard,
    - or hold the `Shift` key on your keyboard and left click on the location you want to navigate to.

    To compare two spectra from different positions, select either one of the figures and press the `E` key on your keyboard. This will add an extra blue navigator "box", which is moved by left-click + dragging it.
    """)
    return


@app.cell
def _(s):
    # Plot the signal using the `plot` method
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, lets try to visualize the intensity from both of the core loss edges, without having removed the plasmon background.

    We do this using by using [`hs.plot.plot_roi_map`](https://hyperspy.org/hyperspy-doc/current/reference/api.plot/index.html#hyperspy.api.plot.plot_roi_map) - _roi_ stand for _region of interest_. Move and resize the red and green spans by click-and-dragging with your mouse. The red span should be from about 930 to 1005 eV, and the green from 1045 to 1145 eV.

    You should be able to see some small changes, but due to the large contribution from the plasmon background it is difficult.
    """)
    return


@app.cell
def _(hs, s):
    # Use `plot_roi_map` with 2 rois
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To improve this, we remove the plasmon background by fitting a power law background to the region in front of the Cu core loss edge. From 700 to 900 eV.
    """)
    return


@app.cell
def _(s):
    # Use the `remove_background` method with signal_range (700, 900)
    s_background_removed = None  # TODO: Use s.remove_background(signal_range=(700., 900.), fast=False)
    return s_background_removed,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We do the same visualization as earlier using [`hs.plot.plot_roi_map`](https://hyperspy.org/hyperspy-doc/current/reference/api.plot/index.html#hyperspy.api.plot.plot_roi_map), however, this time we will define the ROI, a [`SpanROI`](https://hyperspy.org/hyperspy-doc/current/reference/api.roi.html#hyperspy.api.roi.SpanROI) for 1 dimension, and then pass these ROIs as a list:
    """)
    return


@app.cell
def _(hs):
    # Create the two `SpanROI` for energy range (930, 1005) and (1045, 1145)
    Cu_roi = None  # TODO: Use hs.roi.SpanROI(930, 1005)
    Zn_roi = None  # TODO: Use hs.roi.SpanROI(1045, 1145)
    return Cu_roi, Zn_roi


@app.cell
def _(Cu_roi, Zn_roi, hs, s_background_removed):
    # use `plot_roi_map` and pass the two predefined rois
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, the intensity from the plasmons is greatly reduced, with the Cu and Zn edges being much more visible. However, wherever there is Cu (red), there is also Zn (green). So currently, we can't be sure if the Cu core loss edge contributes to the apparent amount of Zn (due to the edges overlapping), or if it is due Cu and Zn being in the same regions.

    To properly resolve this, we need to use the model based approach, by fitting a component to all the features: the plasmon background, the Cu core loss edge and the Zn core loss edge.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 2. Fitting Cu and Zn core-loss edges
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the model-based approach, the low-loss signal can be convolved with the high-loss signal such that the energy spread of the electron beam and plural scattering due to the bulk plasmon are taken into account. This will lead to a better fit of the model to the experimental data. In addition, the experimental zero loss peak can be used to precisely calibrate the energy scale.

    In this example the low-loss signal was not recorded. However, since the sample is fairly thin, the effect of plural scattering is negligible.

    ------

    **Note**: this will download a set of open source **Generalised Oscillator Strengths (GOS)** , which was computed and packaged by Leonhard Segger, Giulio Guzzinati and Helmut Kohl. For more information about the GOS files, see the [Zenodo deposit](https://zenodo.org/doi/10.5281/zenodo.6599070). For more information about how these were computed, and the code used to compute them, see https://github.com/Br0Fi/goscalc. The GOS will be used to calculate the double differential cross-section and quantify the elemental distribution.

    To do EELS model fitting, several metadata are necessary:
    - elements in the specimens
    - beam energy, convergence and collection angle

    The information are stored in the [`metadata`](https://hyperspy.org/exspy/user_guide/metadata_structure.html) and the following methods are can be used these metadata:
    - [`add_elements`](https://hyperspy.org/exspy/reference/signals.html#exspy.signals.EELSSpectrum.add_elements)
    - [`set_microscope_parameters`](https://hyperspy.org/exspy/reference/signals.html#exspy.signals.EELSSpectrum.set_microscope_parameters)

    These metadata may be already present in the signal depending on the data provenance.
    """)
    return


@app.cell
def _(s):
    # Display the `metadata` attribute to see if these metadata are already present in the signal
    return


@app.cell
def _(s):
    # Add the "Cu" and "Zn" elements
    return


@app.cell
def _(s):
    # Check the metadata again
    return


@app.cell
def _(s):
    # The microscope parameters are already present in the metadata but they are incorrect!
    s.set_microscope_parameters(beam_energy=200, convergence_angle=13.33, collection_angle=55.28)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, we are ready to create the model using [`create_model`](https://hyperspy.org/exspy/reference/signals.html#exspy.signals.EELSSpectrum.create_model). By default, the model contains a power law background and edges
    """)
    return


@app.cell
def _(s):
    # create the model using the `create_model` method
    m = None  # TODO: Use s.create_model()
    return m,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Both the power law background and core less edge components (`EELSCLEdge`) has automatically been added.
    """)
    return


@app.cell
def _(m):
    # display the list of components using the `components` attribute
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The model consist of several components, so we use `plot_components=True` to see the individual components. Here, the red dots are the experimental data, the blue line is the whole model, and the green line is the power law we just fitted. There are also several other components shown in the figure: the Cu and Zn core loss edges. When added, they start with an initial non-zero value, so don't worry that they currently do not fit very well with the data.
    """)
    return


@app.cell
def _(m):
    # Plot the model
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For EELS fitting, it is sensible to fit the componennts in a "cascade" fashion, the individual components are fitting sequentially in order of increasing energy. This is refered as the ["smart" fitting approach](https://hyperspy.org/exspy/user_guide/eels.html#fitting-model) and is implemented by the [`smart_fit`](https://hyperspy.org/exspy/reference/models.html#exspy.models.EELSModel.smart_fit) and `multifit(kind='smart')` methods that fit the current navigation position only and all positions, respecticely.
    """)
    return


@app.cell
def _(m):
    # Fit the whole dataset using the smart fitting approach
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see the results. Go to the region around `(32, 14)`, where there clearly is copper or zinc of some kind.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Get elemental maps
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To get the Cu and Zn maps, we use the [`intensity`](https://hyperspy.org/exspy/reference/components.html#exspy.components.EELSCLEdge.intensity) parameter of the [`EELSCLEdge`](https://hyperspy.org/exspy/reference/components.html#exspy.components.EELSCLEdge) component.

    **Note**: as the L$_3$, L$_2$ and L$_1$ are connected in the fitting procedure, we only have to get one of them to get the relative amount of Cu or Zn.
    """)
    return


@app.cell
def _(m):
    # Create the Cu and Zn map from the `intensity` parameter of the `Cu_L3` and `Zn_L3` components
    # The intensity parameter is converted to a signal using the `as_signal` method:
    Cu_map = None  # TODO: Use m.components.Cu_L3.intensity.as_signal()
    Zn_map = None  # TODO: Use m.components.Zn_L3.intensity.as_signal()
    return Cu_map, Zn_map


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 3. Display and export elemental maps
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To more easily compare them, use the [`hs.plot.plot_images`](https://hyperspy.org/hyperspy-doc/current/user_guide/visualisation.html#plotting-several-images) function.
    """)
    return


@app.cell
def _(Cu_map, Zn_map, hs):
    # Use `plot_images` to visualise the images
    return


@app.cell
def _(plt):
    # Save the figure using `savefig` from matplotlib:
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To get an overlay, where the two intensities are shown with different colors in the same plot, use `overlay=True`.
    """)
    return


@app.cell
def _(Cu_map, Zn_map, hs):
    # Use `plot_images` using overlay and remove axes decor
    return


@app.cell
def _(plt):
    # Save the figure using `savefig` from matplotlib:
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The maps can also be saved in different format, for example, `hspy`, `jpg`, `tif`.
    """)
    return


@app.cell
def _(Cu_map, Zn_map):
    # Save both maps as `hspy` file

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To learn more about optional parameters when exporting images, see the [RosettaSciIO documentation](https://hyperspy.org/rosettasciio/user_guide/supported_formats/image.html#rsciio.image.file_writer).
    """)
    return


@app.cell
def _(Cu_map, Zn_map):
    # Save both maps as `jpg` file and add a scalebar

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 4. Saving and restoring the models
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As the fitting process can be slow, [saving the models](https://hyperspy.org/hyperspy-doc/current/user_guide/model/storing_models.html#saving-and-loading-the-result-of-the-fit) can be a good idea.
    """)
    return


@app.cell
def _(m):
    # Save the model using the `save` method of the model
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This results in a file called `model.hspy`, which can be loaded and restored.
    """)
    return


@app.cell
def _(hs):
    # Load the model using the `load` function from hyperspy
    mr = None  # TODO: Use hs.load('model.hspy')
    mr
    return mr,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A signal is returned and the model is saved in the `models` attribute
    """)
    return


@app.cell
def _(mr):
    # Display the attribute `models`
    return


@app.cell
def _(mr):
    # Restore the model using the `restore` method of the `models` attribute
    mr_restored = None  # TODO: Use mr.models.restore('a')
    return mr_restored,


@app.cell
def _(mr):
    # Plot the model
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    --------------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To learn how to make publication quality figures of the elemental maps using `matplotlib`, see the Jupyter Notebook `plotting_maps_using_matplotlib.ipynb` in https://github.com/hyperspy/exspy-demos
    """)
    return


if __name__ == "__main__":
    app.run()
