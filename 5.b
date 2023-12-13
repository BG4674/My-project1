import json
import hashlib
import getpass

USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=2)

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def register_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    users = load_users()

    if username in users:
        print("User already exists. Please choose a different username.")
        return

    salt = "somerandomsalt"  
    hashed_password = hash_password(password, salt)

    users[username] = {'password': hashed_password, 'salt': salt}
    save_users(users)
    print(f"User '{username}' registered successfully.")

def login_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    users = load_users()

    if username not in users:
        print("User not found. Please check your username.")
        return

    stored_password = users[username]['password']
    salt = users[username]['salt']
    hashed_password = hash_password(password, salt)

    if hashed_password == stored_password:
        print(f"Welcome, {username}! You are now logged in.")
    else:
        print("Invalid password. Please try again.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
