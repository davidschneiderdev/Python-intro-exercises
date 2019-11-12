
bill_total = float(input("Total bill amount? "))
service_level = input("Level of service (good, fair, bad)? ")

if service_level == 'good':
    tip_percentage = .2
elif service_level == 'fair':
    tip_percentage = .15
else:
    tip_percentage = .1
    
tip_amount = round(bill_total * tip_percentage, 2)
total_amount = bill_total + tip_amount

print(f"Tip amount: ${tip_amount}")
print(f"Total amount: ${total_amount}")





