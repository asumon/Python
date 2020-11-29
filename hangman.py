# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:01:08 2020

@author: asumon
"""

import random

#Step 1

#Some Constant Words
word_list= ["sumon","hello","hi","baboon","love","like"]
chosen_word = random.choice(word_list)

word_length=len(chosen_word)


#Testing Code
print(f"Passt, The solution is {chosen_word}.")


# Create Blanks
display=[]
for _ in range(word_length):
    display += "_"
#print(display)



end_of_game=False

while not end_of_game:
    guess=input("Please guess the word: ").lower()    
#Check guessed letter
    for position in range(word_length):
        letter=chosen_word[position]
        print(f"Current position : {position}\n Current Letter : {letter}\n Guessed letter: {guess}")
        if letter == guess:
           display[position] = letter
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("\n")
        print("############\n")
        print("YOU WIN !!!\n") 
        print("############")
        
        
        
    
    