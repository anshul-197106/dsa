# json

import json

data={
    "name":"Alice",
    "age":25,
    "city":"New York",
    "hobbies":["reading","coding"]
}

with open("data.json","w")as file:
    json.dump(data, file)

#list diectory contents
# files = os.listdir(",")
# print(files) 
