
import art
import random
import game_data as gd
import os

print(art.logo)

choiceA = random.choice(gd.data)
Adisplay = choiceA["name"]+ ", a " + choiceA["description"] + ", from " + choiceA["country"]

print(f"Comapare A : {Adisplay}")

print(art.vs)

choiceB = random.choice(gd.data)
Bdisplay = choiceB["name"]+ ", a " + choiceB["description"] + ", from " + choiceB["country"]

print(f"Against B : {Bdisplay}")

value = input("Who has more followers?Type 'A' or 'B'")
current_score = 0
while True:
  if choiceA["follower_count"]>choiceB["follower_count"]:
    current_score+=1
    os.system("clear")
    print(art.logo)
    print(f"You're right! current score : {current_score}")
    Bdisplay = choiceB["name"]+ ", a " + choiceB["description"] + ", from " + choiceB["country"]
    print(f"Comapare A : {Bdisplay}")
    print(art.vs)
    choiceC = random.choice(gd.data)
    Cdisplay = choiceC["name"]+ ", a " +choiceC["description"] + ", from " + choiceC["country"]
    print(f"Against B : {Bdisplay}")
    break
  else:
    os.system("clear")
    print(f"Sorry! You got it wrong . Final score : {current_score}")
    break
