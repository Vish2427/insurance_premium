# Insurance Premium Prediction

Application URL : [InsurancePremiumPredictor](https://premium-insurance.herokuapp.com/)

## Table of contents
* [Problem Statement](#problem-statement)
* [Solution Proposed](#solution-proposed)
* [Tech Stack Used](#tech-stack-used)
* [Software and account requirement](#software-and-account-requirement)
* [Setup](#setup)
* [Project Pipeline](#project-pipeline)
### Problem Statement
Insurance are beneficial to anyone looking to protect their family, assets/property and themselves from financial risk/losses.
Insurance plans will help you pay for medical emergencies, hospitalisation, contraction of any illnesses and treatment, and medical care required in the future.
The financial loss to the family due to the unfortunate death of the sole earner can be covered by insurance plans. 
This is a regression problem, in which persons information and health details are taken to 
predict how much espense is required for their insurance premium.

### Solution Proposed

In this project the goal is to give people an estimate of how much they need based on
their individual health situation. After that, customers can work with any health
insurance carrier and its plans and perks while keeping the projected cost from our
study in mind. 
The problem is to find the expense of the insurance premium which can assist a person in concentrating on the health side of an insurance policy rather han the ineffective part.

## Tech Stack Used

1. Python 
2. FlaskAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB
6. GitHub Actions

## Software and account Requirement
1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)


## Setup
Create a conda environment
```
conda create -p venv python==3.7 -y
```

activate conda environment
```
conda activate ./venv
```

To install requirement file
```
pip install -r requirements.txt
```

* Add files to git  `git add .` or  `git add <file_name>`    
* To check the git status  `git status`    
* To check all version maintained by git  `git log`    
* To create version/commit all changes by git  `git commit -m "message"`    
* To send version/changes to github  `git push origin main`    


## Project Pipeline
1. [Data Ingestion](#1-data-ingestion)
2. [Data Validation](#2-data-validation)
3. [Data Transformation](#3-data-transformation)
4. [Model Training](#4-model-training)
5. [Model Evaluation](#5-model-evaluation)
6. [Model Deployement](#6-model-deployement)

### 1. Data Ingestion: 
* Data ingestion is the process in which unstructured data is extracted from one or multiple sources and then prepared for training machine learning models.

### 2. Data Validation:
* Data validation is an integral part of ML pipeline. It is checking the quality of source data before training a new mode
* It focuses on checking that the statistics of the new data are as expected (e.g. feature distribution, number of categories, etc). 

### 3. Data Transformation 
* Data transformation is the process of converting raw data into a format or structure that would be more suitable for model building.
* It is an imperative step in feature engineering that facilitates discovering insights.

### 4. Model Training
* Model training in machine learning is the process in which a machine learning (ML) algorithm is fed with sufficient training data to learn from.

### 5. Model Evaluation
* Model evaluation is the process of using different evaluation metrics to understand a machine learning model’s performance, as well as its strengths and weaknesses.
* Model evaluation is important to assess the efficacy of a model during initial research phases, and it also plays a role in model monitoring.

### 6. Model Deployement
* Deployment is the method by which we integrate a machine learning model into production environment to make practical business decisions based on data. 

