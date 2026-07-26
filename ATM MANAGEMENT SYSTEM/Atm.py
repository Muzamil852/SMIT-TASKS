accounttitle = "Yasir Ali"
accountbalance = 22000

useracc = input("Enter account number: ")
pincode = input("Insert pin: ")

with open('data.csv', 'r') as file:
    for line in file.readlines():
        data = line.strip().split(',')
        if data[2] == useracc and data[3] == pincode:
            while True:
                print("Welcome " + data[0] + " \n 1. View account balance \n 2. Withdraw \n 3. Deposit \n 0. Exit")
                for i in range(3):
                    try:
                        user_input = input("Enter option to proceed : ")
                        break
                    except:
                        print(f"Error {i+1}: Enter a number only!!!")
                else:
                    print("Your Card has been taken")
                    break
                try:
                    if user_input == "1" :
                        print("Account Balance: ", data[1])

                    elif user_input == "2":
                        withdraw_amount = int(input("Enter amount to withdraw: "))
                        if withdraw_amount <= int(data[1]) and withdraw_amount % 500 == 0 and withdraw_amount > 0:
                            data[1] = str(int(data[1]) - withdraw_amount)
                            with open("data.csv", "r") as file:
                                lines = file.readlines()
                            with open("data.csv", "w") as file:
                                for line in lines:
                                    row = line.strip().split(",")
                                    if row[2] == useracc and row[3] == pincode:
                                        row[1] = data[1]
                                    file.write(",".join(row) + "\n")

                        else:
                            print("Incorrect Amount") 
                       
                    elif user_input == "3":
                        deposit_amount = int(input("Enter amount to Deposit: "))
                        data[1] = str(int(data[1]) + deposit_amount)
                        with open("data.csv", "r") as file:
                            lines = file.readlines()
                        with open("data.csv", "w") as file:
                            for line in lines:
                                row = line.strip().split(",")
                                if row[2] == useracc and row[3] == pincode:
                                    row[1] = data[1]
                                file.write(",".join(row) + "\n")
                       
                    elif user_input == "0":
                        break

                    else:
                        print("Wrong Option")
                except:
                    print("Invalid Input")

    else:
            print("USer not found")




