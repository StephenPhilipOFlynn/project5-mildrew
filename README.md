## Dataset Content
* The dataset is sourced from Code Institute's Kaggle page, [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains over 4000 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
* A machine learning is trained and used to predict if a cherry leaf is healthy or unhealthy. This is to satisfy business requirement 2, for the client to have a method to accurately predict if a cherry leaf is healthy.

## ML Business Case
* The two business requirements are listed above. The project was successful in building a project that could predict whether a cherry leaf is healthy with 99% accuracy. 

## Dashboard Design
* The Healthy Leaf Detector Streamlit dashboard is a machine learning application designed to help users quickly and accurately determine whether a leaf is healthy or unhealthy based on an uploaded image. The model uses a pre-trained network to classify leaf images, providing both the predicted class (healthy or unhealthy) and the confidence level of the prediction.

## Project Hypothesis

* We hypothesise that mildew-infected leaves exhibit distinct visual characteristics, that can be distinguished from healthy leafs using image classification machine learning techniques, with an accuracy of at least 95%."
* The project was successful in meeting the hypothesis, with the assumption that a valid picture of a cherry leaf has been submitted from an aerial view from between 3 to 30 cm above the leaf.

*ML Performance Metrics
The purpose of this page is to provide an analysis of the machine learning model's performance. It showcases key metrics such as accuracy, and loss. This page allows users to assess the reliability and effectiveness of the model in detecting mildew, offering transparency and insights into the model's strengths and areas for improvement.
Content Focus: Detailed performance metrics, evaluation results, explanation of metrics, and interpretation of the model's effectiveness.
*Visualiser
This page provides a graphical interface for users to explore and interact with the data and model predictions. The Visualiser is an interactive tool that allows users to gain a deeper understanding of the data, the model's decision-making process, and the factors that influence predictions. This page is useful for users who wish to understand the graphical data being used for the analysis. 
*Test Image
The Test Image page is a hands-on, interactive section where users can upload an image of a leaf and receive a prediction on whether it is infected with mildew. This page is the core of the dashboard's functionality, allowing users to apply the trained model to new, unseen data. It provides immediate feedback, making it a practical and user-friendly feature.

## Unfixed Bugs
* The data was manually uploaded to the Gitpod / VS Code workspace rather than using Kaggle's API. 

## Deployment
* The dashboard was first deployed on the 7 April 2024 on Heroku.
* The dashboard was redeployed on the 11 August 2024 on Heroku.

### Heroku

* The App live link is: https://cherry-leaves-ml-d220bd96c860.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process required logging into the Heroku CLI and changing to a previously supported runtime version. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries. 
* Pillow, Numpy, Pandas, Matplotlib, Seaborn, SciKit, TensorFlow, Keras, Altair for machine learning and data analysis and visualisation.
* Streamlit for dashboard.

## Credits 

* Code Institute walkthrough project 'Malaria Detector' by Gyan Shashwat, provided model code and guidance on structuring this Machine Learning Project.
https://github.com/GyanShashwat1611/WalkthroughProject01/

### Media

- The image set used for the project were taken from Code Institute's kaggle page.
https://www.kaggle.com/datasets/codeinstitute/cherry-leaves



