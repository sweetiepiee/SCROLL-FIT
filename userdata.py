import json
import os

# Gets the folder where userdata.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Stores users.json in the same folder as userdata.py
FILE_NAME = os.path.join(BASE_DIR, "users.json")


# Function that loads all saved users
def load_users():

    # Checks whether users.json exists
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        # Opens and reads the saved user information
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            users = json.load(file)

        return users

    except (json.JSONDecodeError, OSError):
        # If the file cannot be read, return an empty dictionary
        return {}


# Function that saves a new user's information
def save_user(user):

    # Loads all currently saved users
    users = load_users()

    # Uses username as the key
    users[user["username"]] = user

    # Saves the updated users
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


# Function that searches for a user
def get_user(username):

    # Loads all saved users
    users = load_users()

    # Returns the user's information
    return users.get(username)