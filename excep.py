from os import path


def wrong_input():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print('-' * 50)
            print("Incorrect entry! Please, choose something from the list!")


def check_file():
    while True:
        file_path = input("Enter path to the file: ")
        if not path.exists(file_path):
            print("The file does not exist or entered incorrect path!")
        else:
            return file_path


def check_not_file():
    while True:
        file_name = input("Enter name of the file without extension: ")
        if path.exists(f"{file_name}.csv") or path.exists(f"{file_name}.json"):
            print("The file with this name already exists! Are you sure you want to overwrite the file?")
            while True:
                print("Enter 1 - if 'yes', or 2 - if 'no'.")
                num = wrong_input()
                if num == 1:
                    return file_name
                elif num == 2:
                    print("Enter new name of the file: ")
                    break
                else:
                    print("Incorrect entry! Please, choose something from the list!")
        else:
            return file_name


def check_name(text):
    while True:
        name = input(text)
        if not name or not name.isalpha():
            print("Wrong input! The field can not be empty or contain numbers!")
        else:
            return name.capitalize()


def check_number():
    while True:
        try:
            phone = int(input("Enter the phone number without 7: "))
            if len(str(phone)) == 10:
                return phone
            else: 
                print("Number of digits is incorrect! Try again.")
        except ValueError:
            print("Wrong input! The phone should contain only numbers!")
