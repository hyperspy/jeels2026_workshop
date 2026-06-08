# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "exspy",
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

__generated_with = "0.23.8"
app = marimo.App(
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # EELS analysis of perovskite oxides using eXSpy

    This tutorial shows the various functionalities in eXSpy which is used to analyse Electron Energy Loss Spectroscopy data, using EELS datasets from a perovskite oxide heterostructure.

    It assumes some knowledge on how to use HyperSpy, like loading datasets and how the basic signals work.

    This notebook requires **HyperSpy 2.0.0** or later. In addition **eXSpy**, which has the EELS and EDX specific parts of HyperSpy: https://hyperspy.org/exspy/

    ## Author

    7/6/2016 Magnus Nord - Developed for HyperSpy workshop at Scandem conference 2016

    ## Changes

    * 3/8/2016 Updated for HyperSpy 1.1. Added note about Gatan Digital Micrograph GOS.
    * 20/7/2019 Katherine MacArthur - Checked for Hyperspy 1.5.1 and commented out sections requiring Gatan GOS files.
    * 30/7/2019 Magnus Nord - Minor text improvements for M&M19 short course
    * 9/3/2024 Magnus Nord - Updated to work with HyperSpy 2.0.0
    * 1/6/2025 Eric Prestat - reworked for the ePSIC HyperSpy workshop 2025

    ## Table of contents

    1. Specimen & Data
    2. Loading and aligning data
    3. Fourier ratio deconvolution and peak fitting
    4. Fine structure fitting with convolution
    5. Visualise fitting results
    """)
    return


@app.cell
def _():
    import marimo as mo
    import hyperspy.api as hs
    import hyperspy_gui_anywidget  # noqa: F401
    hs.preferences.GUIs.enable_traitsui_gui = False
    hs.preferences.GUIs.enable_anywidget_gui = True
    hs.preferences.GUIs.enable_ipywidgets_gui = False
    return hs, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 1. Specimen & Data

    The data was acquired on a Jeol ARM200cF using a Gatan Quantum ER with DualEELS capabilities.

    The data itself is from La$_{0.7}$Sr$_{0.3}$MnO$_3$ thin films deposited on SrTiO$_3$. In the fine structure example parts of the film has been exposed to a very long electron beam exposure, inducing oxygen vacancies.

    The datasets has been binned to reduce the file size and processing time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 2. Loading and aligning data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here we take a look at a linescan from a La$_{0.7}$Sr$_{0.3}$MnO$_3$ thin film, where parts of the film has been bombarded with the electron beam for an extended time.

    We start by loading the core-loss dataset stored in `datasets/LSMO_linescan.hspy`
    """)
    return


@app.cell
def _(hs):
    # TODO: open the "datasets/LSMO_linescan.hspy" file
    s = hs.load("___")  # TODO: fill in the filepath
    return s,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Plot the signal, and use the red line in the navigation plot to explore the data. There is clearly something going on in the middle on both the oxygen and the manganese edges. In addition, there are some thickness changes during the line scan.
    """)
    return


@app.cell
def _(s):
    # TODO: Plot the signal
    # s.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using the low loss signal, we make sure the energy scale is properly calibrated: `datasets/LSMO_linescan_low_loss.hspy`
    """)
    return


@app.cell
def _(hs):
    # TODO: Open the "datasets/LSMO_linescan_low_loss.hspy"
    s_ll = hs.load("___")  # TODO: fill in the filepath
    return s_ll,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We plot the low loss signal.
    `autoscale=""` can be used to be disable resetting the zoom when changing the navigation coordinate.
    """)
    return


@app.cell
def _(s_ll):
    # TODO: Plot the signal setting the `autoscale` parameter to disable autoscale
    # s_ll.plot(autoscale="")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The zero loss peak is not well aligned at 0 eV energy loss. We align both signals (low-loss and core-loss) by measuring the energy shift on the zero loss peak and applying the shifts to both signals.
    """)
    return


