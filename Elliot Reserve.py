
def rock_paper_scissors():

    import random

    throws_list = ["rock", "paper", "scissors"]

    def computer_throw():
        eliza_throw = random.choice(throws_list)

    def user_throw():
        print("Choose rock, paper, or scissors.")
        input()

    def determine_winning_throw(user_throw, computer_throw):
        if user_throw == "rock":
            if eliza_throw == "paper":
                user_throw = loser
            elif eliza_throw == ("scissors"):
                user_throw = winner
            elif eliza_throw == ("rock"):
                user_throw = tie

        if user_throw == "paper":
            if eliza_throw == "paper":
                user_throw = tie
            elif eliza_throw == ("scissors"):
                user_throw = loser
            elif eliza_throw == ("rock"):
                user_throw = winner

        if user_throw == "scissors":
            if eliza_throw == "paper":
                user_throw = winner
            elif eliza_throw == ("scissors"):
                user_throw = tie
            elif eliza_throw == ("rock"):
                user_throw = loser

        return winner


    throws_list = ["rock","paper","scissors"]
    user_throw = random.choice(throws_list)
    eliza_throw = random.choice(throws_list)
    print(f"You through a {user_throw}")
    print(f"Eliza through a {eliza_throw}")



    if user_throw == "rock":
        if eliza_throw == "paper":
            print("You Lose")
        elif eliza_throw == ("scissors"):
            print("You Win")
        elif eliza_throw == ("rock"):
            print("Tie")

    if user_throw == "paper":
        if eliza_throw == "paper":
            print("Tie")
        elif eliza_throw == ("scissors"):
            print("You Lose")
        elif eliza_throw == ("rock"):
            print("You Win")

    if user_throw == "scissors":
        if eliza_throw == "paper":
            print("You Win")
        elif eliza_throw == ("scissors"):
            print("Tie")
        elif eliza_throw == ("rock"):
            print("You Lose")