"""
@author: diamo
Dia Modi, 501316072
Computer Science Project 

Problem Description: 
As a first-year university student, I am experiencing new responsibilities, one of which is managing my finances. 
Many university students face the challenge of budgeting and tracking their expenses for the first time. To address this, 
I aim to create a simple and easy-to-navigate budget tracker. This program will allow users to record their income and 
expenses with dates, categorize their spending, view transaction summaries, and set budget goals to help manage their finances 
effectively. The goal is to provide an accessible tool that supports students in building responsible financial habits.

In my code, I solve the problem by creating an interactive budget tracker that allows users to manage their finances 
effectively. First, I set up a file (budget_data.txt) to store income, expenses, and their categories, along with dates. 
To ensure proper functionality, I used functions such as load_transactions_from_file() to load previous transactions, 
display_menu() for user interaction, and clear_summary() to clear stored data when needed. When users add income or expenses,
the program updates the file with the appropriate details and adjusts the user's balance and remaining budget. Transactions are 
saved in a file, so the data is stored even after the program is closed. The program also checks for input validity, ensuring that only 
numerical values are entered for financial amounts, and alerts the user if an expense exceeds the current balance. 

Note: The 'budget_data.txt' file handles both input and output by storing all transactions and updates.
"""
#Budget Tracker Program

import datetime  # Added for date functionality

#User-defined function to display the main menu
def display_menu():
    print("\nBudget Tracker Menu")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transaction Summary")
    print("4. Clear Transaction Summary")
    print("5. Reset Budget")
    print("6. Set/Update Budget Goal")
    print("7. Exit")
    
#User-defined function to reset the budget data
def reset_budget():
    file = open("budget_data.txt", "w") #Open the file 'budget_data.txt' in write mode, which clears the file
    file.write("Income, Expense, Category, Date")  #Write the default header line to the file
    file.close() #Close the file to save changes
    print("Budget data reset successfully.")

#User-defined function to clear transaction summary
def clear_summary():
    file = open("budget_data.txt", "w")  #Open the file in write mode
    file.write("Income, Expense, Category, Date\n")  #Reset the file contents with headers
    file.close()  #Close the file after writing to save changes
    print("Transaction summary cleared.")

#User-defined function to load initial transactions from the file
def load_transactions_from_file():
    transactions = []  #Create an empty list to store all transactions
    
    try:
        file = open("budget_data.txt", "r") #Open the file in read mode
        file.readline()  #Read and ignore the first line (the header)
        for line in file:
            transactions.append(line.strip())  #Remove leading/trailing whitespaces from each line
        file.close() #Close the file after reading
        
        return transactions  #Return the list of transactions
    
    except FileNotFoundError:  #Handle the case where the file is not found
        print("File not found.")
        return []  #Return an empty list if the file is missing
    
#Initialize variables and set a budget goal
budget_goal = 0  #The target budget goal, initially set to 0. This is the amount you aim to spend/save.
current_balance = budget_goal  #The current balance, starts at the budget goal and will change as income/expenses are added.
remaining_budget = budget_goal  #The remaining amount of the budget that can still be used, also starts at the budget goal.

# Initialize file with headers if it does not already exist
try:
    file = open("budget_data.txt", "x")  #Try to create a new file 'budget_data.txt' if it doesn't exist
    file.write("Income, Expense, Category, Date\n")  #Write headers to the file
    file.close()  #Close the file after writing
    
except FileExistsError:
    pass #If the file already exists, do nothing

#Log the program start time
start_time = datetime.datetime.now()
print("Program started on " + str(start_time.date()))  #Display the start time to the user

# Main program loop
while True:
    display_menu() #Display the menu of options
    choice = input("Enter your choice: ") #Get the user's choice from the input

    if choice == "1":  #If the user selects option 1, Add Income
        try:
            income = float(input("Enter income amount: ")) #Get the income amount from the user and convert it to a float
            date = input("Enter the date (YYYY-MM-DD): ") #Get the date of the income entry from the user
            current_balance += income #Add the income to the current balance

            #Record income in the file
            file = open("budget_data.txt", "a")  #Open in append mode
            file.write(str(income) + ", 0, Income, " + date + "\n") #Write the income data to the file, including the amount, expense (0), category (Income), and date
            file.close()  #Close the file after writing

            print("Income of $" + str(income) + " added. Current balance: $" + str(current_balance))

        except ValueError:
            print("Invalid input. Please enter a valid number.") #If the user enters something that isn't a valid number, show an error message

    elif choice == "2":  #If the user selects option 2, Add Expense
        try:
            expense = float(input("Enter expense amount: ")) #Get the expense amount from the user and convert it to a float
            category = input("Enter the category of the expense (ex: groceries, miscellaneous): ") #Get the category of the expense from the user
            date = input("Enter the date (YYYY-MM-DD): ") #Get the date of the expense from the user

            if expense > current_balance:   
                print("Warning: Expense exceeds current balance!") #Display a warning if the expense exceeds the current balance
            else:
                current_balance -= expense #Subtract the expense from the current balance
                remaining_budget -= expense  #Subtract from remaining budget goal set by user

            # Record expense in the file
            file = open("budget_data.txt", "a") # Open the file in append mode to add new data without overwriting
            file.write("0, " + str(expense) + ",  " + category + ",  " + date + "\n") #Write the expense data to the file, including the amount, category, and date
            file.close()  #Close the file after writing

        except ValueError:
            print("Invalid input. Please enter a valid number.") #If the user enters something that isn't a valid number, show an error message

    elif choice == "3":  # View Summary
        print("\nTransaction Summary")

        try:
            file = open("budget_data.txt", "r")  #Open the file in read mode to read all of its contents
            for line in file:
                print(line.strip()) #Read and print each line in the file
            file.close()  #Close the file after reading

        except FileNotFoundError:
            print("No transactions found.") #If the file doesn't exist, inform the user that no transactions are recorded

        print("Current balance: " + str(current_balance))
        print("Remaining budget: " + str(remaining_budget))

    elif choice == "4":  #If the user selects option 4, Clear Transaction Summary
        clear_summary()

    elif choice == "5":  #If the user selects option 5, Reset Budget
        file = open("budget_data.txt", "w")
        file.write("Income, Expense, Category, Date")  #Write the default headers back into the file
        file.close()
        print("Budget data reset successfully.")
        
        current_balance = budget_goal #Reset the current balance to the budget goal
        remaining_budget = budget_goal #Reset the remaining budget to the budget goal
        print("Budget reset. Starting balance: $" + str(current_balance))

    elif choice == "6":  #If the user selects option 6, Set/Update Budget Goal
        try:
            new_goal = float(input("Enter your new budget goal: "))
            remaining_budget += new_goal - budget_goal  #Adjust remaining budget
            budget_goal = new_goal  #Update the budget goal
            print("Budget goal set to $" + str(budget_goal) + ". Remaining budget: $" + str(remaining_budget))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "7":  #If the user selects option 7, Exit
        print("Exiting Budget Tracker.")
        exit_time = datetime.datetime.now() #Log the program exit date
        print("Program exited on " + str(exit_time.date())) 
        break

    else: #If the user selects a value outside the range (1-7), they will receive an error message.
        print("Invalid choice. Please select a valid option.")
