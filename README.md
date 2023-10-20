This repository contains the general code for the Nepal case study developed using the geospatial 
cost-benefit clean cooking tool, OnStove. OnStove calculates the net-benefits of different stove 
options in a given geography and compares all stoves to one another with regards to their net-benefit.
In thi study, we linked outputs from OnStove with a multicriteria analysis (MCA) based on the methods of the 
Energy Access Explorer (EAE).

## Introduction 
OnStove is developed by the division of Energy Systems at KTH together with partners. The tool is a 
geospatial, raster-based tool determining the net-benefit of different cooking solutions selected by 
the user for raster grid cell of a given study area. The tool takes into account four benefits of 
adopting clean cooking: reduced morbidity, mortality, emissions and time saved, as well as three costs: 
capital, fuel as well as operation and maintenance (O&M) costs. In each grid cell of the study area the 
stove with the highest net-benefit is chosen.

OnStove produces scenarios depicting the “true” cost of clean cooking. The scenarios benefits and costs
of produced by the tool are to be interpreted as the benefits and costs one could expect if the clean 
cooking transition was to happen now (overnight change). Results from OnStove are to be interpreted as 
an upper bound of net-benefits following a switch to cleaner stoves. OnStove can be used by planners 
and policy makers to identify whether various combinations of interventions in their settings would be 
worth the potential benefits that could be captured

## Installation 
Install a python distribution using 
[Anaconda](https://www.anaconda.com/) or 
[Miniconda](https://docs.conda.io/en/latest/miniconda.html#) (recommended).

### Downloading the source code
Open an `Anaconda Prompt` or a `Command Prompt` and download the source code with:
```
> conda install git
> git clone <<adrress-to-repo>>
```
or you can download as a zip file from the GitHub repository.

### Installing ``OnStove`` with `conda`
The easiest way of installing and using `OnStove` is through `conda`. After installing a distribution of 
`conda`, open an `Anaconda Prompt` or a `Command Prompt` and run:
```
> conda create -n onstove -c conda-forge onstove
```
Now you will have a new conda environment called `onstove` with `OnStove` installed on it. To use it 
open a `Command Prompt`
in the root folder of your analysis and activate the environment with:
```
> conda activate onstove
```

Now your environment `onstove` is available to use. Note that you need to activate it
always before conducting any analysis.

## Running the analysis
Open a Jupyter lab session and follow the steps on the notebooks.
```
> cd root-folder-path
> jupyter lab
```

## Documentation
Access the latest OnStove documentation in [read the docs](https://onstove-documentation.readthedocs.io/en/latest/?badge=latest).
