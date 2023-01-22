# Heritage Housing

Heritage Housing is a project designed to study and predict the sales prices of houses in the city of Ames, Iowa, as requested by a client.

The App live link is: https://heritage-housing.herokuapp.com/

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Unit Range|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above ground (i.e. does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|


## Business Requirements
As a good friend, you are requested by your friend, Lydia Doe, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own country of Belgium, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and has provided that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

The client has indicated that any model used for predicting the house sale prices must have an R2 score of at least 0.75 in order to give her confidence in the results. Note: The R2 (or R squared) metric, is the proportion of the variation in the dependent variable that is predictable from the independent variable(s)

## Hypothesis and Validation
Before undertaking the data analysis, a project hypothesis was posed. This is the outcome that would be expected, and will be verified as to whether it is true or not as part of the data analysis.

- **Hypothesis**: Houses that are larger and of higher quality, will have a higher sales price.
- **Validation**: This will be validated by studying the correlation between house size and quality variables, with the target sales price variable.


## The rationale to map the business requirements to the Data Visualisations and ML tasks
| Requirement | Tasks |
| --- | --- |
| 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that. | <ul> <li>Review dataset using Pandas Profiling.</li> <li>Run a correlation study using Pearson and Spearman correlation, and Predictive Power Score.</li> <li>Select the variables to consider for studying.</li> <li>Create graphs to visualise the correlations to Sale Price for the selected variables.</li> </ul>|
| 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa. | <ul> <li>Determine and perform data cleansing and feature engineering.</li> <li>Select a suitable algorithm to apply to the data to predict sale price.</li> <li>Determine the appropriate hyperparameters to ensure the model meets the client requirements.</li> <li>Deploy a Streamlit dashboard to display the information for the above.</li> </ul> |


## ML Business Case
* The aim is to create an ML model to predict the sale price of houses in Ames, Iowa. A target variable is an integer. We consider a regression model, which is supervised and uni-dimensional.
* The ideal outcome is to provide the client with accurate predictions for the sale price of the houses in her inherited portfolio as well as any other house, so that she can maximise the prices. This will be though the use of a dashboard.
* The model success metrics are:
    * At least 0.75 for R2 score on both train and test sets
    * The ML model is considered a failure if the R2 score is below 0.75 on either (or both) the train and test sets, and/or if the model's predictions are more than 50% off for 30% of inputs after 12 months of use. If this occurs, new/updated models should be developed.
* The output is defined as a continuous value for the sale price. This will be both for the client's inherited properties, as well as for any house in Ames, Iowa, using house attribute information.
* Heuristics: Currently, there is no approach to predict the sale price of houses.
* The training data to fit the model comes from the dataset obtained from Kaggle (see Dataset Content above). This dataset contains about 1.5 thousand house records in the area.
    * The target variable is SalePrice, with all other variables being considered for the model.

## CRISP-DM

This project uses the CRISP-DM process model as the base for the tasks. This stands for "**CR**oss **I**ndustry **S**tandard **P**rocess for **D**ata **M**ining". This has six phases as per the table below. Against each is shown how each phase has been addressed in the project.

| Phase | How Addressed |
| --- | --- |
| 1. Business Understanding | The Business Understanding phase focuses on understanding the objectives and requirements of the project. This has been demonstrated in this ReadMe file through the Business Requirements and ML Business Case sections above. |
| 2. Data Understanding | This phase seeks to identify, collect, and analyze the data sets. The data has been provided by the client and collected from Kaggle within the Data Collection Jupyter notebook. Analysis has been performed in the House Price Correlation Jupyter notebook, with the results presented in the House Sale Price Study page in the dashboard. |
| 3. Data Preparation | The Data Preparation phase looks to get the final data set ready for modeling. This has been performed as part of the Data Cleaning and Feature Engineering Jupyter notebooks. |
| 4. Modelling | This phase looks to build and assess various models based on several different modeling techniques. This has been performed within the Predict Price Jupyter notebook. The information on the final model presented within the ML Model Performance page in the dashboard. |
| 5. Evaluation | The Evaluation phase considers which model best meets the requirements. This is addressed in the Predict Price Jupyter notebook, where a number of algorithms and hyper parameters are considered and reviewed. The final model is also evaluated for whether it meets the business requirements. Information with the metrics on the final model are included within the ML Model Performance page in the dashboard. |
| 6. Deployment | This phase is to allow the client to see the results of the project. This has been completed through deploying the dashboard to Heroku. |


## Epics and User Stories

The project has been broken down into five epics. These have been shown below, along with the associated user stories, mapping to business requirements (see above), the planned actions, and how each story has been completed.

### Epic 1: Information gathering and data collection

| Ref | User Story | Business Requirement(s) | Actions | Completion |
| --- | --- | --- | --- | --- |
| 1.1 | As a user, I want to be able to view the data in the dashboard so that I can verify that it is correct. | 1,2 | Build a section in the dashboard where the data can be viewed by the user. | The dashboard includes the head of the dataset in the House Sale Price Study, where it can be inspected. |

### Epic 2: Data visualization, cleaning, and preparation

| Ref | User Story | Business Requirement(s) | Actions | Completion |
| --- | --- | --- | --- | --- |
| 2.1 | As a user, I want to be able to examine data visualisations so that I can discover how the house attributes correlate with the sale price. | 1 | Build a section in the dashboard where the visualisations from the sale price study can be viewed. | The House Sale Price Study page includes scatterplots to visualise the key attributes that correlate with the sale price. |

### Epic 3: Model training, optimization and validation

| Ref | User Story | Business Requirement(s) | Actions | Completion |
| --- | --- | --- | --- | --- |
| 3.1 | As a user, I want to be able to predict the sale price of the portfolio of houses that I inherited so that I can make decisions to maximise my income. | 2 | Use the ML pipeline to predict the sale price for the inherited houses. | The House Sale Price Predictor page includes the data on the inherited house portfolio, along with the model predicted sale price for each and in total. |
| 3.2 | As a user, I want to be able to predict the sale price of houses in Ames, Iowa, so that I can make decisions on future potential houses. | 2 | Build widgets into the dashboard so that a user can input the house attributes and run the model to determine a predicted sale price. | The House Sale Price Predictor page includes the ability to input house attributes to output a predicted sale price. |

### Epic 4: Dashboard planning, designing, and development

| Ref | User Story | Business Requirement(s) | Actions | Completion |
| --- | --- | --- | --- | --- |
| 4.1 | As a user, I want to be able to view a summary of the project so that I can remind myself of the project purpose. | 1,2 | Build a section of the dashboard to include a summary of information. | The dashboard includes a Project Summary page that provides the key information. |
| 4.2 | As a user, I want to be able to view information on the attribute correlations so that I can understand how variables correlate with sale price. | 1 | Build a section of the dashboard to display the results of the correlation study. | The House Sale Price Study page includes information and scatterplots to visualise the key attributes that correlate with the sale price. |
| 4.3 | As a user, I want to be able to view the predicted sale price of the inherited houses and predict any house in Ames, Iowa so that I can estimate the value of houses in the area. | 2 | Build a section of the dashboard to display the results of inputting the inherited house attributes into the model, including the total. | The House Sale Price Predictor page includes the data on the inherited house portfolio, along with the model predicted sale price for each and in total. In addition, the page includes the ability to input house attributes to output a predicted sale price. |
| 4.4 | As a user, I want to be able to view the project hypothesis and validation, so that I can understand the background to the project. | 1 | Build a section of the dashboard to clearly explain the original project hypothesis and how it has been validated. | The Hypothesis and Validation page provides information on the hypothesis made at the start of the project, and how it was validated during the project. |
| 4.5 | As a user, I want to be able to view information on the model performance so that I can understand how well the machine learning has worked. | 2 | Build a section of the dashboard to display the key metrics related to the model. | The ML Model Performance page provides information, statistics and visualisations for the ML pipeline. |

### Epic 5: Dashboard deployment and release

| Ref | User Story | Business Requirement(s) | Actions | Completion |
| --- | --- | --- | --- | --- |
| 5.1 | As a user, I want to be able to view the dashboard so that I can access all the relevant information and predict house prices. | 1,2 | Deploy the dashboard to Heroku with a publicly available URL. | The dashboard has been deployed to Heroku |

## Dashboard Design
Below is a summary of the key design elements for the dashboard.

### Page 1: Quick Project Summary

A high-level summary of the project, including:
* terms and jargon;
* information on the dataset; and
* the business/client requirements.

### Page 2: House Sale Price Study
Data analysis on the sale price, including:
* a summary of the dataset for the user to inspect, using a checkbox widget to display;
* conclusions made on the correlation study; and
* visualisations of the correlations, accessed via checkbox widgets.

### Page 3: House Sale Price Predictor
Information on predicting sale prices, including:
* information on the client's inherited properties;
* the predicted sale price of the client's inherited properties (including total); and
* the ability to input house attributes in order to predict the sale price of any house in Ames, Iowa, using input widgets.

### Page 4: Project Hypothesis and Validation
Information on the hypothesis made before undertaking the project, including:
* a summary of how the hypothesis was validated as part of the correlation study.

### Page 5: ML Model Performance
Information on the machine learning model used for the house sale price predictor, including:
* the pipeline itself;
* the most important features used to train the model; and
* pipeline performance metrics.

## Unfixed Bugs
Currently, the Twemoji of a house used as the streamlit favicon is not showing in the live (deployed) version of the dashboard, but is showing when running locally. This does not have any impact on the functionality of the dashboard, or the completion of the business requirements. The issue will be resolved in future versions.

No other unfixed bugs have been identified.

## Deployment

The App live link is: https://heritage-housing.herokuapp.com/

The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
The following libraries were used in the development of this project:
* [NumPy](https://numpy.org/): support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these arrays. Used for the arrays used when displaying heatmaps in the correlation study.
* [Pandas](https://pandas.pydata.org/): data manipulation and analysis. Used for the dataframes in the price predictor and model performance pages.
* [MatPlotLib](https://matplotlib.org/): plotting library for Python and NumPy. Used to plot the charts in the correlation study and model performance pages.
* [Seaborn](https://seaborn.pydata.org/): a library that uses Matplotlib underneath to plot graphs. Used to plot the charts in the correlation study.
* [Pandas Profiling](https://pypi.org/project/pandas-profiling/): provides one-line Exploratory Data Analysis (EDA). Used in the Jupyter notebooks to examine the dataset and provide insights.
* [PPS Score](https://github.com/8080labs/ppscore): a data-type-agnostic score that can detect linear or non-linear relationships between two columns. Used in the correlation study to determine which variables have relationships with the target variable.
* [Streamlit](https://streamlit.io/): an app framework for ML dashboards. Used for the dashboarding for this project.
* [Feature Engine](https://feature-engine.readthedocs.io/en/latest/): a library with transformers to engineer and select features to use in machine learning models. Used for data cleaning and data transformation in the Feature Engineering Jupyter notebook.


## Credits 

### Content 

- Various custom functions and code have been taken from the Code Institute Churnometer Walkthrough Project, and have been referenced as such when used in the relevant Jupyter notebooks.
- The template for the project (including the ReadMe) has been taken from the Code Institute project handbook.

### Media

- The page icon has been take from [Twemoji](https://twemoji.twitter.com/).


## Acknowledgements
Grateful thanks to the following:
* The Code Institute students for their assistance on Slack.
* My partner, Scott, for his continued support throughout the process.

