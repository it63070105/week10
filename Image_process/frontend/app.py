import io

import urllib
from flask import Flask, render_template, request
import requests
import base64
import matplotlib.pyplot as plt
import numpy as np
import cv2
import json

app = Flask(__name__,template_folder="")

# encode image as base64 string
def encode_image(image):
    _, encoded_image = cv2.imencode(".jpg", image)
    return "data:image/jpeg;base64," + base64.b64encode(encoded_image).decode()

# decode base64 string to image
def decode_image(image_string):
    encoded_data = image_string.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

url = "http://54.152.253.145:8088"

@app.route('/')
def home():
    # Load the image
    image = cv2.imread("building.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_string = encode_image(image)

    payload = {
        "image": image_string,
        "name": "John",
        "surname": "Doe",
        "numbers": [1, 2, 3, 4, 5]
    }

    response = requests.post(f"{url}/process-image", json=payload)
    data = json.loads(response.content)

    processed_image_string = data["processed_image"]
    processed_image = decode_image(processed_image_string)

    # Create a figure and set the title
    fig = plt.figure(figsize=(12, 4))
    fig.suptitle('Comparison of Images')

    # Add the first image to the left subplot
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(image)
    ax1.set_title('Original image')

    # Add the second image to the right subplot
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.imshow(processed_image)
    ax2.set_title('Processed image')

    # Show the plot
    # plt.show()
    img = io.BytesIO()
    plt.savefig(img, format = 'png')
    img.seek(0)
    plot_data = urllib.parse.quote(base64.b64encode(img.read()).decode())
    return render_template("index.html", image=plot_data)
    

@app.route('/file/<string:name>')
def template(name):
    
    # Load the image
    # if name.find('http') != -1:
    #     url_response = urllib.request.urlopen(name)
    #     img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    #     image = cv2.imdecode(img_array, -1)
    # else:
    
    image = cv2.imread(name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_string = encode_image(image)

    payload = {
        "image": image_string,
        "name": "John",
        "surname": "Doe",
        "numbers": [1, 2, 3, 4, 5]
    }

    response = requests.post(f"{url}/process-image", json=payload)
    data = json.loads(response.content)

    processed_image_string = data["processed_image"]
    processed_image = decode_image(processed_image_string)

    # Create a figure and set the title
    fig = plt.figure(figsize=(12, 4))
    fig.suptitle('Comparison of Images')

    # Add the first image to the left subplot
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(image)
    ax1.set_title('Original image')

    # Add the second image to the right subplot
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.imshow(processed_image)
    ax2.set_title('Processed image')

    # Show the plot
    # plt.show()
    img = io.BytesIO()
    plt.savefig(img, format = 'png')
    img.seek(0)
    plot_data = urllib.parse.quote(base64.b64encode(img.read()).decode())
    return render_template("index.html", image=plot_data)

@app.route('/url')
def template1():
    name = request.args.get('img')

    name = name.replace("%3A", ":")
    name = name.replace("%2F", "/")

    # Load the image
    url_response = urllib.request.urlopen(name)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    image = cv2.imdecode(img_array, -1)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_string = encode_image(image)

    payload = {
        "image": image_string,
        "name": "John",
        "surname": "Doe",
        "numbers": [1, 2, 3, 4, 5]
    }

    response = requests.post(f"{url}/process-image", json=payload)
    data = json.loads(response.content)

    processed_image_string = data["processed_image"]
    processed_image = decode_image(processed_image_string)

    # Create a figure and set the title
    fig = plt.figure(figsize=(12, 4))
    fig.suptitle('Comparison of Images')

    # Add the first image to the left subplot
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(image)
    ax1.set_title('Original image')

    # Add the second image to the right subplot
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.imshow(processed_image)
    ax2.set_title('Processed image')

    # Show the plot
    # plt.show()
    img = io.BytesIO()
    plt.savefig(img, format = 'png')
    img.seek(0)
    plot_data = urllib.parse.quote(base64.b64encode(img.read()).decode())
    return render_template("index.html", image=plot_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8081")
