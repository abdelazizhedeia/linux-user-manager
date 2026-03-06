import os 

def add_user():
    username = input("Enter username: ")
    os.system(f"sudo useradd {username}")
    os.system(f"sudo passwd {username}")

def modify_user():
    username = input("Current username: ")
    new_username = input("New username: ")
    os.system(f"sudo usermod -l {new_username} {username}")

def delete_user():
    username = input("Enter username: ")
    os.system(f"sudo userdel -r {username}")

def list_users():
    os.system("cut -d: -f1 /etc/passwd")

def disable_user():
    username = input("Enter username: ")
    os.system(f"sudo usermod -L {username}")

def enable_user():
    username = input("Enter username: ")
    os.system(f"sudo usermod -U {username}")

def change_password():
    username = input("Enter username: ")
    os.system(f"sudo passwd {username}")