@app.cell
def _(s, s_ll):
    # TODO: align both signal (`s` and `s_ll`) using `align_zero_loss_peak`.
    # s_ll.align_zero_loss_peak(also_align=[s])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The plotted signal has updated and we can checked that the zero loss peak has been shifted to 0 energy loss.

    We can also calculate the relative thickness using the low loss, with the `estimate_thickness` method. We'll have to specify the end of the zero loss beam, which for cold field emissions guns 3.0 eV seems to work well.
    """)
    return


@app.cell
def _(s_ll):
    # TODO: Use the `estimate_thickness` method — specify the energy threshold
    # s_thickness = s_ll.estimate_thickness(threshold=3.0)
    s_thickness = None  # placeholder — replace with the line above
    return s_thickness,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It would also be possible to use hyperspy to determine the threshold itself using:

        th = s_ll.estimate_elastic_scattering_threshold()
        s_ll.estimate_thickness(threshold=th)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Plotting this gives the relative thickness and, as expected, there is an increase towards the end of the line scan
    """)
    return


@app.cell
def _(s_thickness):
    # TODO: Plot the thickness
    # s_thickness.T.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 3. Fourier ratio deconvolution and peak fitting
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.1 Fourier ratio deconvolution

    Lets take a closer look at the oxygen-K edge, firstly by removing the plasmon background with `remove_background`. Note: this will overwrite the `s` spectrum with the cropped one.
    """)
    return


@app.cell
def _(s):
    # TODO: Remove the background using a signal range of (490, 520)
    # s_bg_removed = s.remove_background(signal_range=(490, 520))
    s_bg_removed = None  # placeholder — replace with the line above

    # TODO: Plot the background subtracted signal
    # s_bg_removed.plot()
    return s_bg_removed,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This makes it much easier to compare the different positions. Pressing 'e' with the spectrum window highlighted gives a second spectrum picker, which can be moved independently of the first one.

    We can then do Fourier ratio deconvolution to remove the effects of plural scattering using the `fourier_ratio_deconvolution` method:
    """)
    return


@app.cell
def _(s_bg_removed, s_ll):
    # TODO: Use the `fourier_ratio_deconvolution` method to perform Fourier ratio deconvolution
    # s_deconvolved = s_bg_removed.fourier_ratio_deconvolution(s_ll)
    s_deconvolved = None  # placeholder — replace with the line above
    return s_deconvolved,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Plotting this, we see that the thickness effects has been greatly reduced towards the end of the line scan
    """)
    return


@app.cell
def _(s_deconvolved):
    # TODO: Plot the deconvolved signal
    # s_deconvolved.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For visualisation purposes, we can create a "meaningless" complex signal as a convenience to compare before and deconvolution, with the real (plotted in red) and imaginary (plotted in blue) part corresponding to the before and after deconvolution, respectively.
    """)
    return


@app.cell
def _(s_bg_removed, s_deconvolved):
    # TODO: Create a "meaningless but convenient" complex signal to compare the signal before and after deconvolution
    # comparison = s_bg_removed + s_deconvolved * 1j
    comparison = None  # placeholder — replace with the line above

    # TODO: Plot the comparison
    # comparison.plot()
    return comparison,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.2 Peak fitting

    Since these peaks we are trying to fit overlapping strongly, the fit is highly susceptible to fall into a local minimum during fit optimisation that doesn't describe well the experimental data. To avoid this issue, we constrain (_guide_) the optimisation by using bounded fitting and setting the bounds (`bmin` and `bmax`) of the `sigma` parameter of the `Gaussian` components.

    The fitting approach consists in the following steps:
    1. set bounding: `bmin = 0.75` and `bmax = 3.5` for the `sigma` parameters. By default the `bmin` of the `A` parameter is set to 0. We could also contrain the `centre` parameter but the fit is satisfactionary without adding this constraint
    2. fit each component individually by specifying a fitting range. The order of the component fitting matters in this case: we start with the 2nd peak, then the 3rd and fit the 1st peak last. We choose to fit the first peak last because this peak is small and it overlaps strongly with the 2nd peak
    3. Fix the `centre` parameter
    4. refine the fit by fitting all components together

    Alternative approaches could be considered, for example, setting the bounds to the `centre` parameter and/or avoid fixing the centre at a later could be worth trying.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As a convenience, we start by cropping the signal in energy to the region of interest - this is not necessary but it makes visualisation slightly easier.
    """)
    return


@app.cell
def _(s_deconvolved):
    # TODO: Use the `crop_signal` method to crop to the energy region of (500, 570)
    # s_deconvolved.crop_signal(500., 560.)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We create a model without a background because it was already removed before the deconvolution
    """)
    return


@app.cell
def _(hs, s_deconvolved):
    # Create a model without background
    m = s_deconvolved.create_model(auto_background=False)
    return m,


