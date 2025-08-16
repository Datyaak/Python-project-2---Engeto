"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Adam Pončík
email: adam.poncik47@gmail.com
"""
import random
interval = range(1000, 10000)
computer_num = random.choice(interval)

# Eliminuje duplicity ve vygenerovaném čísle
while len(set(list(str(computer_num)))) < 4:
    computer_num = random.choice(interval)

computer_num_list = list(str(computer_num))

print(f"""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------""")
player_input = input('Enter a number: ')
print("""-----------------------------------------------
""")
player_num = list(str(player_input))
bulls = 0
cows = 0
guess_num = 0


# vyhodnocování podmínek
while bulls < 4:
    bulls = 0
    cows = 0
    player_num = list(str(player_input))

# ošetření znaků a mezer v inputech
    while True:
        if player_input == "":
            player_input = input("Invalid input, please try again: ")
        elif player_num[0] == " " or player_num[-1] == " ":
            player_input = input("Invalid input, please try again: ")
        
        try:
            int(player_input)
            break
        except ValueError:
            player_input = input("Invalid input, please try again: ")

# splnění podmínek čísla
    if len(str(player_input)) != 4:
        player_input = input("Number must be exactly 4 digits long, try again: ")
        continue
    elif int(player_input) < 1000:
        player_input = input("Number mustn't start with zero, try again: ")
        continue
    elif len(set(list(str(player_input)))) < 4:
        player_input = input("The number mustn't contain duplicities, try again: ")
        continue

# Vyhodnocení bulls / cows
    for p in player_num:
        if p in computer_num_list:
            if player_num.index(p) == computer_num_list.index(p):
                bulls += 1
            else:
                 cows += 1
        else:
            continue
    if bulls < 4:
        if bulls == 1 and cows == 1:
            player_input = input(f"""-----------------------------------------------
There is 1 bull and 1 cow in your number. Try again: """)
            guess_num += 1
            continue
        elif bulls == 1:
            player_input = input(f"""-----------------------------------------------
There is 1 bull and {cows} cows in your number. Try again: """)
            guess_num += 1
            continue
        elif cows == 1:
            player_input = input(f"""-----------------------------------------------
There are {bulls} bulls and 1 cow in your number. Try again: """)
            guess_num += 1
            continue
        
        player_input = input(f"""-----------------------------------------------
There are {bulls} bulls and {cows} cows in your number. Try again: """)
        guess_num += 1
        continue

    else:
        guess_num += 1
        continue

if guess_num ==1:
    print(f"""-----------------------------------------------
Correct, you've guessed the right number in {guess_num} guess!
-----------------------------------------------
That's amazing!""")
else:
    print(f"""-----------------------------------------------
Correct, you've guessed the right number in {guess_num} guesses!
-----------------------------------------------
That's amazing!""")