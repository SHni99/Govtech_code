#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculateTranscation(expenses, average):
    
    for name, amount in expenses.items():
        expenses[name] = amount - average
    
    #if negative, person (i) owe some people money
    payors = [(name, amount) for name, amount in expenses.items() if amount < 0]
    #if positive, other people need to return this amount to this person (i)
    recipients = [(name, amount) for name, amount in expenses.items() if amount > 0]
    
    #lowest to highest debts
    payors.sort(key=lambda x: x[1]) 
    
    #highest to lowest expenditure
    recipients.sort(key=lambda x: x[1], reverse=True)
    
    transactions = []

    # While there are payments to settle
    while payors and recipients:
        payor_name, payor_amount = payors[0]
        recipient_name, recipient_amount = recipients[0]

        # Determine the payment that consider the smaller value
        payment = min(-payor_amount, recipient_amount)

        # Update the amount
        payor_amount += payment
        recipient_amount -= payment
        
        # Record the transaction in words
        transactions.append(f"{payor_name} pays {recipient_name} ${payment:.2f}")

        # Update the payor 
        if payor_amount == 0:
            payors.pop(0)  # Payor is removed after his/her debt is cleared
        else:
            payors[0] = (payor_name, payor_amount)  # Update remaining debt has to be paid

        # Update the recipient
        if recipient_amount == 0:
            recipients.pop(0)  # Recipient has collected his debts fully
        else:
            recipients[0] = (recipient_name, recipient_amount)  # Update remaining amount that is needed

    return transactions

def main():
    
    try:
        number_of_people = int(input("Enter the number of people: "))
    except ValueError:
        print("Invalid input: Please enter a positive integer.")
        return
    
    # Number of people has to be more than 0 for the program to run
    if number_of_people <= 0:
        print("Invalid input: The number of people must be a positive integer.")
        
    
    expenses = {}
    totalAmount = 0

    for i in range(number_of_people):
        
        name = input(f"Enter person {i+1} name: ")
            
        try:
            expense = float(input(f"Enter the expense for {name}: "))
        except ValueError:
            print("Invalid input: Please enter a numeric value for expense.")
            break
        
        if expense < 0:
            print("The expense cannot be a negative integer. Please try again")
            break
            
        totalAmount += expense
        expenses[name] = expense
        
    averageAmount = round(float(totalAmount / number_of_people), 2)
    #print(averageAmount)
    
    result = calculateTranscation(expenses, averageAmount)
        
    print(f"Transcation history: {result}")
    print(f"Number of transcation: {len(result)}")
    
if __name__ == "__main__":
    main()


# ## Example scenario 10:
# 
# Alice, 10
# 
# Bob, 5.25
# 
# Charlie, 20
# 
# Dave, 50.50
# 
# Evan, 3.80
# 
# Felix, 0
# 
# 
# Example output 10:
# 
# 
# 
# 
# 
# ## Example scenario 1:
# 
# Alice paid $60
# 
# Bob paid $120
# 
# Charlie paid $30 
# 
# Example output 1:
# 
# Alice pays Bob $10.
# 
# Charlie pays Bob $40
# 
# Number of transactions: 2
# 
# 
# 
# 
# ## Example scenario 2:
# 
# Ali paid $10
# 
# Zack paid $30
# 
# Example output 2:
# 
# Ali pays Zack $10.
# 
# Number of transactions: 1
# 
# 
# 
# 
# 
# ##Example scenario 3:
# 
# Ali,40.105
# 
# Bob,40.105
# 
# Charlie,15.20
# 
# Example output 3:
# 
# Charlie pays Ali $8.30
# 
# Charlie pays Bob $8.30
# 
# Number of transactions: 2
# 
# 
# 
# ##Example scenario 4:
# 
# Ali,40
# 
# Bob,40
# 
# Charlie,10
# 
# Example output 4:
# 
# Charlie pays Ali $10
# 
# Charlie pays Bob $10
# 
# Number of transactions: 2
# 
# 
# ##Example scenario 5:
# 
# Ali,10
# 
# Bob,20
# 
# Charlie,0
# 
# Don,10
# 
# Example output 5:
# 
# Charlie pays Bob $10
# 
# Number of transactions: 1
# 
# 
# 
# Example scenario 6:
# 
# Alice,40
# 
# Bob,40
# 
# Charlie,10
# 
# Don,10
# 
# 
# Example output 6:
# 
# Charlie pays Alice $15
# 
# Don pays Bob $15
# 
# Number of transactions: 2
# 
# 
# 
# Example scenario 7:
# 
# Alice, 200
# 
# Bob, 80
# 
# Charlie, 50
# 
# Don, 20
# 
# Example output 7:
# 
# Bob pays Alice $7.50
# 
# Charlie pays Alice $37.50
# 
# Don pays Alice $67.50
# 
# Number of transactions: 3
# 
# 
# 
# Example scenario 8:
# 
# Alice, 160
# 
# Bob, 120
# 
# Charlie, 50
# 
# Don, 20
# 
# Example output 8:
# 
# Don pays Alice $67.50
# 
# Charlie pays Alice $5.00
# 
# Charlie pays Bob $32.50
# 
# Number of transactions:3
# 
# 
# Example scenario 9:
# 
# Alice, 0
# 
# Bob, 0
# 
# Charlie, 0
# 
# Don, 0
# 
# Evan, 0
# 
# Example output 9:
# 
# Transcation history: []
# Number of transcation: 0
# 
# 
# 
# 
# 

# In[ ]:





# In[ ]:




