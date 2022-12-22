
age = input("What is your current age? ")


ag = int(age)

rem_days = (365*90)-(365*ag)
rem_weeks = (52*90)-(52*ag)
rem_months = (12*90)-(12*ag)

print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left.")
