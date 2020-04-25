#!/usr/local/bin/python3


def get_therapist_response(user_input):
    
    # Rule #1. Finding negative inputs and then responding to them
    negative_list=["sad","disappointed","gloomy","distraught"]
    for word in negative_list:
        if word in user_input:
            print("You're being very negative.")
            return
    
    # Rule #2. Finding you in user input and making a response
    if "you" in user_input:
        bot_response = "Let's talk about you."
    # assigning a value to the variable prompt

    # Rule #3. if they tell us a feeling then we can respond to that
    # elif makes it so the I am and the stuff above are mutually exclusive. 
    elif user_input.find("I am"):
        user_feeling = user_input[4:]
        # importing random into the program
        import random
        # assigning a value to index
        index = random.randint(0, 2)
        # assigning value to response list
        responses_list = ["Do you believe it is normal to be" + user_feeling + "? ",
                          "Why do you feel" + user_feeling + "? ",
                          "Do you know anybody who also feels" + user_feeling + "? "]
        # assigning value to bot response
        bot_response = responses_list[index]
        # having the bot print the bot response
        user_input = input(bot_response)

        index = random.randint(0, 2)
        responses_list = ["Do you say " + user_input + " for any particular reason? ",
                          "Do you know anyone else who would agree with you? ",
                          "So you say " + user_input + " but are you really sure? "]
        # assigning a new value to the variable bot_response
        bot_response = responses_list[index]

    # having the bot print bot response
    print(bot_response)

    # finder = user_input.find("I'm")
    # if (user_input.find("I'm")):
    #     print(bot_response)
    # finder = user_input.find("I am")
    # if (user_input.find("I am")):
    #     print(bot_response)
    #     # assigning a new value to the variable user input
    #     user_input = input(bot_response)


def discuss_weather():
    # assign a value to the prompt variable with literal text
    prompt = "What is the weather like today? "
    # assign a value to the user input variable by calling the function to ask the user a question
    user_input = input(prompt)
    # assign a value to the bot_response variable with literal text
    bot_response = "Do you like that kind of weather? "
    # call the function for displaying text in the console
    if "sun" in user_input or "bright" in user_input:
        bot_response = "Does it make you happy to see the sun? "
    # call the function for displaying text in the console
    if "snowy" in user_input or "blizzard" in user_input:
        bot_response = "Do you like snow, I sure don't."
    # call the function for displaying text in the console
    if "rain" in user_input or "pouring" in user_input:
        bot_response = "So what do you think about rain? "
    # call the function for displaying text in the console
    if "cloudy" in user_input or "overcast" in user_input:
        bot_response = "I hope it doesn't rain."
    # call the function for displaying text in the console
    if "cold" in user_input or "chilly" in user_input:
        bot_response = "I hope you have your coat!"

    print(bot_response)


# defining the function discuss_school_subjects
def discuss_school_subjects():
    inquiry = "What's your favorite subject in school? "
    user_favorite_subject = input(inquiry).lower()
    # assigning a default value to the bot_reply variable
    bot_reply = "I've never heard of that class before."
    # lists of possible responses
    math_response_list = ["math", "mathematics", "algebra", "geometry", "calculus", "precalculus"]
    science_response_list = ["science", "biology", "chemistry", "ecology", "environmental science"]
    english_response_list = ["english", "writing", "reading", "literature"]
    social_studies_response_list = ["social studies", "history", "world history", "global history", "economics"]
    computer_response_list = ["computer science", "computer programming", "programming", "technology"]
    import random
    index = random.randint(0, 1)
    math = ["Cool! Show me what maths you are doing sometime!", "What type of math is your favorite? "]
    science = ["I know a lot about science", "Have you done some science today? "]
    english = ["What is your favorite book then? ", "Fun, I like english to."]
    social_studies = ["Oh, social studies is great!", "What social studies class are you in? "]
    computer = ["You must be having fun then!", "So I've been having a bit of a problem..."]
    none = ["That sucks!", "I hope you can find a class that you like."]
    # decision structure for the question
    if user_favorite_subject in math_response_list:
        bot_reply = math[index]
    if user_favorite_subject in science_response_list:
        bot_reply = science[index]
    if user_favorite_subject in english_response_list:
        bot_reply = english[index]
    if user_favorite_subject in social_studies_response_list:
        bot_reply = social_studies[index]
    if user_favorite_subject in computer_response_list:
        bot_reply = computer[index]
    if user_favorite_subject == "nothing" or user_favorite_subject == "none":
        bot_reply = none[index]
    print(bot_reply)


def discuss_music(user_name):
    # establish list of artists to discuss
    artist_list = ["Demi Lovato", "Ed Sheeran", "Ariana Grande ", "Kanye West", "Future"]
    print("Let's talk about music.")

    # iterate through each artist in the list
    # this is the start of the loop
    for artist in artist_list:
        # all of these indented steps will be done repeatedly
        # this is the body of the loop

        # use the target variable to create a statement
        print("Hey, " + user_name + ", " + artist + " is great!")
    # the loop has now finished
    # make a statement after going through the list
    print("See you later.")


def ask_intro_questions():
    print("Welcome. I'd like to get to know you a little better. ")
    # first_name = input# ("What is your first name? ")
    print("What is your first name? ")
    first_name = input("> ")

    discuss_weather()
    discuss_school_subjects()
    # discuss_music(first_name)
    return first_name


def main():

    first_name = ask_intro_questions()
    print("Thanks for helping me get to know you a little better, " + first_name + "!")
    print("")
    print("I'd like to see how you're doing. Please enter \"done\" when you want to leave.")
    print("")

    # initialize the Boolean to show that the chat is now on
    user_talking = True
    # Keep on talking to user as long as they are answering us/
    stop_words=["stop","quit","done","exit","bye"]

    while user_talking:   
      #code to repeat will go in here; it's not ready yet
      print("Is there something you'd like to tell me? ")
      # assigning a value to user input
      user_input = input("> ").lower()

      if user_input not in stop_words:
        get_therapist_response(user_input)
      else:
        # User wants to leave. 
        # Set user_talking boolean to false to stop loop 
        user_talking = False
        print("Goodbye.")


if __name__ == '__main__':
    main()
