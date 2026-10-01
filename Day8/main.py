import requests
from pypdf import PdfReader

knowledge_text = ""
conversation_history = []

reader = PdfReader("maths.pdf")

for page in reader.pages :   
    knowledge_text+=page.extract_text()
        
url = "http://localhost:11434/api/generate"

while True:
    user_input = input ("What is your question for me Today ? ")
           
    prompt = f""" 
        You are an AI Assistant the explains answers to users in very simple words.
        You will remember previouse conversation in History and you will answer questions based on Context and if question is not in Context
        you will answer normally. 
        you will answer previouse questions without making statement like "Based on our recent conversation we t5alked about ..." and you will 
        answer questions that is not in Context without saying statement like "The question you asked is not in maths.pdf but ..." but you will answer directly after any 
        of those instances. 
        History : {conversation_history}
        Context : {knowledge_text}
        question : {user_input}
        Answer:"""
        
    data = { 
            "model":"llama3.2",
            "prompt":prompt,
            "stream": False
        }
        
    response = requests.post (url , json= data)
    response = response.json()
    response = response["response"]
    print(response)
        
    data_ = { 
            "user":user_input,
            "AI":response
        }
    conversation_history.append(data_)
    respond = input ("Do you have more questions (yes/no) ")
    if respond.lower() == "no":
            break
         
