import time, random, os
def typewriter_print(sample):
    for line in sample.splitlines():
        for i in range(len(line)):
            print(line[:i+1], end="\r", flush=True)
            time.sleep(0.01)
        print(line)
        time.sleep(0.5)  
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def scoreboard():
    return f"""
Round: {rounds+1}
\033[1mScoreBoard-\033[0m
You: {user_score}
Computer: {computer_score}
"""
def countdown3s(text):
    for i in range(3,0,-1):
        for j in range(4):
            print(f"{text} {i}{"."*j}    ", end="\r", flush=True)
            time.sleep(1/4)
clear_screen()
user_score = computer_score = rounds = 0
choice_list = ["rock 🪨 ", "paper 📄", "scissors ✂️ "]
header1 = f"""
Welcome to our interactive game of Rock, Paper, Scissors!\n
Rules of the game-
User has to choose among Rock/Paper/Scissors and compete with the computer
   winning criteria-
   {choice_list[0]} beats {choice_list[2]}
   {choice_list[1]} beats {choice_list[0]}
   {choice_list[2]} beat {choice_list[1]}
Good Luck! Hope you enjoy our game!!
"""
header2 = """
Enter Your choice:
1. 🪨  rock
2. 📄 paper
3. ✂️  scissors
Q. Stop Playing"""
typewriter_print(header1)
countdown3s("The game starts in")
print(" "*50,end="\r",flush=True)
time.sleep(1)
typewriter_print(scoreboard())
time.sleep(0.5)
typewriter_print(header2)
while True:
    clear_screen()
    print(header1, end="")
    print(scoreboard(), end="")
    print(header2)
    user_input = input(">>>")
    while user_input not in "123qQ":
        print("Invalid choice!")
        user_input = input(">>>")
    if user_input in "qQ":
        print()
        countdown3s("Quiting")
        break  
    computer_choice = choice_list[random.randint(0,2)]
    user_choice = choice_list[int(user_input)-1]
    time.sleep(1)
    typewriter_print(f"\nYou chose {user_choice}")
    time.sleep(0.5)
    typewriter_print(f"Computer chose {computer_choice}")
    time.sleep(0.5)
    if user_choice == computer_choice:
        round_result = "\033[33mIt's a tie!\033[0m"
        user_score+=1
        computer_score+=1
    elif (user_choice==choice_list[0] and computer_choice==choice_list[2]) or (user_choice==choice_list[2] and computer_choice==choice_list[1]) or (user_choice==choice_list[1] and computer_choice==choice_list[0]):
        round_result = "\033[32mYou win!\033[0m"
        user_score+=1
    else:
        round_result = "\033[31mYou Lose!\033[0m"       
        computer_score+=1
    print(f"{round_result}\n")
    time.sleep(1)
    rounds+=1
    countdown3s("Next round in")
    clear_screen()
clear_screen()
time.sleep(0.5)
typewriter_print("----- GAME END -----\n")
time.sleep(0.5)
if rounds>0:
    typewriter_print(f"""\n\033[1mGame statistics-\033[0m
Rounds played: {rounds}
Your Score: {user_score}
Computer's Score: {computer_score}   
    """)
    if user_score == computer_score:
        game_result = "\033[33mThe Series is a Draw!\033[0m"
    elif user_score>computer_score:
        game_result = "\033[33mCongratulations!! You Win the Series!\033[0m"
    else:
        game_result = "\033[31mAlas!! You Lose the Series!\033[0m"
    time.sleep(0.5)
    typewriter_print(game_result)
else:
    typewriter_print("""
OH man you didn't even try!
Next time, pick something! The computer was READY.  
""")
print("\n"*5)