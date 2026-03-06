import os

def add_group():
    group = input("Enter group name: ")
    os.system(f"sudo groupadd {group}")

def add_user_to_group():
    user = input("Username: ")
    group = input("Group: ")
    os.system(f"sudo usermod -aG {group} {user}")

def delete_group():
    group = input("Enter group name: ")
    os.system(f"sudo groupdel {group}")

def list_groups():
    os.system("cut -d: -f1 /etc/group")
