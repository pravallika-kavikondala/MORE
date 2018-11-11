# MORE

This is a simple Python Flask application that accepts __MOvie REviews__ from users and displays them. Users can translate the reviews into another language and can check the sentiments behinds the reviews. Google Cloud APIs are used for language translation and sentiment analysis. Our app is deployed on Google Cloud App Engine. 
When the app is deployed, it creates an instance of app engine running on the Google Cloud Platform. To get the app running, first make sure that the instance is running on Google App Engine. Instructions to deploy the app are provided below.

## Getting Started
### Prerequisites
1. User should have a Google Cloud Platform account and a project.
2. User should enable Google Cloud Language and Translate APIs.
3. User should create a service account to use ML APIs. Please refer Setup section in README.md on how to create service account.
4. User should already have requirement.txt installed on his cloud platform. Refer the repo for requirements.txt file.
### Installation
To install requirements.txt, use the following command
```
$pip install -r requirements.txt
```
### Setup 
To create service account:
1. You will need a service account to authenticate. To make one, replace [NAME] with desired name of service account and run the following command in Cloud Shell: $gcloud iam service-accounts create [NAME]
2. Now you'll need to generate a key to use that service account. Replace [FILE_NAME] with desired name of key, [NAME] with the service account name from above and [PROJECT_ID] with the ID of your project. The following command will create and download the key as [FILE_NAME].json: $gcloud iam service-accounts keys create [FILE_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com
3. To use the service account, you'll have to set the variable GOOGLE_APPLICATION_CREDENTIALS to the path of the key. To do this, run the following command after replacing [PATH_TO_FILE] and [FILE_NAME]: $export GOOGLE_APPLICATION_CREDENTIALS=[PATH_TO_FILE]/[FILE_NAME].json
4. Note that this will only set the variable for your current session.Update ~/.bashrc to set credentials for each Cloud Shell session with the following command: $source /google/devshell/bashrc.google

## Deployment
Use the following command to deploy the app on Google Cloud App Engine
```
$gcloud app deploy
```
Your app will be dployed on www.PROJECT_ID.appspot.com
### Note
* This app is basically running on google app engine. So, when loaded it opens on the website: https://pravallika-kavikondala.appspot.com, where pravallika-kavikondala is the project name on Google Cloud Platform.
* In order to see the app running, programmer has to keep the instance running on Google App Engine. Only then the working application can be accessed.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## References
* https://cloud.google.com/python/getting-started/using-cloud-datastore
* https://github.com/GoogleCloudPlatform/getting-started-python/tree/504b3d550b551502cfe96f32542c31b232135eff/2-structured-data
	
## Acknowledgements
* Google Cloud user documentation

## Contact Information
1. Pravallika Kavikondala: pk7@pdx.edu
2. Neha Gadge: ng8@pdx.edu
