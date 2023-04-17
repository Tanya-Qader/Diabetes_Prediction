# Diabetes Prediction with Machine Learning

<img width="632" alt="Screenshot 2023-04-13 at 7 03 57 PM" src="https://user-images.githubusercontent.com/106120403/231901475-2b87a3eb-d90d-414c-8e99-1ed37a0095bf.png">

# Introduction											
Every year since 1984, the CDC has conducted a detailed survey on people’s health and what they're doing about it. The CDC's Behavioral Risk Factor Surveillance System (BRFSS) provides a wealth of information about health and health-related behaviours in the United States. It is the largest and longest-running health survey system in the world, and in its current incarnation, it covers over 400,000 adult interviews from all 50 states, the District of Columbia, and three territories. For more information about the survey itself, you can visit the CDC BRFSS site.

The BRFSS is a rich source of information on how demographics, behaviours, and other risk factors can correlate with health. Many important population health studies and measures use the BRFSS as a key data source. For example, it is the source of the CDC's "Healthy Days" measurement, a key performance metric for the healthcare industry.

Unfortunately, BRFSS data isn't exactly easy to deal with. Its breadth and structure have changed considerably over the years, and there are important sampling considerations that must be taken into account when using the data to draw conclusions. 

The goal of this project is to demonstrate how to use BRFSS data and some of the interesting correlations and associations that can be drawn from this data set using machine learning and statistical techniques to develop a machine learning model to predict a diagnosis of diabetes.

In today’s world, it is important to understand your overall health and be able to make predictions about health issues such as diabetes, high blood pressure, and cholesterol levels. We will be using Machine Learning to predict whether an individual has diabetes or not have diabetes. We will use information such as the person’s age, BMI, activity levels etc.

### Dataset
https://www.cdc.gov/brfss/annual_data/annual_2021.html

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

#### Feature Engineering										
Producing accurate predictions is the goal of a machine learning algorithm, and feature engineering ties it all together. Feature engineering includes everything from filling in missing values to variable transformation to building new variables from existing ones.

A review of the data shows a significant number of null values in several columns.  The reality is that real-world data is rarely clean and homogeneous. In particular, many interesting datasets will have some amount of data missing.  The first part of feature engineering is handling missing values.

The simplest option is removing any rows or columns with missing values.  Removing any rows with null values would essentially eliminate the entire data set.  Removing columns with null values reduces our data set from 303 columns to less than 30!   More importantly, removing such a significant proportion of our dataset may result in a biased model that will lead to incorrect results, reduced accuracy, and less predictive precision. 

There are mainly three types of missing values: 

MCAR (Missing Completly At Random): A variable is missing completely at random if the probability of being missing is the same for all the observations. MCAR data means there is absolutely no relationship between the data missing and any other observed or missing value in the dataset. In other words, those missing data points are a random subset of the dataset.
MNAR (Missing Data Not At Random): As the name suggests, there will be some relationship between the data missing and any other value in the dataset.
MAR(Missing At Random): Missing at Random means the propensity for a data point to be missing is not related to the missing data, but it is related to some of the observed data

Our missing values are of the MCAR type, which is typical of survey results.  Random Sample Imputation is used when data are MCAR. In this technique, NaN values are replaced by a random value (ie. mean, median, mode) selected from that column.  The advantages of using Random Sample imputation include that it is easy to implement and there is less resulting distortion in variance.  The main disadvantage is that there may be some situations randomness won't work.  However, in the case of our dataset, it is likely the most appropriate option. A common method of random sample imputation with numeric features is to replace missing values with the median of the feature’s non-missing values. 

We eliminated data where the survey had only partially completed, thus eliminating a source of bias in our data. We then cleaned our dataset to ensure that our data was consistent.  For example, we removed data where the the individual was unresponsive to the question being asked.  Our data was largely binary, with some ordinal features.  In some cases the binary classes were inconsistent, so we updated the classifiers to ensure they were consistent.  We then renamed the columns to make them more readable.  Finally, we exported the final DataFrame to a CSV file to conduct the remainder of our Feature Engineering.

Using established research, we will narrow the available 303 indicators to reflect features that are known indicators for diabetes.  We reduced our dataset from 303 columns to 27, focussing on the following indicators: 
<img width="560" alt="Screenshot 2023-04-16 at 7 44 45 PM" src="https://user-images.githubusercontent.com/115101031/232350068-e251a2c4-15d8-4268-ab4c-ca45cc7bf89c.png">


#### Feature Selection
After reading in our CSV file, we visualized distribution plots for each our our features.  Visualization of the distribution/density of each variable in our dataset provides a clear way to understand the balance of our data.  For example, the accuracy of our predictions may be skewed simply if the model is making predictions on the largest class in our dataset.  This may dictate which model optimizers would be best suited to our dataset, as well as whether we want to employ any resampling strategies.
<img width="583" alt="Screenshot 2023-04-16 at 7 47 44 PM" src="https://user-images.githubusercontent.com/115101031/232350362-d717a307-1d4d-4b59-abb6-41558d52fc5a.png">

Our goal was to define those features which would work best in training our models and improving our ability to predict whether an individual had diabetes or not.

