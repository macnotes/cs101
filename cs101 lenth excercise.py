#!/usr/local/bin/python3

""" 
Create a new function named count_words. 
Write the def line of the function so that it will take one argument, a sentence. 
Inside the function, write the code that will split the sentence up into words
 and then tell the user how many words are in the sentence.

When you run it, you should get a result like: 
Your sentence has this number of words:
6 
"""

def count_words(my_sentence):
    # print("Sentence: "+ my_sentence)
    words = my_sentence.split()
    number_of_words = len(words)
    print("Your sentence has this number of words:")
    print (str(number_of_words))

def main():
      my_sentence = "Hey, this is not a sentence."
      my_sentence = "Okay then, this is not a sentence either."
      count_words(my_sentence)

main()

