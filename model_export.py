import excep
import csv
import json
from tabulate import tabulate
from os import path
from time import ctime


def read_data(file_name = 'Contacts.txt'):
    with open(file_name, 'r', encoding='utf-8') as f:
        table = []
        for line in f:
            table.append(line.split())
    return table


def show_all_cont(): 
    file_name = excep.check_file()
    with open(file_name, 'r', encoding='utf-8') as f:
        table = []
        for line in f:
            table.append(line.split())
    print()
    return tabulate(table, headers=['Surname', 'Name', 'Phone', 'Comment'])


def read_csv():
    file_name = excep.check_file()
    ti_c = path.getctime(file_name)
    ti_m = path.getmtime(file_name)

    with open(file_name, 'r', encoding='utf-8') as f:
        reader_file = csv.reader(f)
        table = []
        for row in reader_file:
            table.append(row)
    
    print(table)
    return f"The file was created {ctime(ti_c)} and was last modified {ctime(ti_m)}"


def read_json():
    file_name = excep.check_file()
    ti_c = path.getctime(file_name)
    ti_m = path.getmtime(file_name)
    
    with open(file_name, 'r', encoding='utf-8') as f_json:
        print(json.load(f_json))
    
    return f"The file was created {ctime(ti_c)} and was last modified {ctime(ti_m)}"
