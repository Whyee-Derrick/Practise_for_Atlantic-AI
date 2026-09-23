import requests

url = "http://localhost:11434/api/generate"

data ={
    "model":"llama3.2",
    "prompt":"who is the best footballer in the world?",
    "stream":False
     
}

response = requests.post(url, json=data)
response = response.json()
print(response["response"])