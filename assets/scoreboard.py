def scoreboard(rounds,user_score,computer_score):
    return f"""
Round: {rounds+1}
\033[1mScoreBoard-\033[0m
You: {user_score}
Computer: {computer_score}
"""