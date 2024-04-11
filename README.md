<h1 align='center' style="text-align:center; font-weight:bold; font-size:2.5em"> Data Collection Project<br>Candidiate Locater</h1>

<p align='center' style="text-align:center;font-size:1em;">
    <a>Majd Bishara</a>&nbsp;,&nbsp;
    <a>Saleem Kheer-Eldeen</a>&nbsp;,&nbsp;
    <a>Tameer Milhem</a>&nbsp;,&nbsp;
    <a>Lana Haj</a>&nbsp;
    <br/> 
    Technion Institute of Technology<br/> 
    
</p>



# Contents

- [Overview](#overview)
- [Example](#example)
- [Files](#files)
  - [Data](#data)
  - [Notebooks](#notebooks)
  - [Assets](#assets)

## Overview

The "Candidate Locator" project introduces an advanced solution to streamline candidate selection processes within organizations. By harnessing the power AI, particularly LLMs, alongside thorough data collection and processing methods, the project aims to optimize recruitment efforts and identify optimal candidates for specific roles.

At its core, the project employs a pipeline, taking input `meta_indsutry` represeting the recruiter's industry and `prompt` which is the recruitter's description of the candidate they seek, then using LLMs and sophistacated embeddings we find a set of potential candidates which we order according to their expected work duration using a regression model.

By automating candidate selection and tenure prediction, the "Candidate Locator" project offers a data-driven approach to hiring, promising enhanced efficiency and informed decision-making for organizations seeking to secure top talent.

![Pipeline](data/assets/Pipeline.png)

## Example

To run an example head to [Pipeline Notebook](data/notebooks/Final_pipeline.ipynb), and choose your own HR Prompt and meta industry, as an example: 
- `meta_industry = Technology`
- `prompt = Looking for individuals skilled in HTML, CSS, and JavaScript for front-end web development.`

Run the notebook

**Output:**
|id|name|description|expected duration (months)|
|--|----|-----------|-----------------|
|1|James|Experienced Front-End Developer with 3+ year experience in Java, HTML, CSS and Javascript| 24|
|...|...|...| ...|

## Files

### Data

There are 3 external Datasets used throughout the project:
- [Job Listings (scrapped)](data/datasets/job_postings_raw.csv)
- [People Skills](data/datasets/employee_skills_35.csv)
- [Job Requiremenets](data/datasets/job_requiremenets.csv)

### Notebooks

There are 4 notebooks that are divided by subject, the notebook were writting through databricks and should be ran using it:
- [Data Analysis](data/notebooks/Data\ Analysis.ipynb) - Comprehensive analysis of the data with interactive visualizations
- [Pipline](data/notebooks/Final_pipeline.ipynb) - Implementation of the pipeline described
- [Scraping](data/notebooks/scrapping.ipynb) - Code used to scrap data from Linkedin, to use either use your BrightData credintials or set `USE_PROXY = False`
- [Insights](data/notebooks/insights.ipynb) - Minor Insights about the different meta industries

### Misc
Other files, like the files used to interface with the LLM and extract the skills and requiremenets

### Assets

Pictures and other files for the repo
