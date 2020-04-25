#!/usr/local/bin/python3

import random 

"""
Another possibility is to use nesting, where you put one structure 
inside another structure. In this case it would be one if block inside
another if block. You can always put one structure inside another 
structure, as long as you indent them properly. It would look like this:

if user_throw == "rock":
    if eliza_throw == "scissors":
"""

### Dad writes...
throws_list = ["rock","paper","scissors"]
user_throw = random.choice(throws_list)
eliza_throw = random.choice(throws_list)
print(f"You through a {user_throw}")
print(f"Eliza through a {eliza_throw}")
### End of dad written section.


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
