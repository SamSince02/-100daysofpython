import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_val = int(input("What do you choose?Type 0 for Rock, 1 for paper or 2 for scissors .\n"))

comp_val = random.randint(0,2)
print(comp_val)
user_list = [rock,paper,scissors]
comp_list = [rock,paper,scissors]
print(user_list[user_val])
print(comp_list[comp_val])

if user_list[user_val] == comp_list[comp_val]:
  print("Game Draw")
elif user_val==0 and comp_val== 1:
  print("You Lose,Better luck next time.")
elif user_val== 0 and comp_val == 2:
  print("You Win!")
elif user_val==1 and comp_val==0:
  print("You Win!")
elif user_val== 1 and comp_val== 2:
  print("You Lose,Better luck next time")
elif user_val== 2 and comp_val== 0:
  print("You Lose,better luck next time")
elif user_val== 2 and comp_val== 1:
  print("You Win!")
else:
  print("Invalid inputs")



