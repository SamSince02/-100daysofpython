

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill?"))

per_cen = int(input("What percentage tip you would like to give?10,12 or 15?"))

peps = int(input("How many people to split the bill?"))

bill = ((total_bill*(per_cen/100))+total_bill)/peps

print(round(bill,2))

