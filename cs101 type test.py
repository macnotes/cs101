#!/usr/local/bin/python3

""" 
Change the discuss_age function so that it no longer says, "I'm a
year older", but rather, makes one reply to the user after asking the
user's age. Use comparison operators to create a different statement for
three different categories of user age.
"""

prompt = "How old are you? "
user_age = int(input(prompt))
if user_age >= 0 and user_age <= 20:
    print ("You're a kid")
elif user_age > 20 and user_age <= 40:
    print ("You're a big kid")
elif user_age > 40:
    print ("You're not a kid anymore")




#prompt = "How many hours a day do you waste playing video games? "
#user_hours_wasted = input(prompt)
#bot_hours_wasted = int(user_hours_wasted) + 1
#bot_response = "Hey, that's nothing-- I waste " + str(bot_hours_wasted) + " hours a day!"
#print(bot_response)
