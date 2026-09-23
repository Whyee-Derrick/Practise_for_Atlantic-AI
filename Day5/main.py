import requests
from pathlib import Path

knowledge_file = Path("Day5")
knowledge = knowledge_file/"knowledge.txt"

with open (knowledge, "r",encoding = "utf-8") as f:
    knowledge_text = f.read()
user_input = input ("What I do for you today? ")

url = "http://localhost:11434/api/generate"

prompt = f"""
Answer question based of the context been given , and lightly polish answer without adding too much info
context={knowledge_text}
Question={user_input}
Answer:"""  

data ={
    "model": "llama3.2",
    "prompt":prompt,
    "stream":False
} 

response = requests.post(url,json=data )
response = response.json()
print (response["response"])      