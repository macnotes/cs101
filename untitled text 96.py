#!/usr/local/bin/python3

def discuss_music(user_name):
  #establish list of artists to discuss
  artist_list = ["Demi Lovato", "Ed Sheeran", "Ariana Grande ", "Kanye West", "Future" ]
  print("Let's talk about music.")

  #iterate through each artist in the list 
  #this is the start of the loop 
  for artist_name in artist_list: 
    #all of these indented steps will be done repeatedly
    #this is the body of the loop
    #use the target variable to create a statement
    print("Hey, " + user_name + ", " + artist_name + " is great!")

  #the loop has now finished
  #make a statement after going through the list
  print( "See you later.")


user_name=""
discuss_music(user_name)