@app.cell
def _(m):
    # TODO: Plot the model and its components individually
    # m.plot(True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We will fit three Gaussian functions to the edge. We create these components and add them to the model.
    """)
    return


@app.cell
def _(hs):
    g1 = hs.model.components1D.Gaussian()
    g1.name = "O_K_peak1"
    g2 = hs.model.components1D.Gaussian()
    g2.name = "O_K_peak2"
    g3 = hs.model.components1D.Gaussian()
    g3.name = "O_K_peak3"
    return g1, g2, g3


@app.cell
def _(g1, g2, g3, m):
    # Add these components to the model
    m.extend([g1, g2, g3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Step 1: set the bounds of the `sigma` parameter
    """)
    return


@app.cell
def _(g1, g2, g3):
    # Set the bmin and bmax of the `sigma` parameter of all Gaussian components
    for _g in [g1, g2, g3]:
        _g.sigma.bmin = 0.75
        _g.sigma.bmax = 3.5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we fit the components individually, starting from the 2nd peak as described previously

    Step 2: fit each component individually
    """)
    return


@app.cell
def _(g2, m):
    # TODO: Use the `fit_component` method of the model to fit the 2nd component
    # Specify signal range (528., 532.); fit all navigation coordinates; Use bounded fit
    # m.fit_component(g2, signal_range=(528., 532.), only_current=False, bounded=True)
    return


@app.cell
def _(g3, m):
    # TODO: Same as last cell but for 3rd component; use signal range (535., 540.)
    # m.fit_component(g3, signal_range=(535., 540.), only_current=False, bounded=True)
    return


@app.cell
def _(g1, m):
    # TODO: Same as last cell but for 1st component; use signal range (523., 526.)
    # m.fit_component(g1, signal_range=(523., 526.), only_current=False, bounded=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Step 3: fix the `centre` parameter of the three Gaussian components
    """)
    return


@app.cell
def _(m):
    # TODO: Use the `set_parameters_not_free` method of the model
    # m.set_parameters_not_free(parameter_name_list=["centre"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Fit for the current position to check that the fit converge to a satisfactory minimum; a few positions can be checked
    """)
    return


@app.cell
def _(m):
    # TODO: Make sure to use bounded fit
    # m.fit(bounded=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Once satisfied with current fit, fit for all navigation positions
    """)
    return


@app.cell
def _(m):
    # TODO: use `multifit` with bounding
    # m.multifit(bounded=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 4. Fine structure fitting with convolution

    In this section, we will use a different approach: instead of performing a deconvolution before the fitting, we will convolve the mode during fitting. The second approach is expected to provide more accurate results and be more robust because of the following reasons:
    - convolution is numerical more stable than deconvolution accross different experimental dataset, mostly because deconvolution is not a trivial problem to solve numerically: it uses iterative approaches and can also introduce artefacts.
    - Fitting background and edges together usually better describe the experimental data.

    We reload and align the data. Similarly as in the previous section, we start by cropping a region of the O-K edge, for example 450 to 590 eV as a convenience - here, we will use a wider signal range to fit the background and edges.
    """)
    return


@app.cell
def _(hs):
    # TODO: load the datasets and align them
    s2 = hs.load("___")  # TODO: fill in the filepath (core-loss)
    s2_ll = hs.load("___")  # TODO: fill in the filepath (low-loss)

    # TODO: align zero loss peak, also aligning the core-loss signal
    # s2_ll.align_zero_loss_peak(also_align=[s2])

    # TODO: crop the signal to energy range (450., 590.)
    # s2.crop_signal(450., 590.)
    return s2, s2_ll


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We will also check that the elements are correctly in `metadata.Sample.elements`
    """)
    return


@app.cell
def _(s2):
    # Display the metadata
    s2.metadata
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As no elements is defined in the metadata, we add them using the `add_elements` method
    """)
    return


@app.cell
def _(s2):
    s2.add_elements(("O",))
    s2.metadata
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We create the model. We pass the low-loss signal to take into account multiple scattering into the model: the model will be convolved with a the low-loss before being fitted to the data.
    """)
    return


@app.cell
def _(s2, s2_ll):
    # Use the `create_model` method from the signal; don't forget to set the low loss
    m2 = s2.create_model(low_loss=s2_ll)
    return m2,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We check that we have the expected components: a background the `O_K` edges
    """)
    return


@app.cell
def _(m2):
    m2.components
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We plot the model with the individually components as we will used these to observe how the fit proceed
    """)
    return


