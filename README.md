# Diabetes_Prediction - Team Project 4

<img width="632" alt="Screenshot 2023-04-13 at 7 03 57 PM" src="https://user-images.githubusercontent.com/106120403/231901475-2b87a3eb-d90d-414c-8e99-1ed37a0095bf.png">

## Team Members: 
    Tanya Qader
    Oseremeh Okpamen
    Michelle Carvalho
    Mojtaba Zadaskar 
  
  

# Introduction											
As one of the most common diseases in the world, diabetes mellitus affects 37.3 million Americans in 2019 or 11.3% of the country’s population. The proportion of diabetes-related deaths in the US is estimated to be between 11.5% and 12%. Diabetes was diagnosed in 537 million individuals globally in 2021; by 2045, that figure is projected to rise to 783 million. Diabetes also has a significant economic impact, with estimated annual expenditures for direct costs relating to diabetes increasing from $966 billion in 2021 to a projected value in excess of over $1 trillion in 2045. In the US, spending on diabetes care and management makes up roughly 25% of all healthcare spending. The effective management of diabetes is crucial to prevent additional complications, such as eye, foot, and mouth problems, kidney disease and even certain cancers. Additionally, it is also estimated that half of all people affected by diabetes are undiagnosed. Like other diseases, one of the best ways to effectively manage diabetes lies in diagnosing the disease early before the effects become more serious.{1}

Diabetes is usually diagnosed in one of two ways – in the more traditional way involving manual diagnosis by health practitioners – or by technology. Each of these methods has distinct advantages and disadvantages. While it is true that manual diagnosis by health practitioners allows for human expert insight, advances in technology have made this approach much more effective as time goes on and is becoming the preferred approach. Another advantage of technological approaches is that they require less time and resources to employ. Additionally, in the initial stages of the disease, indicators of diabetes can be easier to identify through technology than by manual examinations while eliminating human errors and complications in the initial analysis stages. As the availability of electronic health record data continues to increase, it becomes more attractive to utilize automated diabetes diagnosis systems. In particular, artificial intelligence (AI) and machine learning (ML) approaches are the two main ways automated diabetes diagnosis systems can be built.{1}

Every year since 1984, the CDC has conducted a detailed survey on people’s health and what they're doing about it. The CDC's Behavioral Risk Factor Surveillance System (BRFSS) provides a wealth of information about health and health-related behaviours in the United States. It is the largest and longest-running health survey system in the world, and in its current incarnation, it covers over 400,000 adult interviews from all 50 states, the District of Columbia, and three territories. For more information about the survey itself, you can visit the CDC BRFSS site.{2}

The BRFSS is a rich source of information on how demographics, behaviours, and other risk factors can correlate with health. Many important population health studies and measures use the BRFSS as a key data source. For example, it is the source of the CDC's "Healthy Days" measurement, a key performance metric for the healthcare industry.{2}

Unfortunately, BRFSS data isn't exactly easy to deal with. Its breadth and structure have changed considerably over the years, and there are important sampling considerations that must be taken into account when using the data to draw conclusions. 

The goal of this project is to demonstrate how to use BRFSS data and some of the interesting correlations and associations that can be drawn from this data set using machine learning and statistical techniques to develop a machine learning model to predict a diagnosis of diabetes.

In today’s world, it is important to understand your overall health and be able to make predictions about health issues such as diabetes, high blood pressure, and cholesterol levels. We will be using Machine Learning to predict whether an individual has diabetes or not have diabetes. We will use information such as the person’s age, BMI, activity levels etc.

### Dataset
In 1984, the Centers for Disease Control and Prevention (CDC) initiated the state-based Behavioral Risk Factor Surveillance System (BRFSS) a cross-sectional telephone survey that state health departments conduct monthly over landline telephones and cellular telephones with a standardized questionnaire and technical and methodologic assistance from CDC. BRFSS is used to collect prevalence data among adult U.S. residents regarding their risk behaviors and preventive health practices that can affect their health status. Respondent data are forwarded to CDC to be aggregated for each state, returned with standard tabulations, and published at year’s end by each state. In 2011, more than 500,000 interviews were conducted in the states, the District of Columbia, and participating U.S. territories and other geographic areas.

Identifying a suitable dataset is important for constructing an effective classifier. Therefore, to accurately predict diabetes, the dataset was obtained from BRFSS, which provided sufficient data samples and attributes for training purposes.

2021 BRFSS Dataset: https://www.cdc.gov/brfss/annual_data/annual_2021.html

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

After reading in our CSV file, we set about exploring our dataset before laungching manchine learning.  Visualizing a correlation of our narrowed features with diabetes, we made the decision to drop "Afford Costs" given that it showed to be a very weak correlator.
<img width="765" alt="Screenshot 2023-04-16 at 8 21 45 PM" src="https://user-images.githubusercontent.com/115101031/232352373-fd46ff63-05d2-4fa1-9438-d3d171120f03.png">

