import os 
from user_manager import *
from group_manager import *

def menu():
    while True:
        print("""
========== Linux User Manager ==========
1. Add User
2. Modify User
3. Delete User
4. List Users
5. Add Group
6. Add User to Group
7. Delete Group
8. List Groups
9. Disable User
10. Enable User
11. Change Password
0. Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            modify_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            list_users()
        elif choice == "5":
            add_group()
        elif choice == "6":
            add_user_to_group()
        elif choice == "7":
            delete_group()
        elif choice == "8":
            list_groups()
        elif choice == "9":
            disable_user()
        elif choice == "10":
            enable_user()
        elif choice == "11":
            change_password()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
