#!/usr/local/bin/python3

def playRPS():
  # fill up the list of possible throws
  throw_list = ["rock", "paper", "scissors"]
  # initialize the Boolean to show that we don't yet have a valid response from the user
  waiting_for_valid_response = True
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


playRPS


def ask_yes_no_question():
  #establish list of positive responses
  yes_list = ["yeah","yes","ok"]

  #establish list of negative responses
  no_list = ["no","not","nah"]

  #assign a default value to the bot's response
  response = "ME TOO!"

  #get user input
  answer = input ("Do you like pie? ")
  
  #   print (f"answer {answer}")
  
  #break user input up into a list of words
  words = answer.split(" ")

  # if any(word in all_text for word in keyword_list):

  #iterate through each word in the user word list
  for word in words:
    #see if that word is in the positive list
    if word in yes_list:
      #assign bot response an appropriate value for positive user input
      response = "Yes, I also like pie."
    #see if that word is in the negative list
    if word in no_list:
      #assign bot response an appropriate value for negative user input
      response = "I also do not like pie."

  #display the bot's response
  print (response)

# ask_yes_no_question()



# words = "My name is Bob.".split()
# for word in words:
#   print (word)


# Example from https://www.w3schools.com/python/python_dictionaries.asp
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# import time
# sleep_time = .5
# credits_dict = {
#   "Testing": "Sue",
#   "Help": "Sam",
#   "Snacks": "Bob"
# }
# for role in credits_dict:   # for key in dict
#   name = credits_dict[role] # value for key (role)
#   time.sleep(sleep_time)
#   print("")
#   print(role+": "+name)
#   print("")


# import time
# sleep_time = .5
# credit_list = ["Beta Tester-El","Help-Dad","Snacks-Mom"]
# for credit in credit_list:
#   time.sleep(sleep_time)
#   print("")
#   print(credit)
#   print("")

