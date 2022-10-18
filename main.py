import base64
import os
from typing import List
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from dataclasses import dataclass
from datetime import datetime


# # ui = input("Please Enter Password:\n> ")
# with open("cashe/holder1.txt", "r") as var:
#     test = var.read()
#     var.close()

# password = bytes(str(test), encoding="utf-8")
# salt = os.urandom(16)
# kdf = PBKDF2HMAC(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=390000,
# )
# key = base64.urlsafe_b64encode(kdf.derive(password))
# f = Fernet(key)
# token = f.encrypt(b"Secret message!")
# token
# f.decrypt(token)

# while True:
#     user = input("Input: ")
# with open("cashe/holder2.txt", "w") as dd:
#     dd.write(user)


@dataclass
class Formats:
    domain: str
    password: str
    time: datetime


attempts = 3
l: List = []
l2: List = []
verify = False

if os.path.exists("cashe/login.txt"):
    while True:
        ui = input("Enter Password \n> ")
        if ui == "123":
            verify = True
            # will log out if verify check fails
            while verify == True:
                print("Please Enter A Command: \nView Password\nNew Password\nModify")
                command = input("> ")
                command = command.lower()
                if command == "view" or command == "view password":
                    # display inserted passwords from cache/passwords.txt
                    while True:
                        verify_input = input("Please verify password\n> ")
                        if verify_input == "123":
                            # for each in l:
                            #     print(
                            #         f"\n{each.domain}\n    {each.password}\n    {each.time}\n\n"
                            #     )
                            with open("cashe/passwords.txt", "r") as file:
                                words = file.read().splitlines()
                                for each in words:
                                    l2.append(each.split())
                            # Find maximal length of all elements in list
                            n = max(len(x) for l in l2 for x in l)
                            # Print the rows
                            for row in l2:
                                print("".join(x.ljust(n + 2) for x in row))
                                print(
                                    "------------------------------------------------------------------------"
                                )
                            break
                        else:
                            print("INCORRECT PASSWORD: LOGGING OUT")
                            verify = False
                            break

                elif command == "new" or command == "new password":
                    try:
                        # give prompt to insert new password
                        domain = input("Name Your Password: \n> ")
                        password = input("Enter Your Password: \n> ")
                        # saves time for later
                        current_date_and_time = datetime.now()
                        # this should write the information in a file instead
                        # l.append(Formats(domain, password, current_date_and_time))
                        with open("cashe/passwords.txt", "a") as file:
                            file.write(
                                f"{domain} {password} {current_date_and_time}" + "\n"
                            )
                            file.close
                    except FileNotFoundError:
                        print("ERROR: FILE NOT FOUND: GENERATING NEW FILE")
                        with open("cashe/passwords.txt", "w") as holder:
                            holder.close

                elif command == "mod" or command == "modify":
                    ...  # give list of passwords and allow to change a password or remove a password

                elif command == "log" or command == "logout":
                    break

        else:  # tracks attempts and stops system when out of attempts
            attempts -= 1
            if attempts >= 1:
                print(f"INVALID PASSWORD: {attempts} attempt left")
            elif attempts == 0:
                print("NO ATTEMPTS LEFT, PLEASE TRY AGAIN IN 5 MINUTES.")
else:
    dir = "cashe"
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir)
    print(path)
    os.mkdir(path)
    print(f"Directory {dir} created")
    login = input("Creating New login folder, please create a new password.\n> ")
    with open("cashe/login.txt" "w") as create:
        create.write(login)
        create.close
