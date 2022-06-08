'''
Here is final project
'''
print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you  like to give ? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))
total_bill_with_tip = tip/100 * bill + bill
pay = (f"Each person should pay: ${total_bill_with_tip/7}")
print(pay)