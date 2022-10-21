import excep


def data_input():
    name = excep.check_name("Enter the name: ")
    surname = excep.check_name("Enter the surname: ")
    phone = excep.check_number()
    comment = input("Enter any comment: ")
    return f"{surname} {name} {phone} {comment}\n"
