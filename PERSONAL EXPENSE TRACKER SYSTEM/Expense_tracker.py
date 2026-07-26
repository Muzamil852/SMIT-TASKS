import csv
def add_expense():
    date = input("Enter Date (DD/MM/YY):")
    category = input("Enter Category(Food,Travel,Shopping etc): ")
    amount = int(input("Enter amount spent: "))
    expense = [date,category,amount]
    with open("data.csv",'a',newline="")as file:
        writer = csv.writer(file)
        writer.writerow(expense)
    print("Expense Added Successfully.")

def view_all_expense():
    with open("data.csv",'r')as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split(",")
            print(f"Date: {line[0]}")
            print(f"Category: {line[1]}")
            print(f"Amount spent: {line[2]}")
            print("="*20)           

def total_expense():
    expense_sum = 0
    with open("data.csv",'r')as file:
        lines = file.readlines()
        if not lines:
            print("No Expenses Found")
        else:
            for line in lines:
                line = line.strip().split(',')
                expense_sum +=  int(line[2])
            print(f"Total Money Spent: {expense_sum}")

def search_by_category():
    category_to_search = input("Enter category: ")
    found = False
    with open("data.csv",'r')as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split(',')
            if category_to_search.lower() == line[1].lower():
                print(f"Date: {line[0]}")
                print(f"Amount Spent: {line[2]}")
                print("-"*5)
                found = True
        if not found:
           print("No Category Found.")

while True:
    print("=====Personal Expense Tracker===== \n\n1.Add Expense\n2.View Expense\n3.Search by Category\n4.Total Expense\n5.Exit")
    try:
        user_input = int(input("Choose option: "))
        if user_input == 1:
            add_expense()
        elif user_input == 2:
            view_all_expense()
            print()
        elif user_input == 3:
            search_by_category()
            print()
        elif user_input == 4:
            total_expense()
            print()
        elif user_input == 5:
            break
        else:
            print("Invalid Option")
    except ValueError:
        print("Enter number only")