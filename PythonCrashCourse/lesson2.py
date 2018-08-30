import json

def get_username(filename):
    try:
        with open(filename) as file_res:
            username = json.load(file_res)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(filename):
    username = input("What's your name?")
    with open(filename,"w") as file_res:
        json.dump(username,file_res)
    return username

def greet_user(filename):
    username = get_username(filename)
    if username:
        checkname = input("Hey,are you " + username + "?(yes/no)")
        if checkname == "yes":
            print("I knew it,you are " + username)
        else:
            print("Humm,let me think...,so")
            username = get_new_username(filename)
            print("Welcome," + username)
    else:
        print("Zzz...")
        username = get_new_username(filename)
        print("Hi~\n" + username)


filename = "./username.json"

greet_user(filename)