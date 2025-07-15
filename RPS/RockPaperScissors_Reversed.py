import time, random, os, sys
# Add the parent directory (Python-Games/) to sys.path
print(__file__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# import assets
from assets.input_suppressor import suppress_input
from assets.typewriter_print import tprint
from assets.clear_screen import clear_screen
from assets.countdown import countdown
from assets.scoreboard import scoreboard 
from assets.text_formatting import red, green, yellow, bold
# =========== EXECUTION BEGINS ============
# clear buffer before execution
clear_screen()
# define code params
user_score = computer_score = rounds = user_wins = computer_wins = ties = 0
choice_list = ["rock 🪨 ", "paper 📄", "scissors ✂️ "]
# define and print first header texts
header1 = f"""
Welcome to our interactive game of Rock, Paper, Scissors!\n
Rules of the game-
User has to choose among Rock/Paper/Scissors and compete with the computer
   Reversed Logic Mode (because chaos is fun) -
   {choice_list[2]} beats {choice_list[0]} [Scissors absolutely destroy Rock because why not]
   {choice_list[0]} beats {choice_list[1]} [Rock drills a hole into Paper's soul]
   {choice_list[1]} beat {choice_list[2]}  [Paper wraps Scissors like a burrito of defeat]
Good Luck! Hope you enjoy our game!!
"""
header2 = """
Enter Your choice:
1. 🪨  rock
2. 📄 paper
3. ✂️  scissors
Q. Stop Playing"""
with suppress_input():
    tprint(header1)
    countdown("The game starts in",3)
    time.sleep(1)
    tprint(scoreboard(rounds,user_score,computer_score))
    time.sleep(0.5)
    tprint(header2)
# ===== PRIMARY LOOP =====
while True:
    # print static headers including current scoreboard
    clear_screen()
    with suppress_input():
        print(header1, end="")
        print(scoreboard(rounds,user_score,computer_score), end="")
        print(header2)
    user_input = input(">>>")
    # validate input
    while user_input not in ("1","2","3","q","Q"):
        print("Invalid choice!")
        user_input = input(">>>")
    # check quit status
    if user_input in ("q","Q"):
        print()
        countdown("Quitting",3)
        break  
    with suppress_input():
        # define current iteration choices
        computer_choice = choice_list[random.randint(0,2)]
        user_choice = choice_list[int(user_input)-1]
        time.sleep(1)
        tprint(f"\nYou chose {user_choice}")
        time.sleep(0.5)
        tprint(f"Computer chose {computer_choice}")
        time.sleep(0.5)
        # check result and update score
        if user_choice == computer_choice:
            round_result = yellow("It's a tie!")
            user_score+=1
            computer_score+=1
            ties += 1
        elif (user_choice==choice_list[2] and computer_choice==choice_list[0]) or (user_choice==choice_list[1] and computer_choice==choice_list[2]) or (user_choice==choice_list[0] and computer_choice==choice_list[1]):
            round_result = green("You win!")
            user_score+=1
            user_wins +=1
        else:
            round_result = red("You Lose!")       
            computer_score+=1
            computer_wins+=1
        # print result
        print(f"{round_result}\n")
        time.sleep(1)
        rounds+=1
        countdown("Next round in",3)
        clear_screen()
# ====== GAME END ======
with suppress_input():
    clear_screen()
    time.sleep(0.5)
    tprint("----- GAME END -----\n")
    time.sleep(0.5)
    # print game statistics if played 
    if rounds>0:
        tprint(f"""\n{bold("Game statistics-")}
Rounds played: {rounds}
User won {user_wins} rounds
Computer won {computer_wins} rounds
{ties} rounds were tied
Your Score: {user_score}
Computer's Score: {computer_score}\n   
""")
        # check and print Series result
        if user_score == computer_score:
            game_result = yellow("The Series is a Draw!")
        elif user_score>computer_score:
            game_result = green("Congratulations!! You Win the Series!")
        else:
            game_result = red("Alas!! You Lose the Series!")
        time.sleep(0.5)
        tprint(game_result)
    # roast user if not played 
    else:
        tprint("""
    You ghosted the computer harder than its ex.
    Next time, press a key. ANY key.
    """)
    print("\n"*5)