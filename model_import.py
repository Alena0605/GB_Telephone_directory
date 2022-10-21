from shutil import copy
import json
import excep
import model_export as m_e


def save_to_csv():
    file_2 = excep.check_not_file()
    copy('Contacts.txt', f"{file_2}.csv")
    return "File is saved."
 

def save_to_json():
    file_1 = 'Contacts.txt'
    file_2 = excep.check_not_file()

    with open(file_1, 'r', encoding='utf-8') as f:
        contacts_list = m_e.read_data(file_1)
        data = []
        for contact in contacts_list:
            data_dict = {}
            data_dict['surname'] = contact[0]
            data_dict['name'] = contact[1]
            data_dict['phone'] = contact[2]
            if len(contact) == 4:
                data_dict['comment'] = contact[3]
            else:
                data_dict['comment'] = ''
            data.append(data_dict)
    
    with open(f"{file_2}.json", 'w', encoding='utf-8') as f_json:
        json.dump(data, f_json, ensure_ascii=False)

    return "File is saved."
