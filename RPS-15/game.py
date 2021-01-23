import random

rating_dict = {}
name = None
combination = {"rock": {"scissors", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge"},
               "paper": {"rock", "gun", "lightning", "devil", "dragon", "water", "air"},
               "scissors": {"paper", "air", "sponge", "wolf", "tree", "human", "snake"},
               "gun": {"wolf", "tree", "human", "snake", "scissors", "fire", "rock"},
               "lightning": {"tree", "human", "snake", "scissors", "fire", "rock", "gun"},
               "devil": {"human", "snake", "scissors", "fire", "rock", "gun", "lightning"},
               "dragon": {"snake", "scissors", "fire", "rock", "gun", "lightning", "devil"},
               "water": {"scissors", "fire", "rock", "gun", "lightning", "devil", "dragon"},
               "air": {"fire", "rock", "gun", "lightning", "devil", "dragon", "water"},
               "sponge": {"gun", "lightning", "devil", "dragon", "water", "air", "paper"},
               "wolf": {"lightning", "devil", "dragon", "water", "air", "paper", "sponge"},
               "tree": {"devil", "dragon", "water", "air", "paper", "sponge", "wolf"},
               "human": {"dragon", "water", "air", "paper", "sponge", "wolf", "tree"},
               "snake": {"water", "air", "paper", "sponge", "wolf", "tree", "human"},
               "fire": {"paper", "sponge", "wolf", "tree", "human", "snake", "scissors"}
               }

rating = open('rating.txt', 'r')
for value in rating:
    rating_name, rating_score = value.split()
    rating_dict[rating_name] = int(rating_score)
rating.close()

# User name
def who_are_you():
    global name
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    if name not in rating_dict:
        rating_dict[name] = 0

# Choosing the list of option to start the game from combination dict
def game_mode():
    print(f"\nPlease choose the combination of game mode from this list by typing out the name (separate each word with comma):\n{[keys for keys in combination.keys()]}")
    print("\nIf you choose less then 3 game mode, default will be ['rock', 'paper', 'scissors']")
    option_lst = list(input('> ').split(','))
    option_lst = [ _.strip() for _ in option_lst]
    if len(option_lst) < 3:
        option_lst = ["rock", "paper", "scissors"]
        return option_lst
    else:
        return option_lst

# Update score to txt file
def update_score():
    print("Saving your score to rating file...")

    updated_rating_list = [f"{key} {score}\n" for key, score in rating_dict.items()]
    updated_rating_list = "".join(updated_rating_list)

    rating = open('rating.txt', 'w')
    rating.write(updated_rating_list)
    rating.close()

# Main block
def main():
    option = input('> ').strip()
    computer_option = random.choice(option_list)
    if option in option_list or option == "!exit" or option == "!score":
        if option in combination[computer_option]:
            rating_dict[name] -= 50
            print(f"Sorry, but the computer chose {computer_option}.\nYou lose 50 points.")
        elif option == computer_option:
            rating_dict[name] -= 25
            print(f"There is a draw ({computer_option}).\nYou lose 25 points.")
        elif option == "!score":
            print(f'Your score: {rating_dict[name]}')
        elif option == "!exit":
            update_score()
            print("Bye!")
            exit()
        else:
            rating_dict[name] += 100
            print(f"Well done. The computer chose {computer_option} and failed.\nYou gain 100 points.")
    else:
        print("Invalid input")



# Game starting...
who_are_you()
option_list = game_mode()
print("Okay, let's start")
while True:
    print(f"\nWrite action ({', '.join(option_list)}, !score, !exit)")
    main()