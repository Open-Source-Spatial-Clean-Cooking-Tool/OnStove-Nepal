# <img src="assets/img/OnStoveLogoNepal.svg" alt="drawing" style="width:400px"/>

This repository contains the general code for the Nepal case study developed using the geospatial 
cost-benefit clean cooking tool, OnStove. OnStove calculates the net-benefits of different stove 
options in a given geography and compares all stoves to one another with regards to their net-benefit.
In this study, we linked outputs from OnStove with a multicriteria analysis (MCA) based on the methods of the 
Energy Access Explorer (EAE).

## Introduction 
OnStove is developed by the division of Energy Systems at KTH together with partners. OnStove, is a 
geospatial raster-based tool that determines the net-benefits of different cooking solutions, 
for each raster grid cell of a given study area. The tool takes into account four benefits of 
adopting clean cooking: reduced morbidity, mortality, emissions and time saved, as well as three costs: 
capital, fuel, and operation and maintenance (O&M). In each grid cell of the study area the 
stove with the highest net-benefit is chosen.

OnStove produces scenarios depicting the “true” cost of clean cooking. The scenarios benefits' and costs
produced by the tool are to be interpreted as the benefits and costs one could expect if the clean 
cooking transition was to happen now (overnight change). Results from OnStove are can be interpreted as 
an upper bound of net-benefits following a switch to cleaner stoves. This can give a sense of the cost 
of inaction. OnStove can be used by planners and policy makers to identify whether various 
combinations of interventions in their settings would be worth the potential benefits that could be 
captured.

## Installation 
Install a python distribution using
[Miniconda](https://docs.conda.io/en/latest/miniconda.html#) (recommended) or
[Anaconda](https://www.anaconda.com/)

### Downloading the source code
Open an `Anaconda Prompt` or a `Command Prompt` and download the source code with:
```
> conda install git
> git clone https://github.com/Open-Source-Spatial-Clean-Cooking-Tool/OnStove-Nepal.git
```
or you can download as a zip file from the GitHub repository.

### Installing ``OnStove`` with `conda`
The easiest way of installing and using `OnStove` is through `conda`. After installing a distribution of 
`conda`, open an `Anaconda Prompt` or a `Command Prompt`, and run:
```
> conda create -n onstove -c conda-forge onstove
```
After a few minutes, you will have a new conda environment called `onstove` with `OnStove` installed 
on it. To use it open an `Anaconda Prompt`, and activate the environment with:
```
> conda activate onstove
```
Now your environment `onstove` is available to use. **Note that you need to activate it
always before conducting any analysis**.

## Running the analysis
In the `Anaconda Prompt`, change your current directory to the path where you have the OnStove Nepal 
code, using the command `cd`: 
```
> cd replace-with-folder-path
```
Then open a Jupyter lab session with:
```
> jupyter lab
```
Double click on one of the notebooks inside the `3. Scripts` folder and follow the steps described
there. The order of the analysis is:
1. ``DataProcessor.ipynb`` - reads and processes all raw geospatial data needed for the analysis.
2. ``NepalRunner.ipynb`` - runs the `OnStove` model for Nepal for one selected scenario.
3. ``MCA.ipynb`` - runs the `MCA` analysis based on the results of the `OnStove` model, to prioritize 
actions based on the government's goals.

## Documentation
Access the latest OnStove documentation in [read the docs](https://onstove-documentation.readthedocs.io/en/latest/?badge=latest).
