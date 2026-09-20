import json


with open ("data.json","r",encoding="utf-8") as f:
    data_ =json.load(f)

def search(user_input):
    for item in data_:
        if item["topic"].lower() in user_input.lower():
            return item["content"] 
    else:
        return "Not available."   

#Main program
user_input = input ("What question do you have for me today?😊 ")
print(search(user_input)) 

while True:
    respond = input ("Do you have anymore questions? (yes/no) ")
    if respond.lower() == "yes":
        user_input = input ("What question do you have for me,I'm all ears? ")
        print(search(user_input))
    elif respond.lower() == "no":
        break
    else:
        print ("Wrong respond please try again! Type either \"yes\" or \"no\" .")
            
        
        
          