# <img src="assets/img/OnStoveLogoNepal.svg" alt="drawing" style="width:400px"/>

This repository contains the general code for the Nepal case study developed using the geospatial 
cost-benefit clean cooking tool, OnStove. OnStove calculates the net-benefits of different stove 
options in a given geography and compares all stoves to one another with regards to their net-benefit.
In this study, we linked outputs from OnStove with a spatial multicriteria analysis (MCA) based on the methods of the 
[Energy Access Explorer (EAE)](https://www.energyaccessexplorer.org/).

## Introduction 
OnStove is developed by the division of [Energy Systems at KTH](https://www.energy.kth.se/energy-systems/division-of-energy-systems-1.937036) 
together with partners. OnStove, is a geospatial raster-based tool that determines the net-benefits of 
different cooking solutions, for each raster grid cell of a given study area. The tool takes into account 
four benefits of adopting clean cooking: reduced morbidity, mortality, emissions and time saved, as well
as three costs: capital, fuel, and operation and maintenance (O&M). In each grid cell of the study area the 
stove with the highest net-benefit is chosen.

OnStove produces scenarios depicting the “true” cost of clean cooking. The scenarios' benefits and costs
produced by the tool are to be interpreted as the benefits and costs one could expect if the clean 
cooking transition were to happen now (overnight change). Results from OnStove can be interpreted as 
an upper bound of net-benefits following a switch to cleaner stoves. This can give a sense of the cost 
of inaction. OnStove can be used by planners and policymakers to identify the potential benefits  
different interventions could cause in their systems.

## Installation 
Install a python distribution using
[Miniconda](https://docs.conda.io/en/latest/miniconda.html#) (recommended) or
[Anaconda](https://www.anaconda.com/)

### Downloading the source code
Open an `Anaconda Prompt` or a `Command Prompt` and download the source code with:
```
conda install git
git clone https://github.com/Open-Source-Spatial-Clean-Cooking-Tool/OnStove-Nepal.git
```
or you can download as a zip file from the GitHub repository. The repository contains the folder 
structure and scripts needed to run the entire analysis.

### Installing ``OnStove`` with `conda`
The easiest way of installing and using `OnStove` is through `conda`. The `OnStove` Nepal model, uses 
version `0.1.6` of the tool. After installing a distribution of 
`conda`, open an `Anaconda Prompt` or a `Command Prompt`. You can install the environment by either running:
```
conda create -n onstovenepal -c conda-forge -c bioconda onstove==0.1.6 snakemake-minimal
```
Or by using the provided ``environment.yaml`` file in the root folder:
```
conda env create -f environment.yaml
```
After a few minutes, you will have a new conda environment called `onstovenepal` with `OnStove` installed 
on it. To use it open an `Anaconda Prompt`, and activate the environment with:
```
conda activate onstovenepal
```
Now your environment `onstovenepal` is available to use. 
> [!IMPORTANT]
> Note that you always need to activate the 
environment before conducting any analysis.

## Input data
All GIS and socio- and techno-economic data for the model, can be downloaded from the permanent repository at 
DOI: [10.5281/zenodo.10641858](https://doi.org/10.5281/zenodo.10641858). Download the data and extract it
inside the `1. Data` and `2. Scenario inputs` based on the information provided in the repository.

## Running the analysis
In the `Anaconda Prompt`, change your current directory to the `3. Scripts` folder inside the path where 
you have the OnStove Nepal project, using the command `cd`: 
```
cd <replace-with-folder-path>/3.\ Scripts
```
Once you are in that folder you have two different ways you can run the analysis:

### Running manually with Jupyter lab
Open a Jupyter lab session running the following in the anaconda prompt:
```
jupyter lab
```
Double-click on one of the notebooks inside the `3. Scripts` folder and follow the steps described
there. The order of the analysis is:
1. ``DataProcessor.ipynb`` - reads and processes all raw geospatial data needed for the analysis.
2. ``OnStove.ipynb`` - runs the `OnStove` model for Nepal for one selected scenario.
3. ``MCA.ipynb`` - runs the `MCA` analysis based on the results of the `OnStove` model, to prioritize 
actions based on the government's goals.

### Running with the automated workflow through `Snakemake`
You can run the entire analysis using the `Snakemake` automated workflow. The workflow will allow you to run the entire 
model very easily, going from raw data processing, up to results and visualizations creation. To read more about 
The ``OnStove`` workflow, please visit the post about
[the development of the `OnStove` automated workflow](https://climatecompatiblegrowth.github.io/guidelines/knowledge/2023/09/27/onstove-workflow.html).

To run the workflow type in the anaconda prompt:
```
snakemake -n
```
This will perform a dry run that will tell you what are the different steps that will be performed without running them.
This is useful to check that your model input files are in the right places and to see which will be the expected
output files. Then to start the analysis run:
```
snakemake --cores 3
```
Where `--cores 3` tells the computer how many processes it is allowed to run in parallel. This is directly linked 
with the number of scenarios.

## Results
After the runs finish, all results will be available in the `4. Results` folder. You can read more about the results and
access them at the permanent repository at DOI: [10.5281/zenodo.10643983](https://doi.org/10.5281/zenodo.10643983), and in the 
related paper.

## Documentation
Access the latest OnStove documentation in [read the docs](https://onstove-documentation.readthedocs.io/en/latest/?badge=latest).
