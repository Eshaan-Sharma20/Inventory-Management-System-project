 import inventory_file
import report as rp
import sales_record as sr
from datetime import date,datetime,timedelta
inventory_file.load_inventory()
sr.load_sales()
def main_menu():
    while True :
        print("-" * 51)
        print(f"{"INVENTORY MANAGEMENT SYSTEM":^51}")
        print("-"*51)
        print("1-> add item")
        print("2-> show inventory")
        print("3-> report a sale")
        print("4-> show reports")
        print("5-> advanced options")
        print("6-> Exit")
        print("-" * 51)
        choice=input("enter your choice: ")
        if choice=="1":
            add_item()
        if choice=="2":
            show_inventory()
        if choice=="3":
            report_sale()
        if choice=="4":
            show_reports()
def add_item():
    print("-" * 51)
    print(f"{"ADD ITEM":^51}")
    print("-" * 51)
    name=input("enter the item name: ")
    cp = float(input("enter the cost price: "))
    sp = float(input("enter the selling price: "))
    quantity=int(input("enter the quantity: "))
    if inventory_file.add_items(name,cp,sp,quantity):
         print("Item added to the inventory successfully")
         inventory_file.save_inventory()
    else:
        print("Item already exist")
def show_inventory():
    items = inventory_file.storage()
    if not items:
        print("No Items in Inventory Yet")
        return
    print("="*52)
    print(f"{"INVENTORY":^51}")
    print("-" * 51)
    #print("S.No\t\tItem\t\tCost Price\t\tSelling Price\t\tQuantity")
    print(f"{'S.No':<8}{'Items':<15}{'CP':>7}{'SP':>7}{'Quantity':>13}")
    print("-"*51)
    a = 1
    for item_name, item_data in items.items():# item name is a key and item data woh dictionary hai us key waale naam ki dictionary ki values ko store krta hai
        print(f"{str(a):<8}{item_data["name"]:<15}{item_data["cp"]:>7}{item_data["sp"]:>7}{item_data["qty"]:>13}")
        a += 1
def report_sale():
    print("-" * 51)
    print(f"{'REPORT A SALE':^51}")
    print("-" * 51)
    name = input("enter the item name: ")
    quantity = int(input("enter the quantity sold: "))
    items = inventory_file.storage()
    cp = items[name]["cp"]
    sp = items[name]["sp"]
    profit = (sp - cp) * quantity

    if rp.sales_repo(name,quantity):
        sale = {
            "item": name,
            "qty": quantity,
            "profit":profit,
            "date": date.today().isoformat()#coverts the python format to string format

        }
        sales=sr.sales()
        sales.append(sale)
        sr.save_sales()
        print("Sales recorded.Good job")
        inventory_file.save_inventory()
    else:
        print("Sales not recorded")
def show_reports():
    print("-" * 51)
    print(f"{'BUSINESS REPORTS':^51}")
    print("-" * 51)
    print(f"{'1-> SALES SUMMARY':^51}")
    print(f"{'2-> INVENTORY INSIGHTS':^51}")
    print(f"{'3-> DETAILED SALES TABLE':^51}")
    print("=" * 51)
    global choice
    choice=input("enter a choice: ")
    if choice=="1" or choice=="3":
        report_type()
def report_type():
    print("-" * 51)
    print(f"{'TYPE OF REPORT':^51}")
    print("-" * 51)
    print(f"{'1-> TODAY':^51}")
    print(f"{'2-> YESTERDAY':^51}")
    print(f"{'3-> PAST WEEK':^51}")
    print(f"{'4-> PAST MONTH':^51}")
    print(f"{'5-> PAST YEAR':^51}")
    print(f"{'6-> LIFETIME':^51}")
    print(f"{'7-> ENTER MANUALLY':^51}")
    print("=" * 51)
    timespan = input("enter a choice: ")
    if timespan =="7":
        strtdate=input("starting date: ")
        enddate=input("ending date: ")



main_menu()
