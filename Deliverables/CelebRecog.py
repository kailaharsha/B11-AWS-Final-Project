import json
import boto3

def lambda_handler(event, context):

    rekognition = boto3.client('rekognition')
    
    record = event["Records"][0]
    object_name = record['s3']['object']['key']

    parameters = {
        "Image": {
            "S3Object": {
                "Bucket": "b11-images-input",
                "Name": object_name
            }
        }
    }

    response1 = rekognition.recognize_celebrities(Image=parameters["Image"])
    response2 = rekognition.detect_faces(Image=parameters["Image"], Attributes=['ALL'])

    if (len(response1['CelebrityFaces']) != 0):
        name = response1['CelebrityFaces'][0]["Name"]
        gender = response1['CelebrityFaces'][0]["KnownGender"]["Type"]
        wiki_url= response1['CelebrityFaces'][0]["Urls"][0]
        imdb_url = response1['CelebrityFaces'][0]["Urls"][1]
        
        age_lower = response2["FaceDetails"][0]["AgeRange"]["Low"]
        age_upper = response2["FaceDetails"][0]["AgeRange"]["High"]
        age_range = "["+str(age_lower)+"-"+str(age_upper)+"]"
        
    else : 
        name = None
        wiki_url= None
        imdb_url = None
        gender = None
        age_range = None
    
    dic = {"Celebrity Name" : name,
            "Gender" : gender,
            "Age Range" : age_range,
            "Wikipedia URL" : wiki_url,
            "IMDB URL" : imdb_url
            }
     
    s3 = boto3.resource("s3")
    output_name = object_name.replace("png", "json")
    output_object = s3.Object("b11-images-output", output_name)
    output_object.put(Body=json.dumps(dic).encode('utf-8'))

    return "OK"
    