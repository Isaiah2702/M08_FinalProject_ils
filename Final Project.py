# Assignment: Final Project
# Author: Isaiah Snelling
# Created: 2024-26-11, Finished: 2024-14-12
# IDE: Visual Studio Code
# Pseudo Code:
# Initialize global variables to store income, expenses, and goals data.
# Define a function to show the home screen. Clear the screen, display the title, and add buttons to navigate to Income, Expenses, Goals, and Summary sections.
# Define a function to show the income section. Clear the screen, display input fields for income details, and add buttons to save income or return to the home screen.
# Define a function to save income data. Validate inputs, convert values to the correct format, save the data to the global list, show a confirmation message, and return to the home screen.
# Define a function to show the expenses section. Clear the screen, display input fields for expense details, and add buttons to save expenses or return to the home screen.
# Define a function to save expense data. Validate inputs, convert values to the correct format, save the data to the global list, show a confirmation message, and return to the home screen.
# Define a function to show the goals section. Clear the screen, display input fields for goal details, and add buttons to save goals or return to the home screen.
# Define a function to save goal data. Validate inputs, convert values to the correct format, save the data to the global list, show a confirmation message, and return to the home screen.
# Define a function to show the summary section. Clear the screen, calculate totals for income, expenses, and savings, display financial summary and goal progress, and add a button to return to the home screen.
# Define a function to clear the screen by removing all widgets from the main window.
# Initialize the main application window, set the title and size, and display the home screen on startup.
# Start the Tkinter main loop to run the application.


import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Global variables for storing data (to be replaced with a database in the future)
# income_data will hold all income entries as dictionaries
income_data = []  
# expenses_data will hold all expense entries as dictionaries
expenses_data = []  
# goals_data will hold all goals as dictionaries with target amount and deadlines
goals_data = []  


def show_home_screen():
    # This function clears the screen and shows the main menu with buttons to navigate
    # to different sections of the app (Income, Expenses, Goals, and Summary).

    # Clear any existing widgets
    clear_screen()  
    # Display the title label for the home screen
    tk.Label(root, text="Welcome to Budget Planner", font=("Arial", 16)).pack(pady=20)

    # Buttons to navigate to different sections of the application
    tk.Button(root, text="Income", width=15, command=show_income_section).pack(pady=10)
    tk.Button(root, text="Expenses", width=15, command=show_expenses_section).pack(pady=10)
    tk.Button(root, text="Goals", width=15, command=show_goals_section).pack(pady=10)
    tk.Button(root, text="Summary", width=15, command=show_summary_section).pack(pady=10)


def show_income_section():
    # This function clears the screen and displays the income input form where the user
    # can input income details such as source, amount, date, and if the income is recurring.

    # Clear any existing widgets
    clear_screen()  
    # Display the title label for the income section
    tk.Label(root, text="Income Section", font=("Arial", 16)).pack(pady=10)

    # Income source input
    tk.Label(root, text="Income Source:").pack(pady=5)
    source_entry = tk.Entry(root, width=30)
    source_entry.pack()

    # Income amount input
    tk.Label(root, text="Amount:").pack(pady=5)
    amount_entry = tk.Entry(root, width=30)
    amount_entry.pack()

    # Income date input, default to current date
    tk.Label(root, text="Date (YYYY-MM-DD):").pack(pady=5)
    date_entry = tk.Entry(root, width=30)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    date_entry.pack()

    # Checkbox for recurring income
    is_recurring = tk.BooleanVar()  # Boolean variable to track recurring income
    tk.Checkbutton(root, text="Recurring Income", variable=is_recurring).pack(pady=5)

    # Buttons to save the income or go back to home screen
    tk.Button(root, text="Save", width=10, command=lambda: save_income(source_entry.get(), amount_entry.get(), date_entry.get(), is_recurring.get())).pack(pady=10)
    tk.Button(root, text="Back", width=10, command=show_home_screen).pack(pady=10)


def save_income(source, amount, date, recurring):
   # This function validates the income input fields, converts the values into appropriate types,
   # and then saves the income entry to the global list.

    if not source or not amount or not date:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        # Convert amount to float
        amount = float(amount)  
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    try:
        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")  
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    # Append the validated income data to the global list
    income_data.append({"source": source, "amount": amount, "date": date, "recurring": recurring})
    recurring_text = "Recurring" if recurring else "One-Time"
    messagebox.showinfo("Success", f"Income saved:\n\nSource: {source}\nAmount: ${amount}\nDate: {date}\nType: {recurring_text}")
    show_home_screen()


def show_expenses_section():
    # This function clears the screen and displays the expense input form where the user
    # can input details for their expenses such as type, amount, date, category, and if the expense is recurring.

    # Clear any existing widgets
    clear_screen()  
    # Display the title label for the expenses section
    tk.Label(root, text="Expenses Section", font=("Arial", 16)).pack(pady=10)

    # Expense type input
    tk.Label(root, text="Expense Type:").pack(pady=5)
    type_entry = tk.Entry(root, width=30)
    type_entry.pack()

    # Expense amount input
    tk.Label(root, text="Amount:").pack(pady=5)
    amount_entry = tk.Entry(root, width=30)
    amount_entry.pack()

    # Expense date input, default to current date
    tk.Label(root, text="Date (YYYY-MM-DD):").pack(pady=5)
    date_entry = tk.Entry(root, width=30)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    date_entry.pack()

    # Expense category input
    tk.Label(root, text="Category:").pack(pady=5)
    category_entry = tk.Entry(root, width=30)
    category_entry.pack()

    # Checkbox for recurring expense
    is_recurring = tk.BooleanVar()  # Boolean variable to track recurring expense
    tk.Checkbutton(root, text="Recurring Expense", variable=is_recurring).pack(pady=5)

    # Buttons to save the expense or go back to home screen
    tk.Button(root, text="Save", width=10, command=lambda: save_expense(type_entry.get(), amount_entry.get(), date_entry.get(), category_entry.get(), is_recurring.get())).pack(pady=10)
    tk.Button(root, text="Back", width=10, command=show_home_screen).pack(pady=10)


