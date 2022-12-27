from art import logo
import random


if input("Do you wanna play a game of Blackjack ? Type 'y' or 'n'") == "y":

  print(logo)

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards = []
  comp_cards = []
  
  user_choice1 = random.choice(cards)
  user_choice2 = random.choice(cards)

  user_cards.append(user_choice1)
  user_cards.append(user_choice2)


  user_sum = sum(user_cards)
  
  comp_choice1 = random.choice(cards)

  comp_cards.append(comp_choice1)
  
  comp_sum = sum(comp_cards)
  
  print(f"Your cards : {user_cards}, current score : {user_sum}")
  
  print(f"Computer's first card : {comp_choice1}")
  should_continue = True
  while sum(user_cards)< 21 or sum(comp_cards) < 21:
    should_continue = True
    choice = input("Type 'y' to get another card,type 'n' to pass : ")
    
    if choice == "y":

        user_choice = random.choice(cards)
        user_cards.append(user_choice)
        user_sum = sum(user_cards)
        if sum(user_cards)>21:
            print(f"Your cards : {user_cards}, current score : {user_sum}")
            print(f"Computer's cards : {comp_cards}, current score : {comp_sum}")
            print(f"Your final hand : {user_cards}, current score : {user_sum}")
            print(f"Computer's final hand : {comp_cards}, current score : {comp_sum}")
            print("You Lose")
            should_continue=False
            break
        elif sum(user_cards)<=21 and sum(user_cards)!= sum(comp_cards):
            print(f"Your cards : {user_cards}, current score : {user_sum}")
            print(f"Computer's cards : {comp_cards}, current score : {comp_sum}")
            print(f"Your final hand : {user_cards}, current score : {user_sum}")
            print(f"Computer's final hand : {comp_cards}, current score : {comp_sum}")
            should_continue = True
    else:
        comp_choice = random.choice(cards)
        comp_cards.append(comp_choice)
        comp_sum = sum(comp_cards)
        if sum(comp_cards)>21:
            print(f"Your cards : {user_cards}, current score : {user_sum}")
            print(f"Computer's cards : {comp_cards}, current score : {comp_sum}")
            print(f"Your final hand : {user_cards}, current score : {user_sum}")
            print(f"Computer's final hand : {comp_cards}, current score : {comp_sum}")
            print("You Win")
            should_continue = False
            break
        elif sum(comp_cards)<21:
            if sum(user_cards)>sum(comp_cards):
                print(f"Your cards : {user_cards}, current score : {user_sum}")
                print(f"Computer's cards : {comp_cards}, current score : {comp_sum}")
                print(f"Your final hand : {user_cards}, current score : {user_sum}")
                print(f"Computer's final hand : {comp_cards}, current score : {comp_sum}")
                print("You win")
                should_continue=False
                break
            elif sum(user_cards)<sum(comp_cards):
                print(f"Your cards : {user_cards}, current score : {user_sum}")
                print(f"Computer's cards : {comp_cards}, current score : {comp_sum}")
                print(f"Your final hand : {user_cards}, current score : {user_sum}")
                print(f"Computer's final hand : {comp_cards}, current score : {comp_sum}")
                print("You Lose")
                should_continue = False
                break
        elif sum(comp_cards)==21 and sum(comp_cards)!=sum(user_cards):
                print(f"Your cards : {user_cards}, current score : {user_sum}")
                print(f"Computer's cards : {comp_cards}, current score : {comp_sum}")
                print(f"Your final hand : {user_cards}, current score : {user_sum}")
                print(f"Computer's final hand : {comp_cards}, current score : {comp_sum}")
                print("You Lose")
                should_continue=False
                break

