import requests

conversation_history = []
while True:
    user_input = input ("what do you have for me today:  ").lower().strip()

    url = "http://localhost:11434/api/generate"
    
    prompt =f"""
    Answer questions after searching through the converstion history so you can't forget about things I asked you about in the past and 
    if you don't find anything there then answer normally
    user question : {user_input}
    converstion history : {conversation_history}
    Answer: """
    

    data ={
    "model":"llama3.2",
    "prompt":prompt,
    "stream" : False
}

    response = requests.post(url,json=data)

    response =response.json()
    response = response["response"]
    print(response)
    history = {
    "user":user_input,
    "AI": response
}
    conversation_history.append(history)
    respond = input ("Do you have any futher questions? (yes/no):   ").lower().strip()
    if respond == "yes":
        continue
    else:
        break
        
    
