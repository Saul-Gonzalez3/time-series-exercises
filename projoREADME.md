# <a name="top"></a>Life, Liberty, and the Pursuit of Freedom from Credit Card Fraud

by Saul Gonzalez


> *The challenge for capitalism is that the things that breed trust also breed the environment for fraud.*
> > *James Surowiecki
 

[Project Plan](#Project_Plan) | [Data Dictionary](#Data_Dictionary) | [Conclusions](#Conclusions) | [Next Steps](#Next_Steps) | [Recommendations](#Recommendations) | [Steps to Reproduce Our Work](#Steps_to_Reproduce_Our_Work)|


<b>Project Description</b>:  

This project contains the findings of research derived from the utilization of machine learning modeling using regression modeling to determine the highest drivers, or indicators that help predict credit card fraud.
    

<b>Project Goal</b>:  Predict credit card fraud while incorporating unsupervised machine learning learning techniques that can consistently and accurately detect potentially fraudulent transactions on unseen data.


Preliminary Questions:

1. Are any of the features correlated? 

2. Does <b>device_os</b> show a liability for credit card fraud due to the percentage of fraud attributed to they type of device_os?

3. Does <b>zip_count_4w</b> show a trend of credit card fraud attributed to specific locations?

4. Classification or regression? Should I do both for a comparison given the time I have to work on this?

5. Are all input variables relevant? Which ones are <b>MOST</b> relevant? 


<a name="Project Plan"></a><b>Project Plan</b>:

1. Create all the files needed to make a functioning project (.py and .ipynb files).

2. Create a .gitignore file and ignore the env.py file.

3. Start by acquiring data from [Kaggle Bank Account Fraud Dataset Suite](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022) dataset and document all my initial acquisition steps in the acquire.py file.

4. Using the prepare file, clean the data and split it into train, validatate, and test sets.

5. Explore the data. (Focus on the main main questions). Experiment with various feature combinations and clustering to gain insight, if some is found, to support hypothesis testing.

6. Answer all the questions with statistical testing.

7. Identify drivers of credit card fraud. Make prediction of credit card fraud using driving features found during exploration and statistical testing.

8. Document findings.

9. Add important finding to the final notebook.

10. Create csv file of test predictions on best performing model.

[[Back to top](#top)]


<a name="Data Dictionary"></a><b>Data Dictionary</b>:
These variables were based on physicochemical tests. Physicochemical tests are: tests that evaluate the materials of the container component or system to ensure purity and the absence of harmful contaminants or residuals from the manufacturing process.
|**Input Variables**|**Description**|
|----------|----------------|
|Fixed fraud_bool| Fraud label (1 if fraud, 0 if legit).|
|Income | Annual income of the applicant in quantiles. Ranges between [0, 1]. |
| name_email_similarity | Metric of similarity between email and applicant’s name. Higher values represent higher similarity. Ranges between [0, 1].|
| prev_address_months_count | Number of months in previous registered address of the applicant, i.e. the applicant’s previous residence, if applicable. Ranges between [−1, 380] months (-1 is a missing value). |
| current_address_months_count | Months in currently registered address of the applicant. Ranges between [−1, 406] months (-1 is a missing value).|
| customer_age | Applicant’s age in bins per decade (e.g, 20-29 is represented as 20). |
| days_since_request | Number of days passed since application was done. Ranges between [0, 78] days. |
| intended_balcon_amount | Initial transferred amount for application. Ranges between [−1, 108]. |
| payment_type | Credit payment plan type. 5 possible (annonymized) values. |
| zip_count_4w | Number of applications within same zip code in last 4 weeks. Ranges between [1, 5767]. |

[[Back to top](#top)]



<a name="Conclusions"></a><b>Conclusions</b>:

After acquiring & preparing the data, I conducted uni/bi/multi-variate exploration on the wine data to look at features and how they might impact the target 'quality'.

We paired various features together and used clustering to observe potential relationships between the features.
     
The results of our data exploration culminated in the resulting clusters and features being selected to go into regression modeling:

- Wine Color
- Chlorides
- Clustering of Alcohol and Sulphates
- Clustering of Citric Acid and pH
- Clustering of Free Sulfur Dioxide and Total Sulfur Dioxide
- Volatile Acidity and Density

I chose to go with regression modeling due to all of our features being continuous. 

I used the following regression models:
- Ordinary Least Squares (OLS)
- LassoLars
- Generalized Linear Model (GLM)

I found that our Ordinary Least Squares model was the best performing model, showcasing a 12% average model prediction error on unseen data.
    
[[Back to top](#top)]
    

    
<a name="Next Steps"></a><b>Next Steps</b>:

- I would look at conducting this entire study without the use of clustering, using the same models, to compare results and observe the impact of clustering to the modeling results.

- Furthermore, additional study on features for both red and white wines 'individually', given sufficient time, could prove insightful in determining the best drivers of quality for each colored wine.
    
- Lastly, if there happens to be additional data that becomes available, it could prove useful as there are likely other outside features that contribute to wine quality (grape quality, climate grapes grown, fermentation process, etc.) that could be stronger drivers of quality not provided by our current data source.
    
[[Back to top](#top)]
    

    
<a name="Recommendations"></a><b>Recommendations</b>:  

- The data source showed a larger percentage of white wines produced compared to red wines, which could have produced a bias in the data that skewed the data. The data could be reduced to even out the differences between red and wines. 
    
- There could be an issue with oxidation in the wines. The lower quality wines have lower amounts of sulphates, and we think that by increasing the amount of sulphates, the oxidation issues would be remedied and improve the quality of wines. 
        
- Higher alcohol content is a major factor in the higher quality wines, specifically white wines. A two-fold effort can be enacted to maximize marketing towards white wine (where high quality is aplenty) and to chemically increase the alcohol while balancing the acidity to sufficiently improve quality in the red wines. 
    
[[Back to top](#top)]
    

    
<a name="Steps to Reproduce Our Work"></a><b>Steps to Reproduce Our Work</b>:

1. Clone this repo.

2. Acquire the wine data from the Data.World Wine Quality Dataset.

3. Put the data in the file containing the cloned repo.

4. Run your notebook.
    
[[Back to top](#top)]

