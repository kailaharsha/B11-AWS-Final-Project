# B11-AWS-Final-Project
This repository contains files that were used to build the MIBA Term-2 Cloud Platforms : AWS course's Final project. 

This repository has 2 .py files named `webScraping.py` & `CelebRecog.py`. These codes were used to build two Lambda functions called `webScraping` & `CelebRecog`. 

THE IAM roles for each of these 2 Lambda functions are uploaded to this repository in the form of `.json` files. 

The Lambda functions require addition of certain Python library layers. Two files names `bs4.zip` & `requests.zip` have also been uploaded to this repository. These zip files can be used to create custom Layers for AWS Lambda functions and the layers can be associated with our Lambda functions whenever necessary. 

## Requirements for `webScraping` Lambda function 
- A bs4 python layer 
- A requests python layer
- An inbuilt AWS-provided Pandas Layer (`AWSSDKPandas-Python39`)
- Importing the inbuilt boto3 library
- Importing the inbuilt json library
 

## Requirements for `CelebRecog` Lambda function
- Importing the inbuilt boto3 library
- Importing the inbuilt json library


## Functionality of `webScraping` Lambda function 
This function scrapes celebrity images from the [IMDB](https://www.imdb.com/search/name/?match_all=true&ref_=rlm) website and inputs the images into an S3 bucket. For this Lambda function to run, please create an S3 bucket that is named `b11-images-input`

## Functionality of `CelebRecog` Lambda function 
This function gets triggered whenever an image is uploaded into `b11-images-input` S3 bucket. It calls AWS Rekognition's `recognize_celebrities()` & `detect_faces()` function to extract attributes from the celebrity image. The output for each image is in the form of a `.json` file and is uploaded to a bucket called `b11-images-output`.
 







