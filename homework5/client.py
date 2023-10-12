import requests

url = "http://116.203.143.215:5000/predict"

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url, json=client).json()
print(response)
