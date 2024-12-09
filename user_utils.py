# user_utils.py

import csv

CSV_FILE = "data.csv"

def read_user_data():
    
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

def authenticate_user(username, password):
    
    users = read_user_data()

    for user in users:
        if user["Username"] == username and user["Password"] == password:
            return user
    return None

def get_username_by_name(name):
    
    users = read_user_data()

    for user in users:
        if user["Name"] == name:
            return user  
    return None

def read_user_data():
   
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)  
