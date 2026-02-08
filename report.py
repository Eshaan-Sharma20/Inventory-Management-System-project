 import inventory_file as inf
import sales as sl

def sales_repo(nm,sale):
    items=inf.storage()
    item=items[nm]
    stock=item["qty"]
    if nm not in items:
        print("item not in inventory")
        return False
    if sale>stock:
        print("not enough stock.Sorry for the inconvinience")
        return False
    item["qty"]-=sale
    cost=item["cp"]
    price=item["sp"]
    profit=sl.prof(cost,price,sale)
    item["total_profit"]+=profit
    return True



