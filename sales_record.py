import json as js
import inventory_file as invfile
import datetime
invfile.load_inventory()
record=[]
def sales():
    return record
def save_sales():
    global record
    with open("record.json","w") as f:
        js.dump(record,f,indent=4)
def load_sales():
    global record
    try:
        with open("record.json","r") as f:
            record=js.load(f)
    except FileNotFoundError :
        record=[]