***Univariate Selection*** - Statistical tests can be used to select those features that have the strongest relationship with the output variable. The scikit-learn library provides the SelectKBest class that can be used with a suite of different statistical tests to select a specific number of features. Using the chi-squared (chi²) statistical test for non-negative features to select 10 of the best features gives us a good sense of which features may provide the strongest predictive outcome.
<img width="250" alt="Screenshot 2023-04-16 at 7 51 57 PM" src="https://user-images.githubusercontent.com/115101031/232350528-0c8e52a2-84d0-4d4e-941b-a74d34f3d938.png">

***Feature Importance*** - You can get the feature importance of each feature of your dataset by using the feature importance property of the model. Feature importance gives you a score for each feature of your data, the higher the score more important or relevant the feature is to your output variable. Feature importance is an inbuilt class that comes with Tree-Based Classifiers, we will be using Extra Tree Classifier for extracting the top 10 features for the dataset.
<img width="553" alt="Screenshot 2023-04-16 at 7 53 04 PM" src="https://user-images.githubusercontent.com/115101031/232350589-c0935f42-9d2b-4ddd-93d2-8b8adedc1c88.png">

***Correlation Matrix with Heatmap*** - Correlation states how the features are related to each other or the target variable. Correlation can be positive (an increase in one value of a feature increases the value of the target variable) or negative (an increase in one value of the feature decreases the value of the target variable).  Heatmap makes it easy to identify which features are most related to the target variable, we will plot a heatmap of correlated features using the Seaborn library.
<img width="582" alt="Screenshot 2023-04-16 at 7 54 02 PM" src="https://user-images.githubusercontent.com/115101031/232350660-5df4f5c0-bea4-461d-96cb-9d648c3ddc1f.png">

***Recursive Feature Elimination*** - Recursive Feature Elimination (or RFE) works by recursively removing attributes and building a model on those attributes that remain. It uses the model accuracy to identify which attributes (and combination of attributes) contribute the most to predicting the target attribute. You can learn more about the RFE class in the scikit-learn documentation. The example below uses RFE with the logistic regression algorithm to select the top 3 features. The choice of algorithm does not matter too much as long as it is skillful and consistent.  Recursive Feature Elimination fits a model that starts with all the input variables, then iteratively removes those with the weakest relationship with the output until the desired number of features is reached. It actually fits a model instead of just running statistical tests, unlike Univariate Testing. RFE is popular because it is easy to configure and use and because it is effective at selecting those features in a training dataset that are more or most relevant in predicting the target variable. 

***Recursive Feature Elimination with Cross-Validation (RFECV)*** -  The CV in RFECV means Cross-Validation. It gives you a better understanding of what variables will be included in your model. The Cross-Validation part splits the data into different chunks and iteratively trains and validates models on each chunk separately. This simply means that each time you assess different models with certain variables included or eliminated, the algorithm also knows how accurate each model was from the model scenarios that are created and can determine which provided the best accuracy and concludes the best set of input variables to use.
<img width="504" alt="Screenshot 2023-04-16 at 7 58 24 PM" src="https://user-images.githubusercontent.com/115101031/232350938-bf2631af-b97f-45d5-9c7d-d7304b3faf28.png">

***Principal Component Analysis*** - Principal Component Analysis (or PCA) uses linear algebra to transform the dataset into a compressed form. Generally, this is called a data reduction technique. A property of PCA is that you can choose the number of dimensions or principal components in the transformed result. In the example below, we use PCA and select 2 principal components. 

***Ridge Regression*** - One of the most important things about ridge regression is that without wasting any information about predictions, it tries to determine variables with zero effects. Ridge regression is popular because it uses regularization for making predictions, and regularization is intended to resolve the problem of overfitting. Ridge regression can also help us in feature selection to find out the important features required for modelling purposes.  We can consider ridge regression as a way or method to estimate the coefficient of multiple regression models.  We mainly find the requirement of ridge regression where variables in data are highly correlated. We can also think of ridge regression as a possible solution to the imprecision of LSE(least square estimator) where the independent variables of any linear regression model are highly correlated.

# Machine Learning




# Additional Supporting Content

***Link to Tableau to further show the relationship between Diabetes and the features***
* https://public.tableau.com/app/profile/mojtaba.zadaskar/viz/shared/W3CCWYNDB

***Link to the Project Presentation PowerPoint***
* https://docs.google.com/presentation/d/1f4IErv21VkdBfn4Hmy-l7u7yjIzmLlKGUOm07Lc417k/edit#slide=id.g11d335f8426_1_172

***Link to the Dashboard***
* https://tanya-qader.github.io/diabetes_page/

***Knowledgebase - Additional Sources***
* https://www.cdc.gov/pcd/issues/2019/19_0109.htm
* https://www.sciencedirect.com/science/article/pii/S2772442522000582#da1
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9018179/
* https://www.researchgate.net/publication/366621858_Risk_Factor_Analysis_Associated_with_BRFSS_dataset
* https://www.sciencedirect.com/topics/engineering/confusion-matrix#:~:text=A%20confusion%20matrix%20is%20a,malignant%20tissue%20is%20considered%20cancerous