@app.cell
def _(m2):
    # TODO: Plot the model and its components individually
    # m2.plot(True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We perform a smart fit to fit components before fitting the peaks of the fine structure
    """)
    return


@app.cell
def _(m2):
    # TODO: Run smart fit
    # m2.smart_fit()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can notice that the edge position doesn't describe well the data, we adjust the `onset_energy`. Visual inspecting shows us that the onset is at 524 eV. We want to do that for all navigation positions.
    """)
    return


@app.cell
def _(m2):
    # TODO: Use the `set_parameters_value` method from the model
    # m2.set_parameters_value("onset_energy", 524, component_list=[1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We run a fit again to check how the fit improves
    """)
    return


@app.cell
def _(m2):
    # TODO: Run smart fit again
    # m2.smart_fit()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Once we have satisfy with the current fit, fit all navigation positions
    """)
    return


@app.cell
def _(m2):
    # TODO: Run multifit with kind="smart"
    # m2.multifit(kind="smart")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We enable the fine structure and set the `fine_structure_width` to 30. Further documentation is available in the [eXSpy user guide](https://hyperspy.org/exspy/user_guide/eels.html#fine-structure-analysis-using-gaussian-functions).
    """)
    return


@app.cell
def _(m2):
    m2.enable_fine_structure()
    m2[1].fine_structure_width = 30
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We fit all navigation positions.
    """)
    return


@app.cell
def _(m2):
    # TODO: Run multifit with kind="smart"
    # m2.multifit(kind="smart")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The fit looks very nice but this is still using spline to fit the fine structure. This approach of fitting the fine structure is useful to improve fit quality and get accurate edges intensity for quantification but it doesn't give use the characteristics (peaks, height, width) of the peaks of the fine structure.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Add Gaussian to the fine structure

    To get the characteristics (peaks, height, width) of the peaks of the fine structure, we will add `Gaussian` components and fit these in the same manner as done in the section 3.2.
    """)
    return


@app.cell
def _(hs):
    # Create the three Gaussian copmponents
    g1_m2 = hs.model.components1D.Gaussian()
    g1_m2.name = "O_K_peak1"
    g2_m2 = hs.model.components1D.Gaussian()
    g2_m2.name = "O_K_peak2"
    g3_m2 = hs.model.components1D.Gaussian()
    g3_m2.name = "O_K_peak3"
    return g1_m2, g2_m2, g3_m2


@app.cell
def _(g1_m2, g2_m2, g3_m2):
    # Set bounds on the `sigma` parameter
    for _g in [g1_m2, g2_m2, g3_m2]:
        _g.sigma.bmin = 0.75
        _g.sigma.bmax = 3.5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Add the `Gaussian` components to the list of `fine_structure_components`. We also set the `fine_structure_spline_onset`, which defines where the spline will start to a value of 18.
    """)
    return


@app.cell
def _(g1_m2, g2_m2, g3_m2, m2):
    # TODO: Get the O_K edge component from the model
    O_K = m2.components.O_K

    # TODO: Add Gaussian components to fine_structure_components and set spline_onset
    # O_K.fine_structure_components.update((g1_m2, g2_m2, g3_m2))
    # O_K.fine_structure_spline_onset = 18
    return O_K,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Fit the three Gaussian components individually; observe how the fit progress before each steps and if it describes well the experimental data.
    """)
    return


@app.cell
def _(g2_m2, m2):
    # TODO: Fit g2_m2 with signal_range=(528., 532.), bounded=True
    # m2.fit_component(g2_m2, signal_range=(528., 532.), only_current=False, bounded=True)
    return


@app.cell
def _(g3_m2, m2):
    # TODO: Fit g3_m2 with signal_range=(535., 540.), bounded=True
    # m2.fit_component(g3_m2, signal_range=(535., 540.), only_current=False, bounded=True)
    return


@app.cell
def _(g1_m2, m2):
    # TODO: Fit g1_m2 with signal_range=(523., 526.), bounded=True
    # m2.fit_component(g1_m2, signal_range=(523., 526.), only_current=False, bounded=True)
    return


@app.cell
def _(m2):
    # TODO: Fix the centre parameter
    # m2.set_parameters_not_free(parameter_name_list=["centre"])
    return


@app.cell
def _(m2):
    # TODO: Run smart fit with bounded=True
    # m2.smart_fit(bounded=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, fit all components together for all navigation positions.
    """)
    return