Reviewing histograms of each feature showed that the data was not normally distributed.
<img width="803" alt="Screenshot 2023-04-16 at 8 24 46 PM" src="https://user-images.githubusercontent.com/115101031/232352563-39e0cff8-c0b0-4674-a3d7-56be29478964.png">

This was confirmed by also reviewing the skewness of our data (df.skew).  As such, we needed to consider options to scale our data prior to runnung our maching learning models.  Data scaling is a method for reducing the effect of data bias on predictions which is highly used in pre-processing step in any Machine Learning project. It can be applied to any type of prediction model.  We focussed our options on three of the most popular scalers.

***StandardScaler*** is a fast and specialized algorithm for scaling data. It calculates the mean and standard deviation of the data set and normalizes it by subtracting the mean and dividing by standard deviation. Using StandardScaler is a common practice in ML projects if the data set follows a normal distribution.  

***MinMaxScaler*** is a simple and effective linear scaling function. It scales the data set between 0 and 1. In other words, the minimum and maximum values in the scaled data set are 0 and 1 respectively. MinMax Scaler is often used as an alternative to Standard Scaler if zero mean and unit variance want to be avoided. 

***RobustScaler*** is a technique that uses median and quartiles to tackle the biases rooting from outliers. Instead of removing mean, RobustScaler removes median and scales the data according to the quantile range aka IQR: Interquartile Range.

<img width="436" alt="Screenshot 2023-04-16 at 8 30 22 PM" src="https://user-images.githubusercontent.com/115101031/232352866-ebd1a015-d2ec-4a1d-8dce-6dc708c51b28.png">

A comparison of all three scalers with a copy of our DataFrame, swayed the choice towards the MinMaxScaler as it will likely best address a dataset that is not normally distributed/skewed.

<img width="217" alt="Screenshot 2023-04-16 at 8 30 32 PM" src="https://user-images.githubusercontent.com/115101031/232352874-e9ca8683-25a6-4334-80b7-4e36c148bae3.png">


We initiated our machine learning with Logistic Regression, Decision Tree, KNN and Random Forest.

***Logistic Regression***: Logistic regression is an example of supervised learning. It is used to calculate or predict the probability of a binary (yes/no) event occurring.


<img width="425" alt="Screenshot 2023-04-16 at 8 38 18 PM" src="https://user-images.githubusercontent.com/115101031/232353369-3a56386b-cc24-4462-8eae-ae48e886a3c0.png">


While the precision, recall and f1-score are high for healthy individuals, those for individuals with diabetes are less than ideal.  Though the model accuracy is high (87%), it may be highly influenced by the fact that healthy individuals outnumber those with diabetes.  As a result, the false negatives (individuals misdiagnosed as healthy = 850) is unacceptably high.

***K Nearest Neighbors***: The k-nearest neighbors algorithm, also known as KNN or k-NN, is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point.

<img width="424" alt="Screenshot 2023-04-16 at 9 17 58 PM" src="https://user-images.githubusercontent.com/115101031/232356367-18755260-cbda-4379-9076-fac48118c72d.png">

KNN did not provide improvement in our accuracy or prediction of diabetes.  In fact, it did worse in generating significantly more false negatives (6803)!

***Decision Tree***: A decision tree can be used to visually and explicitly represent decisions and decision making. As the name goes, it uses a tree-like model of decisions. It makes predictions based on how a previous set of questions were answered.

<img width="419" alt="Screenshot 2023-04-16 at 9 19 33 PM" src="https://user-images.githubusercontent.com/115101031/232356515-48c26e28-9be4-4c1c-9a77-6beaa07f23fd.png">

Our accuracy, precision, recall and f1-score are consistent with the prior models.  While precision and recall and f1-scores are better at predicting diabetes, the high number of false negatives is still abysmally high.

***Random Forest***: One of the most popular and commonly used algorithms by Data Scientists. Random forest is a Supervised Machine Learning Algorithm that is used widely in Classification and Regression problems. It builds decision trees on different samples and takes their majority vote for classification and average in case of regression. One of the most important features of the Random Forest Algorithm is that it can handle the data set containing continuous variables, as in the case of regression, and categorical variables, as in the case of classification. It performs better for classification and regression tasks. 

<img width="422" alt="Screenshot 2023-04-16 at 10 52 58 PM" src="https://user-images.githubusercontent.com/115101031/232367412-79668a4d-1e77-49da-b779-b64687ce2d03.png">

Random Forest provides a consistent result with earlier models, but does offer a slightly improved/reduced false negatives.

