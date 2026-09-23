import requests

url = "http://localhost:11434/api/generate"

user_input = input ("You: ")

data = {
    "model": "llama3.2",
    "prompt":user_input,
    "stream": False
}

response = requests.post(url,json = data)

response = response.json()
print ("AI: ",response["response"])


while True:
    user_input = input ("Do you have anyother questions?(yes/no)  ")
    if user_input.lower() == "yes":
        user_input = input("You: ")
        data = {
                 "model": "llama3.2",
                "prompt":user_input,
                "stream": False
            }

        response = requests.post(url,json = data)

        response = response.json()
        print ("AI: ",response["response"])
    elif user_input.lower() == "no":
        break
    else:
        print ("Incorrect input, enter either yes/no ")
    

