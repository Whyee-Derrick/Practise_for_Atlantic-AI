import csv
import requests


with open ("kaggle.csv","r",encoding="utf-8") as f:
    reader = list(csv.DictReader(f))

    user_input = input ("what\'s on your mind ,any question for me?").lower()
    def local_search ():
     for row in reader :
        if user_input in row ["question"].lower() or user_input in row ["context"].lower():
          return row["context"].lower()
     else: 
        return ("Not Available!")
         
    
url = "http://localhost:11434/api/generate"

prompt = f"""
  Answer questions simple based on the context given , and polish it abit and if the question is not in the given context answer yourself in simple words without talking about you not getting any info from the given context
  Question :{user_input }
  context : {local_search()}
  Answer:"""

data ={
    "model":"llama3.2",
    "prompt":prompt,
    "stream":False
}

response = requests.post (url,json=data)
response = response.json()
response = response["response"]
print (response)