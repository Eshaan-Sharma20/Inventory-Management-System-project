 # 📌 Inventory Management System

## 🟢 Project Title
**Inventory Management System for Small Business Owners**

---

## 🟣 Overview of the Project
This project is a beginner-friendly Python application that helps small shop owners manage their inventory using a simple terminal interface. Users can add items, update existing items, record sales, calculate profit/loss automatically, and generate useful reports — all without using external libraries or databases.  
The system temporarily stores data in memory during runtime, making it ideal for academic demonstration of Python fundamentals such as functions, dictionaries, conditionals, loops, and modular programming.

---

## ⭐ Features
| Category | Description |
|---------|-------------|
| Add Item | Insert new stock with cost price, selling price & quantity |
| Update Item | Modify CP / SP / quantity of existing products |
| Record Sale | Reduce quantity and calculate profit/loss |
| Inventory Report | View full list of items, stock & prices |
| Low Stock Alert | View items with quantity < 30 units |
| Profit Report | View individual & overall profit/loss summary |

---

## 🛠 Technologies / Tools Used
| Type | Tool |
|------|------|
| Programming Language | Python |
| Libraries | None (no external dependencies) |
| Storage | In-memory dictionary |
| Execution | Command Line / Terminal |

---

## ▶️ Steps to Install & Run the Project
1️⃣ Download/clone the repository  
2️⃣ Make sure all `.py` files are in the **same folder**  
3️⃣ Open terminal / command prompt inside that folder  
4️⃣ Run the program using:
python main.py

Instructions for Testing

To test the project manually:
Start the program and choose Add Item
Add at least 2–3 products
Choose View Inventory to verify items
Choose Update Item and modify values
Choose Record Sale to reduce quantity and calculate profit/loss
Generate:
Low Stock Report
Profit Report
Inventory Report
Expected behaviour:
No duplicate items should be added
Quantity should decrease after sale
Profit/loss should update correctly
Low-stock items should display only when qty < 30
