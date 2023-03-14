import json
import bs4
import requests
import boto3

def lambda_handler(event, context):
  
    s3 = boto3.resource('s3')
    
    images = []
    for i in range(1):
        url = 'https://www.imdb.com/search/name/?match_all=true&start='+str((50*i)+1)+'&ref_=rlm'
        source = requests.get(url)
        soup = bs4.BeautifulSoup(source.text, 'html.parser')
        for j in soup.find_all("div", {"class": "lister-item-image"}) : 
            images.append(j.img['src'])
            
            response = requests.get(images[len(images)-1])
            image = response.content
            
            file_name = str(len(images)).zfill(3)+".png"
            object = s3.Object('b11-images-input', file_name)
            
            object.put(Body = image)
            
    return {
        'statusCode': 200,
        'body': json.dumps('Images uploaded successfully to S3 bucket.')
    }
    
