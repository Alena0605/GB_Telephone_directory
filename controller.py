import user_interface as u_i
import excep 
import log
import model_add as m_a
import model_delete as m_d
import model_export as m_ex
import model_import as m_im
import model_search as m_s


def run():
    print("WELCOME TO THE PHONEBOOK DIRECTORY!")

    while True:
        print()
        u_i.main_menu()
        num = excep.wrong_input()
        print('-' * 50)

        if num == 1:
            print("1. Show all existing contacts")
            print()

            while True:
                print()
                u_i.export_menu()
                op = excep.wrong_input()
                print('-' * 50)

                if op == 1:   
                    print("1. Show all existing contacts")
                    log.log_operation("1. Show all existing contacts -> 1. Show all existing contacts\n")
                    print(m_ex.show_all_cont())
                elif op == 2:
                    print("2. Load from .csv")
                    log.log_operation("1. Show all existing contacts -> 2. Load from .csv\n")
                    print(m_ex.read_csv())
                elif op == 3:
                    print("3. Load from .json")
                    log.log_operation("1. Show all existing contacts -> 3. Load from .json\n")
                    print(m_ex.read_json())
                elif op == 4:
                    print("4. Return to the Main menu")
                    break
                else:
                    print("Incorrect entry! Please, choose something from the list!")

        elif num == 2:
            print("2. Add new contact")
            log.log_operation("2. Add new contact")
            print(m_a.add_contact())
        elif num == 3:
            print("3. Delete contact")
            log.log_operation("3. Delete contact")
            print(m_d.delete_contact())
        elif num == 4:
            print("4. Search the existing contact")
            log.log_operation("4. Search the existing contact\n")
            print(m_s.search_contact())
        elif num == 5:
            print("5. Import contacts")

            while True:
                print()
                u_i.import_menu()
                op = excep.wrong_input()
                print('-' * 50)

                if op == 1:
                    print("1. Save to .csv")
                    log.log_operation("5. Import contacts -> 1. Save to .csv\n")
                    print(m_im.save_to_csv())
                elif op == 2:
                    print("2. Save to .json")
                    log.log_operation("5. Import contacts -> 2. Save to .json\n")
                    print(m_im.save_to_json())
                elif op == 3:
                    print("4. Return to the Main menu")
                    break
                else:
                    print("Incorrect entry! Please, choose something from the list!")

        elif num == 6:
            return "The programm has finished working."

        else:
            print("Incorrect entry! Please, choose something from the list!")
