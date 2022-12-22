
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1 = name1.lower()
n2 = name2.lower()

name = n1 + n2

c1 = name.count("t")
c2 = name.count("r")
c3 = name.count("u")
c4 = name.count("e")
c5 = name.count("l")
c6 = name.count("o")
c7 = name.count("v")
c8 = name.count("e")

count1 = c1 + c2 + c3 + c4
count2 = c5 + c6 + c7 + c8

cname = str(count1) + str(count2)
count = int(cname)

if count <10 or count > 90:
    print(f"Your score is {count}, you go together like coke and mentos.")
elif count > 40 and count < 50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")