
bill_total = float(input("Total bill amount? "))

service_list = ["good", "fair", "bad"]

entered_correctly = True
while entered_correctly:
    service_level = input("Level of service (good, fair, bad)? ")
    if service_level.lower() in service_list:
        entered_correctly = False
        if service_level == 'good':
            tip_percentage = .2
        elif service_level == 'fair':
            tip_percentage = .15
        else:
            tip_percentage = .1
    else: 
        print("Please enter either 'good', 'fair', or 'bad'.")

integer_entered = True    
while integer_entered:
    num_people = int(input("Split how many ways? "))
    else:
        print("Please enter a one or two digit number.")
  
tip_amount = round(bill_total * tip_percentage, 2)
total_amount = bill_total + tip_amount
split_amount = round((total_amount/num_people), 2)

print(f"Tip amount: ${tip_amount}")
print(f"Total amount: ${total_amount}")
print(f"Amount per person: ${split_amount}")