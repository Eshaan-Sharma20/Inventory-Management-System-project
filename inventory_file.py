 import json as js


inventory={}
def add_items(nm,cp,sp,quan):
    if nm in inventory:
        return False
    inventory[nm] = {
        "name": nm,
        "cp": cp,
        "sp": sp,
        "qty": quan,
        "total_profit": 0.0
    }
    return True
def storage():
    return inventory
def save_inventory():
    global inventory
    with open("inventory.json","w") as f:
        js.dump(inventory,f,indent=4)
def load_inventory():
    global inventory
    try:
        with open("inventory.json","r") as f:
            inventory=js.load(f)
    except FileNotFoundError :
        inventory={}


