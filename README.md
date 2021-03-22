<!-- https://drive.google.com/file/d/1kYWbQPcjMp4z8cTCW0_ShrDLZsaOIy2u/view?usp=sharing -->
# E-Commerce Payment Fraud Detection

##### Table of Contents  
[Motivation](#motivation)  
[Dataset](#dataset)  
[Automated ML](#automl)  
[Hyperparameter Tuning](#hyper)  
[Model Deployment](#deploy)   
[Screen Recording](#recording)  
[Future improvements](#future)    

<a name="motivation"/>  

## Motivation
The world is getting more digitalized, and so do payments. Fraud in commerce is called "payment fraud" and is defined as any type of illegal or false transaction. The profit can be money, goods or even sensitive information. Since COVID-19 e-payment transactions amount has risen. According to the [Sift insights](https://blog.sift.com/2020/where-does-fraud-go-from-here-how-coronavirus/), the education space, travel and transportation are the most hot targets in this year. 

<p align="center">
  <img src="https://blog.sift.com/wp-content/uploads/2020/07/COVID-graphic-768x362.png">
</p>

There are several tools on the market that are used to detect payment frauds, and all of them use artificial intelligence to do so. In this project there is an attempt to analyze a dataset and determine how well can fraudulent actions be recognized. 

<a name="dataset"/>  

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

<a name="automl"/>  

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

- The task **(task)** - values can be 'classification', 'regression', or 'forecasting'. In our case it's classification, since we want to distinguish between normal payments and payment fraud
- The primary metric **(primary_metric)** - in our case it's accuracy, since it defines how well our model performs
- Training data **(training_data)** - for this use case we use the creditcard data we have previously uploaded
- Label column name **(label_column_name)** - the column that contains our classification result. In creditcard dataset this column is called "Class"
- Compute target **(compute_target)** - a machine to run our task. We will use the one we have created previously. 

Additionally, we have defined the experiment timeout **(experiment_timeout_minutes)**, which is 30 minutes. This way we define how long, in minutes, our experiment should continue to run.
To perform a cross-validation **(n_cross_validations)**, we needed to define the number, which is set to 5 as in most of the Microsoft examples. As a result, metrics are calculated with the average of the five validation metrics. 

Finally, we've submitted our experiment. 

<p align="center">
  <img src="automl/automl_settings.PNG" height="250">
</p>

When navigating to the experiment, it can be seen that the training is running

<p align="center">
  <img src="automl/training-child-models.PNG" height="250">
</p>

### Results
The experiment is completed

<p align="center">
  <img src="automl/automl-completed-2.PNG" height="250">
</p>

Upon the completion of the experiment, in the run details we can see how our models have perfomed, and which one has scored the best accuracy. As we can see, VotingEnsemble has slightly outperformed StackEnsemble model.

<p align="center">
  <img src="automl/run-details-4.PNG" height="350">
</p>

This accuracy can also be seen on the graphic. It seems that most of the methods perfomed almost equally well. 

<p align="center">
  <img src="automl/run-details-accuracy.PNG" height="300">
</p>

Does this mean we have an ideal training model? Unfortunately, not. Though AutoML has worked on balancing our dataset, we must remember that from the very start it was highly imbalanced, which means we are lacking on the fraud examples. Therefore, any analysis will bring the high accuracy for this type of the dataset. At the same time, our experiment was not in vain, since if we check for parameters, we will see that the definitely meaningful features are V4 and V14.

<p align="center">
  <img src="automl/voting-ensemble-features.PNG" height="250">
</p>

This means, that there are important features, which can help to define a fraudful payment. 
By using the values from the confusion matrix, we can determine the true positive and true negative rates. 

<p align="center">
  <img src="automl/confusion-matrix.PNG" height="250">
</p>

After a quick math, we can say that: 

- The non-fraudulent transactions are recognized in 99.991558% of cases
- The fraudulent transactions are recognized in 78.658536% of cases, which is still a good result.

<a name="hyper"/>  

## Hyperparameter Tuning
First of all, we need to clean our data - by turning it from inbalanced to the balanced one. To do so, we have selected all fraudulent entries (which are 492 in total), and randomly selected 492 non-fraudulent ones. Out of these entries we have built a single dataset

<p align="center">
  <img src="hyperdrive/dataset_1.PNG" height="250">
</p>

As can be seen on the following generated image, the dataset is now balanced:

<p align="center">
  <img src="hyperdrive/dataset_2.PNG" height="250">
</p>

The results can now be stored in a csv file, which we call "prepared.csv".

<p align="center">
  <img src="hyperdrive/dataset_3.PNG" height="250">
</p>

Since our data is now balanced, for the Hyper Drive model we've used LogisticRegression with two configurazitation parameters:

- Regularization strength, which lies between 0.001 and 1. The lower the value is, the bigger is the impact.
- Maximal number of iterations, which lies between 30 and 250. 

These parameters are selected randomly, with the help of RandomParameterSampling.
For the termination policy the BanditPolicy was used. 

<p align="center">
  <img src="hyperdrive/hyper_sampling.PNG">
</p>

Starting our Hyper Drive, we can see the details with RunDetails widget:

<p align="center">
  <img src="hyperdrive/hypervisor_run.PNG" height="300">
</p>


### Results
Our experiment is now finished, and we can see that the best two runs have reached the same result, which is around 94.77% of accuracy. 

<p align="center">
  <img src="hyperdrive/completed_1.PNG" height="250">
</p>

The following graphic gives a better overview of the performance of different runs:

<p align="center">
  <img src="hyperdrive/completed_2.PNG" height="250">
</p>

<p align="center">
  <img src="hyperdrive/completed_3.PNG" height="250">
</p>

<p align="center">
  <img src="hyperdrive/completed_4.PNG" height="250">
</p>

We can now print the best model id: 

<p align="center">
  <img src="hyperdrive/best_model.PNG" height="150">
</p>

<a name="deploy"/>  

## Model Deployment
Comparing all models, I decided to deploy the AutoML best model. 
In order to deploy and to test it, the two additional scrips were required: 

- score.py
- endpoint.py

score.py contains two methods: init() and run(data). These help to initialize the model, and define how to proceed with requests. The input and output samples define in which format the model has to expect the data, and provide response. 

<p align="center">
  <img src="deployment/samples.PNG">
</p>

The service was named as "payment-fraud-detection". The AciWebservice Class represents a machine learning model deployed as a web service endpoint on Azure Container Instances.

<p align="center">
  <img src="deployment/deployment.PNG">
</p>

After waiting for several minutes, the deployment has succeeded. 

<p align="center">
  <img src="deployment/fraud_detection_1.PNG">
</p>
<p align="center">
  <img src="deployment/fraud_detection_2.PNG">
</p>
<p align="center">
  <img src="deployment/fraud_detection_3.PNG">
</p>

After trying out the endpoint.py with random data, the request turned out to be successful, and returned response (0, 0), which means that both requests are non-fraudulent. 

<p align="center">
  <img src="deployment/endpoint_run.PNG">
</p>

<a name="recording"/>  

## Screen Recording
The whole project is summarized in the following short video (please click on the image below). 
<!--- <div align="center">
  <a href="https://drive.google.com/file/d/1xPzfLuen6wuJ_UZ6q4oFnv666XksRaY5/view?usp=sharing"><img src="https://images.pexels.com/photos/1626481/pexels-photo-1626481.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" alt="IMAGE ALT TEXT"></a>
</div> -->
<div align="center">
  <a href="https://drive.google.com/file/d/1xPzfLuen6wuJ_UZ6q4oFnv666XksRaY5/view?usp=sharing"><img src="https://images.pexels.com/photos/1626481/pexels-photo-1626481.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" alt="IMAGE ALT TEXT"></a>
</div>

<a name="future"/>  

## Future improvements
As can be seen from the data analysis, the dataset is highly imbalanced. Unfortunately, this is hard to change, since we do not have enough fraud examples. Therefore, it would be important on better understanding the data, and finding ways to collect more. 
