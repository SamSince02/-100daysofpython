print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

dir = input("You're at the cross road.Where do you want to go?Type 'Left' or 'Right'\n")
dir_ection = dir.lower()
if dir_ection == "left" or dir_ection == 'l':
  what_to_do = input("You've come to the lake.There is an island in the middle of teh lake.Type 'wait' to wait for a boat.Type 'swim'to swim across\n")
  if what_to_do == "wait":
    color = input("You arrive at the island unharmed.There is a house with 3 doors.One red, One blue and One yellow.Which color do you choose?\n")
    if color == "red":
      print("It's a room full of fire.Game Over.")
    elif color == "yellow":
      print("You found the Tresure!.You Win!")
    elif color == "blue":
      print("You enter a room of beasts.Game Over.")
    else:
      print("You chose the door that doesn't exist.Game Over.")
  else:
    print("You get attacked by an angry tout.Game Over.")
else:
  print("You fell into a hole.Game over.")
    