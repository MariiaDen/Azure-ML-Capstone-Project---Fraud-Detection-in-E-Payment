# E-Commerce Payment Fraud Detection

The world is getting more digitalized, and so do payments. Fraud in commerce is called "payment fraud" and is defined as any type of illegal or false transaction. The profit can be money, goods or even sensitive information. Since COVID-19 e-payment transactions amount has risen. According to the [Sift insights](https://blog.sift.com/2020/where-does-fraud-go-from-here-how-coronavirus/), the education space, travel and transportation are the most hot targets in this year. 

<p align="center">
  <img src="https://blog.sift.com/wp-content/uploads/2020/07/COVID-graphic-768x362.png">
</p>

There are several tools on the market that are used to detect payment frauds, and all of them use artificial intelligence to do so. In this project there is an attempt to analyze a dataset and determine how well can fraudulent actions be recognized. 

## Dataset
When it comes to financial information, it is almost impossible to get data to perform research. After searching for information online, one dataset has been found. 

### Overview
The dataset contains transactions made by credit cards in September 2013 by european cardholders. The dataset contains anonymized credit card transactions labeled as fraudulent or genuine. The data has gone through a PCA transformation and therefore contains only numerical data. The data contains 32 columns which have been renamed as V1, V2, ... V28. The dataset can be found [here](https://www.kaggle.com/mlg-ulb/creditcardfraud).

The data is very unbalanced, as any dataset with fraud occurences. Data used in fraud detection in banking, real-time bidding in marketing or intrusion detection in networks [often have less than 1%](https://www.kdnuggets.com/2017/06/7-techniques-handle-imbalanced-data.html) of rare, but “interesting” events. There are multple ways to handle this problem. One of them is resampling - selecting equal amount of data for both classes - genuine and fraudulent transactions. Alternatively, the usage of ensembling methods is recommended.

### Task
Though it will be impossible to say which features play the biggest role in payment fraud detection since data is highly anonymized, but it still will be interesting to see which methods work the best, and whether there are some more distinctive features that determine the outcome. These learnings can be then used for the less anonymized data, when it gets accessible. 

### Access
Since this is a kaggle dataset, the data has been downloaded as a csv file and uploaded to the ML Azure environment. 

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
