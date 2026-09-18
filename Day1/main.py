import json
from pathlib import Path

file_name = Path("Day1").parent/"courses.json" 
try:
    with open(file_name, 'r') as f:
        courses = json.load(f)
except FileNotFoundError:
    print ("The file is not found")        

def search(user_input):
    for course in courses:
        if course["code"] == user_input:
            return f"{course["code"]} is {course["name"]}\nlevel: {course["level"]}\nSemester:{course["semester"]}."
    else:
        return "Course not Available!"    
   

user_input = input ("What course are you looking for ? ")
print(search(user_input))

while True:    
    next_respond = input ("Do you want to look for another course (yes/no) ? ")
    if next_respond.lower()== "yes":
        user_input = input ("What course are you looking for ? ")
        print(search(user_input))
    elif next_respond.lower() == "no":
        print ("Thanks for your time!😁")
        break    
    else:
        print ("Enter the right respond ")
