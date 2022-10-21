import model_export as m_e
import excep
import log


def delete_contact():
    file = excep.check_file()
    contacts_list = m_e.read_data(file)
    
    print()
    print("Enter name and surname for delete from list: ")
    name = excep.check_name("Enter the name: ").capitalize()
    surname = excep.check_name("Enter the surname: ").capitalize()

    for contact in contacts_list:
        if surname == contact[0] and name == contact[1]:
            index = contacts_list.index(contact)
            contacts_list.pop(index)
            
            log.log_data_input(f"{'  '.join(contact)}")
            
            with open(file, 'w', encoding='utf-8') as f:
                for ls in contacts_list:
                    f.write(' '.join(ls) + '\n')
            
            print()
            return f"The contact {surname} {name} is deleted."
    
    log.log_data_input(f"Contact {surname} {name} does not exist")
    return "This contact does not exist!"
