# VizBlend

[![PyPI Version](https://img.shields.io/pypi/v/vizblend)](https://pypi.org/project/vizblend/) [![License](https://img.shields.io/pypi/l/vizblend)](https://github.com/MahmoudHousam/VizBlend/blob/master/LICENSE) [![Build Status](https://github.com/MahmoudHousam/VizBlend/actions/workflows/release.yml/badge.svg)](https://github.com/MahmoudHousam/VizBlend/actions) [![CI/CD](https://github.com/MahmoudHousam/VizBlend/actions/workflows/main.yml/badge.svg)](https://github.com/MahmoudHousam/VizBlend/actions) [![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/) [![PyPI Downloads](https://static.pepy.tech/badge/vizblend)](https://pepy.tech/projects/vizblend)

VizBlend is a Python package that simplifies creating interactive analytical reports by consolidating Plotly figures into a single HTML file. It’s designed to function like a modern PowerPoint presentation but with the power of stunning and interactive data visualizations.

Whether you’re a data analyst, scientist, or developer, VizBlend streamlines the visualization workflow and enhances collaboration.

# Demo
Below is a preview of a report generated with VizBlend:

⭐ If You Like It, Start it, please! ⭐
![VizBlend Thumbnail](https://cdn.jsdelivr.net/gh/MahmoudHousam/VizBlend@master/demo/preview5.gif)
[VizBlend Thumbnail](https://cdn.jsdelivr.net/gh/MahmoudHousam/VizBlend@master/demo/preview5.gif)

# Installation and use case

Install vizBlend using pip:
```
pip install vizBlend
```
Import VizBlend and add figures
```
from vizblend import CreateReport  
import plotly.graph_objects as go  

report = CreateReport(report_title="Sales Report")  
bar_fig = go.Figure(go.Bar(x=["A", "B", "C"], y=[10, 20, 30]))  
report.add_figure(bar_fig, {"title": "Sales Data"})
```
Generate the report
```
report_file = report.blend_graphs_to_html()  
print(f"Report saved to {report_file}")
```

# Learning Purpose

Beside its main job, this repo intends to teach aspiring data analysts or even data scientists who cannot have full control over their coding cycle. With a simple mission: create visualizations and append them to an HTML file, you can take your learning curve up to include useful skills:
* Write unit and integration tests with edge cases to ensure your code is not error-prone.

* Write CI/CD workflows to run on every push or pull request to ensure the newly committed code is compatible enough.

* Creating, managing and deploying your package to PyPi so that you can simply run `pip install <package_name>` and start using it.


    ##### Useful Resources

    * [Building and testing Python | Official GitHub Actions Docs](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python)

    * [pypi-publish | GitHub Action](https://github.com/marketplace/actions/pypi-publish)

