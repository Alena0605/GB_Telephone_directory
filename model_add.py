import model_input as m_i
import excep
import log


def add_contact():
    data = m_i.data_input()
    file = excep.check_file()
    with open(file, 'a', encoding='utf-8') as f:
        f.write(data)
    log.log_data_input(data)
    return "The data are written."