def save_expense(expense_type, amount, date, category, recurring):
    # This function validates the expense input fields, converts the values into appropriate types,
    # and then saves the expense entry to the global list.
  
    if not expense_type or not amount or not date or not category:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        # Convert amount to float
        amount = float(amount)  
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    try:
        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")  
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    # Append the validated expense data to the global list
    expenses_data.append({"type": expense_type, "amount": amount, "date": date, "category": category, "recurring": recurring})
    recurring_text = "Recurring" if recurring else "One-Time"
    messagebox.showinfo("Success", f"Expense saved:\n\nType: {expense_type}\nAmount: ${amount}\nDate: {date}\nCategory: {category}\nType: {recurring_text}")
    show_home_screen()


def show_goals_section():
    # This function clears the screen and displays the goals input form where the user
    # can input details for their financial goals such as name, target amount, and deadline.

    # Clear any existing widgets
    clear_screen()  
    # Display the title label for the goals section
    tk.Label(root, text="Goals Section", font=("Arial", 16)).pack(pady=10)

    # Goal name input
    tk.Label(root, text="Goal Name:").pack(pady=5)
    goal_name_entry = tk.Entry(root, width=30)
    goal_name_entry.pack()

    # Target amount input
    tk.Label(root, text="Target Amount:").pack(pady=5)
    target_amount_entry = tk.Entry(root, width=30)
    target_amount_entry.pack()

    # Deadline input for the goal, default to current date
    tk.Label(root, text="Deadline (YYYY-MM-DD):").pack(pady=5)
    deadline_entry = tk.Entry(root, width=30)
    deadline_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    deadline_entry.pack()

    # Buttons to save the goal or go back to home screen
    tk.Button(root, text="Save", width=10, command=lambda: save_goal(goal_name_entry.get(), target_amount_entry.get(), deadline_entry.get())).pack(pady=10)
    tk.Button(root, text="Back", width=10, command=show_home_screen).pack(pady=10)

def save_goal(name, target_amount, deadline):
    # This function validates the goal input fields, converts the values into appropriate types,
    # and then saves the goal entry to the global list.

    if not name or not target_amount or not deadline:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        # Convert target amount to float
        target_amount = float(target_amount)  
    except ValueError:
        messagebox.showerror("Error", "Target amount must be a number.")
        return

    try:
        # Validate date format
        datetime.strptime(deadline, "%Y-%m-%d")  
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    # Append the validated goal data to the global list
    goals_data.append({"name": name, "target_amount": target_amount, "deadline": deadline})
    messagebox.showinfo("Success", f"Goal saved:\n\nName: {name}\nTarget Amount: ${target_amount}\nDeadline: {deadline}")
    show_home_screen()

def show_summary_section():
    # This function clears the screen and shows a summary of the user's financial status:
    # total income, total expenses, net savings, and goal progress.

    # Clear any existing widgets
    clear_screen()  
    # Display the title label for the summary section
    tk.Label(root, text="Summary Section", font=("Arial", 16)).pack(pady=10)

    # Calculate and display total income
    income_total = sum(item["amount"] for item in income_data)
    tk.Label(root, text=f"Total Income: ${income_total:.2f}", font=("Arial", 12)).pack(pady=5)

    # Calculate and display total expenses
    expenses_total = sum(item["amount"] for item in expenses_data)
    tk.Label(root, text=f"Total Expenses: ${expenses_total:.2f}", font=("Arial", 12)).pack(pady=5)

    # Calculate and display net savings
    net_savings = income_total - expenses_total
    tk.Label(root, text=f"Net Savings: ${net_savings:.2f}", font=("Arial", 12)).pack(pady=5)

    # Calculate and display goal progress
    if goals_data:
        tk.Label(root, text="Goals Progress:", font=("Arial", 12)).pack(pady=5)
        for goal in goals_data:
            progress = (income_total - expenses_total) / goal["target_amount"] * 100
            # Ensure progress is between 0% and 100%
            progress = min(max(progress, 0), 100)  
            tk.Label(root, text=f"{goal['name']}: {progress:.2f}% completed", font=("Arial", 10)).pack(pady=2)
    else:
        tk.Label(root, text="No goals set.", font=("Arial", 10)).pack(pady=5)

    # Button to go back to the home screen
    tk.Button(root, text="Back", width=10, command=show_home_screen).pack(pady=20)

def clear_screen():
   # This function removes all widgets from the main window to prepare for displaying
   # new sections of the app.

    for widget in root.winfo_children():
        widget.destroy()

# Initialize the main application window
root = tk.Tk()
root.title("Budget Planner")
root.geometry("400x500")

# Show the home screen on startup
show_home_screen()

# Start the Tkinter main loop
root.mainloop()