@app.cell
def _(m2):
    # TODO: Run multifit with kind="smart" and bounded=True
    # m2.multifit(kind="smart", bounded=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 5. Visualise fitting results

    We can then compare the parameters in the components, by getting the parameter values as signals using the `as_signal` method.

    Firstly get the ratio of the `A` parameters for the largest peak and the pre-peak, by using `as_signal` and dividing the signals. Then plot the results.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5.1 Fitting after deconvolution
    """)
    return


@app.cell
def _(g1, g3):
    g1_g3_ratio = g1.A.as_signal() / g3.A.as_signal()
    return g1_g3_ratio,


@app.cell
def _(g1_g3_ratio):
    # TODO: Plot the ratio
    # g1_g3_ratio.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then get the difference in centre positions between the largest peak and the pre-peak, via the `centre` parameter in the Gaussians.
    """)
    return


@app.cell
def _(g1, g3):
    g1_g3_position = g3.centre.as_signal() - g1.centre.as_signal()
    return g1_g3_position,


@app.cell
def _(g1_g3_position):
    # TODO: Plot the position difference
    # g1_g3_position.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Lastly, get the ratio of the `sigma` parameters in the largest peak and the pre-peak.
    """)
    return


@app.cell
def _(g1, g3):
    g1_g3_sigma = g1.sigma.as_signal() / g3.sigma.as_signal()
    return g1_g3_sigma,


@app.cell
def _(g1_g3_sigma):
    # TODO: Plot the sigma ratio
    # g1_g3_sigma.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In all of the comparisons there are some large changes in the region with beam damage. However, the values can vary a great deal. This is most likely due to the pre-peak almost disappearing at some points in the line scan, leading to bad fitting of g1 and g3.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5.2 Fitting with convolution
    """)
    return


@app.cell
def _(g1_m2, g3_m2):
    g1_g3_ratio_m2 = g1_m2.A.as_signal() / g3_m2.A.as_signal()
    return g1_g3_ratio_m2,


@app.cell
def _(g1_g3_ratio_m2):
    # TODO: Plot the ratio for the convolution approach
    # g1_g3_ratio_m2.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then get the difference in centre positions between the largest peak and the pre-peak, via the `centre` parameter in the Gaussians.
    """)
    return


@app.cell
def _(g1_m2, g3_m2):
    g1_g3_position_m2 = g3_m2.centre.as_signal() - g1_m2.centre.as_signal()
    return g1_g3_position_m2,


@app.cell
def _(g1_g3_position_m2):
    # TODO: Plot the position difference for the convolution approach
    # g1_g3_position_m2.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Lastly, get the ratio of the `sigma` parameters in the largest peak and the pre-peak.
    """)
    return


@app.cell
def _(g1_m2, g3_m2):
    g1_g3_sigma_m2 = g1_m2.sigma.as_signal() / g3_m2.sigma.as_signal()
    return g1_g3_sigma_m2,


@app.cell
def _(g1_g3_sigma_m2):
    # TODO: Plot the sigma ratio for the convolution approach
    # g1_g3_sigma_m2.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5.3 Comparison of fitting results for both approaches
    """)
    return


@app.cell
def _(g1_g3_ratio, g1_g3_ratio_m2, hs):
    # TODO: Use hs.plot.plot_spectra to compare the two approaches
    # ax = hs.plot.plot_spectra([g1_g3_ratio, g1_g3_ratio_m2], legend=["Deconvolution approach", "Convolution approach"])
    # ax.set_ylabel("1st to 3rd peak intensity ratio")
    ax = None  # placeholder — replace with the lines above
    return ax,


@app.cell
def _(g1_g3_position, g1_g3_position_m2, hs):
    # TODO: Use hs.plot.plot_spectra to compare the two approaches
    # ax2 = hs.plot.plot_spectra([g1_g3_position, g1_g3_position_m2], legend=["Deconvolution approach", "Convolution approach"])
    # ax2.set_ylabel("1st to 3rd peak separation (eV)")
    ax2 = None  # placeholder — replace with the lines above
    return ax2,


if __name__ == "__main__":
    app.run()
