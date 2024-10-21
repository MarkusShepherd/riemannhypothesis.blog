# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import jupyter_black
from mpmath import zeta
from zeta_animation import animate_complex_function

jupyter_black.load()

# %%
animate_complex_function(
    function=zeta,
    z_start=0.5 + 0j,
    z_end=0.5 + 200j,
    background_color="black",
    axis_color="darkgrey",
    plot_steps=30_000,
    fade_steps=2_000,
    line_base_color="orange",
    min_opacity=0.2,
    width=3840,
    height=2160,
    dpi=100,
    duration_s=120,
    fps=60,
    out_path="zeta_4k_60fps.mp4",
)
