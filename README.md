# League of Legends Ranked Game Analysis
*Author: Colin Heider*

## Summary
This is a project repo from class AD450 at North Seattle College, also will be used as a portfolio project for statistical analysis 

## Table of Contents
1. [Installation](#installation)
2. [File Structure](#file-structure)
3. [Main](#main)
4. [Report](REPORT.md)
5. [Contribution](CONTRIBUTION.md)


## Installation

In your terminal, navigate to a location to download the repository.  Clone the repository with the command below.
```bash
git clone https://github.com/cheider/AD450-FinalProject
```
Check that Conda is installed by running:
```bash
conda --version
```
If not installed, visit the anaconda website for instructions of installing Conda.

After the repository is cloned, and Conda is installed: navigate into the project from the terminal.  
Then, install the dependencies listed in the requirements.yml file using the command:
```bash
conda env create -f requirements.yml
```
Activate the newly created environment:
```bash
conda lol_stats_env
```

## File Structure

|Directory|File|Purpose|Function|
|:--|:--|:--|:--|
|root|
||README.md|root source for all documentation|
||main.ipynb|DESCRIPTION FOR MAIN HERE|
||REPORT.md|full report including project design, result charts, and analysis|
||requirements.yml|dependency list|
||CONTRIBUTING.md|tracks contributions of team members|
||.gitignore|blocks files from git tracking|
|data|various|houses csv files for input data|
|images|various|houses chart images files for report|
|test|various|houses test and unit tests for various functions within this project|
|util||contains processing and generation files for input and output used in the main notebook file|

