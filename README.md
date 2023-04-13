# Diabetes Prediction with Machine Learning

<img width="632" alt="Screenshot 2023-04-13 at 7 03 57 PM" src="https://user-images.githubusercontent.com/106120403/231901475-2b87a3eb-d90d-414c-8e99-1ed37a0095bf.png">

# Introduction											
Every year since 1984, the CDC has conducted a detailed survey on people’s health and what they're doing about it. The CDC's Behavioral Risk Factor Surveillance System (BRFSS) provides a wealth of information about health and health-related behaviours in the United States. It is the largest and longest-running health survey system in the world, and in its current incarnation, it covers over 400,000 adult interviews from all 50 states, the District of Columbia, and three territories. For more information about the survey itself, you can visit the CDC BRFSS site.

The BRFSS is a rich source of information on how demographics, behaviours, and other risk factors can correlate with health. Many important population health studies and measures use the BRFSS as a key data source. For example, it is the source of the CDC's "Healthy Days" measurement, a key performance metric for the healthcare industry.

Unfortunately, BRFSS data isn't exactly easy to deal with. Its breadth and structure have changed considerably over the years, and there are important sampling considerations that must be taken into account when using the data to draw conclusions. 

The goal of this project is to demonstrate how to use BRFSS data and some of the interesting correlations and associations that can be drawn from this data set using machine learning and statistical techniques to develop a machine learning model to predict a diagnosis of diabetes.

In today’s world, it is important to understand your overall health and be able to make predictions about health issues such as diabetes, high blood pressure, and cholesterol levels. We will be using Machine Learning to predict whether an individual has diabetes or not have diabetes. We will use information such as the person’s age, BMI, activity levels etc.

### Dataset
https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

### Research Questions:

1. Can the machine learning model accurately predict diabetes, pre-diabetes, and non-diabetes, and what factors contribute to this accuracy?
2. Can our machine learning model be trained on a small subset of clinical data to accurately predict diabetes, pre-diabetes, and non-diabetes in a larger population, and how does its performance compare to models trained on larger datasets?
3. Can specific subgroups within the population (e.g., age, BMI, physical activity, etc.) be identified and addressed in order to improve the model's performance overall?
4. Can the machine learning model be used to identify potential risk factors for diabetes and pre-diabetes, and how can this information be used to improve clinical interventions and patient outcomes?

# ETL
#### Getting BRFSS data												
To get started, we downloaded the data from the BRFSS Annual Survey Data page, choosing the most recent data set from 2021. The data is available in .XPT (SAS Transport Format) or in .ASCII files.   

#### Cleaning BRFSS data											
After reading the SAS file and creating our DataFrame, we note that the BRFSS data is not useful right out of the box. We have to do some heavy-duty cleaning.  The 2021 data set includes 438693 rows and 303 columns.  

# Feature Engineering										
Producing accurate predictions is the goal of a machine learning algorithm, and feature engineering ties it all together. Feature engineering includes everything from filling in missing values to variable transformation to building new variables from existing ones.

A review of the data shows a significant number of null values in several columns.  The reality is that real-world data is rarely clean and homogeneous. In particular, many interesting datasets will have some amount of data missing.  The first part of feature engineering is handling missing values.

The simplest option is removing any rows or columns with missing values.  Removing any rows with null values would essentially eliminate the entire data set.  Removing columns with null values reduces our data set from 303 columns to less than 30!   More importantly, removing such a significant proportion of our dataset may result in a biased model that will lead to incorrect results, reduced accuracy, and less predictive precision. 

There are mainly three types of missing values: 

MCAR (Missing Completly At Random): A variable is missing completely at random if the probability of being missing is the same for all the observations. MCAR data means there is absolutely no relationship between the data missing and any other observed or missing value in the dataset. In other words, those missing data points are a random subset of the dataset.
MNAR (Missing Data Not At Random): As the name suggests, there will be some relationship between the data missing and any other value in the dataset.
MAR(Missing At Random): Missing at Random means the propensity for a data point to be missing is not related to the missing data, but it is related to some of the observed data

Our missing values are of the MCAR type, which is typical of survey results.  Random Sample Imputation is used when data are MCAR. In this technique, NaN values are replaced by a random value (ie. mean, median, mode) selected from that column.  The advantages of using Random Sample imputation include that it is easy to implement and there is less resulting distortion in variance.  The main disadvantage is that there may be some situations randomness won't work.  However, in the case of our dataset, it is likely the most appropriate option. A common method of random sample imputation with numeric features is to replace missing values with the median of the feature’s non-missing values. 

# Link to Tableau to further show the relationship between Diabetes and the features

https://public.tableau.com/app/profile/mojtaba.zadaskar/viz/shared/W3CCWYNDB

# Machine Learning


# Link to the Project Presentation PowerPoint


# Link to the Dashboard



