#IMPORTING MODULES
from datetime import datetime 
import os
import getpass

print("LET'S START YOUR DIARY WRITING JOURNEY!!!")

PASSWORD_FILE = "diary_password.txt"

def create_password():
    if not os.path.exists(PASSWORD_FILE):
        password = getpass.getpass("Create your diary password: ")
        with open(PASSWORD_FILE, "w") as f:
            f.write(password)
        print("Password set successfully!\n")

def check_password():
    if not os.path.exists(PASSWORD_FILE):
        print("Password not found. Please set a password first.")
        return False
    password = getpass.getpass("Enter your diary password: ")
    with open(PASSWORD_FILE, "r") as f:
        saved_password = f.read()
    if password == saved_password:
        return True
    else:
        print("Incorrect password.\n")
        return False

def write_entry():
    if not check_password():
        return
    entry = input("What's on your mind today?\n>>> ")
    now = datetime.now()
    date_str = now.strftime("%d-%m-%y")
    time_str = now.strftime("%H:%M:%S")

    filename = f"Diary_{date_str}.txt"

    with open(filename, "a") as f:
        f.write(f"[{time_str}] {entry}\n")
    print(f"Entry saved in {filename}!\n")

def view_file():
    if not check_password():
        return
    date_str = input("Enter date to view (dd-mm-yy): ")
    filename = f"Diary_{date_str}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            print(f"\n--- Diary Entry on {date_str} ---\n")
            print(f.read())
    else:
        print("No entry found for that date.\n")

def main():
    create_password()
    while True:
        print("\n--- Personal Diary Menu ---")
        print("1. Write a new entry")
        print("2. View an entry by date")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            write_entry()
        elif choice == "2":
            view_file()
        elif choice == "3":
            print("Exiting diary. Stay safe!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
