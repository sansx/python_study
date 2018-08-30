import json

faverite_number = input("What's your favorite number?")
filename = "./number.json"


with open(filename,"w") as file_res:
    json.dump(faverite_number,file_res)

try:
    with open(filename,"r") as file_res:
        print("I know your favorite number! It's "+json.load(file_res))
except FileNotFoundError:
    print("can't find your favorite number")