# Visualzations 
####  Tableau for visualization 
      Used several indictors to compare the difference between the Diabetes and No Diabetes,
      
      Indicators are :
      1. Drink
      
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/Drink%20VsDiabetes.png">

      2. Gender 
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/GenderVs%20Diabetes.png">

      3. Ethnicity
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/EthnicityVsDiabetes.png">
      
      4. Kidney and Lung Disease
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/Kidney%20%26%20Lung%20Vs%20Diabetes.png">      
      
      5. Heart Problems
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/Heart%20Disease%26heart%20AttackVs%20Diabetes.png">

      6. Income
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/IncomeVs%20Diabetes.png">
      
      7. Pyhsical Activity
      8. Exercise 30 days 
     

 ## Tableau Public Link:
 
* https://public.tableau.com/views/Project4-dataset2021/Diabetes?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link

 # Dashboard 
 #### streamLit
      
      Used stream lit to create a dashboard , with the use of ML and based on the questions that the client will respond ,
      the system could predict, is he/she diabetes or no diabetes.

   First screenshot:
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/dashboard%20picture.PNG">

   Second screenshot:
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/dashboard%20picture2.PNG">

    Third screenshot:
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/dashboard%20picture3.PNG">


    Fourth screenshot:
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/dashboard%20picture4.PNG">


    Fifth  screenshot:
<img width="600" alt="Drink Vs Diabetes" src="https://github.com/Tanya-Qader/Diabetes_Prediction/blob/Mojtaba/Images/dashboard%20picture5.PNG">



The dashboard allows users to input data such as race/ethnicity, physical activity, high blood pressure, gender, age, income,smoker, and whether the person is overweight or obese. Based on this input, the model predicts the likelihood of the person having diabetes, which is then displayed on the dashboard.


## Conclusions:

* Our dataset is subjective and compromises an extensive set of features, not all necessarily related to our project scope.  Based on surveys, the dataset reflects individuals perceptions, recollections, and often their reluctance to share personal informaiton.  While it provided a good dataset to work with, we recognzed that if we were to tackle the project in real-life, working with scientific data or standardized medical records/data would provide a more reliable and consistent dataset for us to predict diabetes using machine learning. This would also mean that instead of relying on a all-emcompassing dataset that may or may not include data relevant to predicting diabetes, a standardized dataset using medical records and professional diagnistics from health professionals, would ensure that our data reflected current medical guidelines for assessment of diabetes.

* What was interesting in using our dataset was the way in which we could visualize a correlation between other heath issues.  For example, find that a High BP correlated to heart conditions.  Or a lack of activity correlating to difficulty walking.  We were also surprised by the correlation between income and a diabetes diagnosis, which made us think about factors that might impact a person's likelihood to be diagnosed that were not directly medical in nature.  For example, people with low incomes are more likely to be burdened by illness-related treatment because income and diabetes have a strong link. 

* A key focus in our project was in understanding the nature of our data and the type of tools that would suit our analysis.  For example, understanding that our dataset was not normally distributed helped us make decisions about which feature engineering tools to use.  Equally, understanding that our dataset had a high number of null values or non-responses pushed us to carefully consider how we might treat these variables so that we did not eliminate large swathes of useful data, or that we did not unnecessarily bias our results.  Working with binary and ordinal data also informed our choices when scaling our dataset and our decisions around which machine learning models might works best.

* Our dashboard is created by _Streamlit_ which provided a useful and interactive means to combine our machine learning with user input to test the likelihood of a person having diabetes based on several key factors. By using logistic regression, we can achieve a high degree of accuracy in our predictions. Overall, this tool can be very useful in the healthcare industry and can potentially help identify individuals who are at risk for diabetes. However, in our case the streamlit app is not publicly published, therefore the dashboard will only open if the local port is connected. In order to publish the app, we need a web hosting or AWS to host the web and make is accessible for everyone. 

* We were able to see the high value that machine learning and interactive tools like a dashboard can offer both the patient and health professionals in both diagnosing, but also recommending preventative and disease management care.

  
# Additional Supporting Content

***Link to Tableau to further show the relationship between Diabetes and the features***
* https://public.tableau.com/views/Project4-dataset2021/Diabetes?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link

***Link to the Project Presentation PowerPoint***
* https://docs.google.com/presentation/d/1f4IErv21VkdBfn4Hmy-l7u7yjIzmLlKGUOm07Lc417k/edit#slide=id.g11d335f8426_1_172

***Link to the Dashboard***
* Since we didnt publish this app publicly, this link will only open if the local machine with the local port number is connected to run this app. 

* https://tanya-qader.github.io/diabetes_page/

***Knowledgebase - Additional Sources***
* https://www.sciencedirect.com/science/article/pii/S2772442522000582#da1 {1}
* https://www.cdc.gov/pcd/issues/2019/19_0109.htm {2}
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9018179/
* https://www.researchgate.net/publication/366621858_Risk_Factor_Analysis_Associated_with_BRFSS_dataset
