# login.py

users = {
    "admin": "123456",
    "user": "password"
}

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed!")

if __name__ == "__main__":
    login()