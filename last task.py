import sqlite3


def create_table():
    taefe = sqlite3.connect('expenses.db')
    c = taefe.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS Expenses (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    category TEXT,
                    amount REAL,
                    description TEXT
                )''')

    taefe.commit()
    taefe.close()

def add_expense(date, category, amount, description):
    taefe = sqlite3.connect('expenses.db')
    c = taefe.cursor()
    
    c.execute("INSERT INTO Expenses (date, category, amount, description) VALUES (?, ?, ?, ?)", (date, category, amount, description))
    
    taefe.commit()
    taefe.close()

def view_expenses():
    taefe = sqlite3.connect('expenses.db')
    c = taefe.cursor()
    
    c.execute("SELECT * FROM Expenses")
    expenses = c.fetchall()
    
    for expense in expenses:
        print(expense)
    
    taefe.close()

def update_expense(id, date, category, amount, description):
    taefe = sqlite3.connect('expenses.db')
    c = taefe.cursor()
    
    c.execute("UPDATE Expenses SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?", (date, category, amount, description, id))
    
    taefe.commit()
    taefe.close()

def delete_expense(id):
    taefe = sqlite3.connect('expenses.db')
    c = taefe.cursor()
    
    c.execute("DELETE FROM Expenses WHERE id = ?", (id,))
    
    taefe.commit()
    taefe.close()

def main_menu():
    create_table()
    
    while True:
        print("Personal Expenses Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date: ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully!")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            id = input("Enter expense id to update: ")
            date = input("Enter new date: ")
            category = input("Enter new category: ")
            amount = float(input("Enter new amount: "))
            description = input("Enter new description: ")
            update_expense(id, date, category, amount, description)
            print("Expense updated successfully!")
        elif choice == '4':
            id = input("Enter expense id to delete : ")
            delete_expense(id)
            print("Expense deleted successfully ")
        elif choice == '5':
            break
        else:
            print("Invalid choice Please try again.")

main_menu()