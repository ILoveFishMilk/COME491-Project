import requests

def recognize_request(image_paths):


    images = [('images', open(image_path, 'rb')) for image_path in image_paths]
    
    url = "http://localhost:8000/app"

    return requests.post(url, files=images).text
