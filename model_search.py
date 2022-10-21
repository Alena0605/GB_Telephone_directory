import model_export as m_e
import excep


def search_contact():
    file = excep.check_file()
    contacts_list = m_e.read_data(file)
    
    print()
    print("Enter name and surname for searching: ")
    name = excep.check_name("Enter the name: ").capitalize()
    surname = excep.check_name("Enter the surname: ").capitalize()

    for contact in contacts_list:
        if surname == contact[0] and name == contact[1]:
            index = contacts_list.index(contact)
            print()
            return '  '.join(contacts_list[index])
    
    return "This contact does not exist!"
