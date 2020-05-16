#!/usr/local/bin/python3

#get the user's name
#greet user

#repeat while user wants to play
#get the user's throw
#get the computer's throw
#see which throw wins the round
#announce results of the round
#update the score
#ask for replay


#announce final results
#say the game is over

import random

throws_list = ["rock","paper","scissors"]
user_throw = random.choice(throws_list)
eliza_throw = random.choice(throws_list)
print(f"You through a {user_throw}")
print(f"Eliza through a {eliza_throw}")
