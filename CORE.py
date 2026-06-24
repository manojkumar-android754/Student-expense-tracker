print("--- Student Expense Tracker Started ---")

budget = int(input("Enter your monthly budget limit (in Rs.): "))
total_spent = 0

print(f"Your monthly budget limit is: Rs. {budget}")

while True:
    print("\n-------------------------------")
    user_input = input("Enter expense amount (or type 'exit' to stop): ")
    
    #  if the user wants to quit
    if user_input.lower() == 'exit':
        print("Saving your report and closing tracker...")
        with open("expense_report.txt", "w") as file:
            file.write("--- STUDENT EXPENSE REPORT ---\n")
            file.write(f"Initial Budget: Rs. {budget}\n")
            file.write(f"Total Amount Spent: Rs. {total_spent}\n")
            file.write(f"Final Remaining Balance: Rs. {budget - total_spent}\n")
        print("✅ 'expense_report.txt' saved successfully!")
        break
        
    # --- MATH BLOCK ---
    expense = int(user_input)
    total_spent = total_spent + expense
    remaining = budget - total_spent
    
    print(f"Total Spent so far: Rs. {total_spent}")
    
    if total_spent > budget:
        print(f"⚠️ WARNING: You crossed your budget by Rs. {total_spent - budget}!")
    else:
        print(f"✅ Success! You have Rs. {remaining} left.")