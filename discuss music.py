#!/usr/local/bin/python3

# fill up the list of possible throws
throw_list = ["rock", "paper", "scissors"]
# initialize the Boolean to show that we don't yet have a valid response from the user
# waiting_for_valid_response = True
# allow the loop to run while we are still waiting for a valid response
while waiting_for_valid_response:
    # let the user pick a throw
    user_throw = input("Please pick Rock, Paper or Scissors")
    # convert to lower case for purposes of analysis
    user_throw = user_throw.lower()
    # check to see if user gave a valid response
    if user_throw in throw_list:
        print("Good choice!")
        # re-assign the value of the Boolean to show that we are no longer waiting for the response to be valid (exit point) 
        waiting_for_valid_response = False
    else:
        # throw was not valid so user needs to pick again
        print("That was not one of your choices.")
# continue with the program now that the response is valid
# all code below this point is not in the loop
bot_response = "Okay, you picked " + user_throw + "Now it's my turn!"
print(bot_response)
