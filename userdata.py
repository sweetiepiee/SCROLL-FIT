import json
import os

#Name of the file where all user account information will be stored
FILE_NAME = "users.json"

#Function that loads all saved users from the JSON file
def load_users():

    #Checks whether the users.json file exists
    if not os.path.exists(FILE_NAME):

        #Returns an empty dictionary if no users have been saved yet
        return{}

    #Opens the JSON file and reads the saved user information
    with open(FILE_NAME, "r") as file:
        users = json.load(file)

    #Returns all saved users
    return users

#Function that saves a new user's information
def save_user(user):

    #Load all currently saved users
    users = load_users()

    #Uses the username as the key for the user's information
    users[user["username"]] = user

    #Opens the JSON file and saves the updated user information
    with open (FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

#Function that searches for a user using their username
def get_user(username):

    #Loads all saved users
    users = load_users()

    #Returns the user's information if the username exists
    return users.get(username)