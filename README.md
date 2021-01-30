https://drive.google.com/file/d/1kYWbQPcjMp4z8cTCW0_ShrDLZsaOIy2u/view?usp=sharing
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

The project is split into multiple steps: 

<p align="center">
  <img src="capstone-diagram.png" height="300">
</p>

We will be training model using Automated ML and HyperDrive. The results will be compared and the best model deployed. 
At the final step we will test the model endpoint. 

### Access
Since this is a kaggle dataset, the data has been downloaded as a csv file and uploaded to the ML Azure environment. 
The csv file has then been uploaded to the Azure ML to the blob storage: 

<p align="center">
  <img src="dataset/creditcard.PNG" height="250">
</p>

<p align="center">
  <img src="dataset/creditcard-2.PNG" height="250">
</p>

By choosing the dataset and navigating to the Consume tab, you can see the usage details, which can be copied later on to the Python Script:

<p align="center">
  <img src="dataset/dataset-usage.PNG" height="250">
</p>

## Automated ML
To train our model with AutoML, we need to create an experiment first. Let's name it 'lab3-experiment'

<p align="center">
  <img src="automl/create_experiment.PNG" height="200">
</p>

Now we can read our dataset, and create a new compute cluster. Microsoft offers different virtual machines. We will select 'STANDARD_D2_V2' version. 

<p align="center">
  <img src="automl/cluster_creation.PNG" height="250">
</p>

If we refer to the official Microsoft documentation, we will see:
*"D-series VMs are designed to run applications that demand higher compute power and temporary disk performance. D-series VMs provide faster processors, a higher memory-to-core ratio, and a solid-state drive (SSD) for the temporary disk. Dv3-series, Dv2-series, a follow-on to the original D-series, features a more powerful CPU. The Dv2-series CPU is about 35% faster than the D-series CPU."*

Since training a model requires a high compute power, this option matches our needs well. 

When configuring AutoML, at a minimum we need to define: 

- The task - values can be 'classification', 'regression', or 'forecasting'. In our case it's classification, since we want to distinguish between normal payments and payment fraud
- The primary metric - in our case it's accuracy, since it defines how well our model performs
- Training data - for this use case we use the creditcard data we have previously uploaded
- Label column name - the column that contains our classification result. In creditcard dataset this column is called "Class"
- Compute target - a machine to run our task. We will use the one we have created previously. 

Additionally, we have defined the experiment timeout, which is 30 minutes. This way we define how long, in minutes, our experiment should continue to run.
To perform a cross-validation, we needed to define the number, which is set to 5 as in most of the Microsoft examples. As a result, metrics are calculated with the average of the five validation metrics. 

Finally, we've submitted our experiment. 

<p align="center">
  <img src="automl/automl_config.PNG" height="250">
</p>


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
