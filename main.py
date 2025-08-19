"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Adam Pončík
email: adam.poncik47@gmail.com
"""
import random

# Definované konstanty
req_num_length = 4  # počet cifer v hádaném čísle, lze snadno měnit obtížnost hry
min_val = 10 ** (req_num_length - 1)  # spodní hranice intervalu n ciferného čísla
max_val = 10 ** (req_num_length)      # horní hranice intervalu n ciferného čísla (exkluzivní pro range)
interval = range(min_val, max_val)
separator = "-" * 47  # oddělovač řádků

# Generování n ciferného čísla neobsahující duplicity
def generate_number():
    computer_num = random.choice(interval)
    while len(set(str(computer_num))) < req_num_length:
        computer_num = random.choice(interval)
    return str(computer_num)

def validate_input(inp: str):
    """
    Ověřuje správný formát vstupu --> čtyřciferné celé číslo, které
    nezačíná nulou a neobsahuje dvě stejné číslice

    Vrací boolean hodnotu True, pokud je uživatelský input v pořádku.
    V případě problému vrátí False, doplněný o string, který
    specifikuje problém.
    """
    if inp == "":
        return False, "Invalid input, please try again: "
    try:
        int(inp)
    except ValueError:
        return False, "Invalid input, please try again: "
    if len(inp) != req_num_length:
        return False, f"Number must be exactly {req_num_length} digits long, try again: "
    elif int(inp) < min_val:
        return False, "Number mustn't start with zero, try again: "
    elif len(set(inp)) < req_num_length:
        return False, "The number mustn't contain duplicities, try again: "
    return True, None

def evaluate_guess(comp_num: str, guess: str):
    bulls = 0
    cows = 0
    for i, p in enumerate(guess):
        if p == comp_num[i]:
            bulls += 1
        elif p in comp_num:
            cows += 1
    return bulls, cows

def result_message(bulls: int, cows: int):
    """
    Vrací string, který při neúspěšném pokusu o uhodnutí specifikuje
    výskyt "bulls" a "cows". Výstup zohledňuje jednotné a množné čísla
    anglické gramatiky.
    """
    if bulls == 1 and cows == 1:
        return f"""{separator}
There is 1 bull and 1 cow in your number. Try again: """
    elif bulls == 1:
        return f"""{separator}
There is 1 bull and {cows} cows in your number. Try again: """
    elif cows == 1:
        return f"""{separator}
There are {bulls} bulls and 1 cow in your number. Try again: """
    else:
        return f"""{separator}
There are {bulls} bulls and {cows} cows in your number. Try again: """

def print_intro():
    print(f"""
Hi there!
{separator}
I've generated a random {req_num_length} digit number for you.
Let's play a bulls and cows game.
{separator}""")

def print_outro(guess_num: int):
    if guess_num == 1:
        print(f"""{separator}
Correct, you've guessed the right number in {guess_num} guess!
{separator}
That's amazing!""")
    else:
        print(f"""{separator}
Correct, you've guessed the right number in {guess_num} guesses!
{separator}
That's amazing!""")

def run_game() -> int:
    """
    Celá hra běží jako smyčka, která skončí uhodnutím správného čísla.
    Výstupem je číslo pokusu, při kterém bylo uhádnuto správné číslo.
    """
    text = "Enter a number: "
    guess_num = 0
    comp_num = generate_number()
    bulls = 0
    while bulls < req_num_length:
        bulls = 0
        cows = 0
        player_input = input(text).strip()

        ok, msg = validate_input(player_input)
        if not ok:
            text = msg
            continue

        bulls, cows = evaluate_guess(comp_num, player_input)

        if bulls < req_num_length:
            text = result_message(bulls, cows)
            guess_num += 1
            continue
        else:
            guess_num += 1
            break

    return guess_num

if __name__ == "__main__":
    print_intro()
    total_guesses = run_game()
    print_outro(total_guesses)
