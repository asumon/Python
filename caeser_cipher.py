# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 04:05:33 2020

@author: asumon
"""

##CAESER CIPHER   Encoding and Decoding process

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



'''
direction=input("Type 'Encode' to Encrypt, type 'decode' to decrypt:\n")

text=input("Please type your Message:\n").lower()

shift=int(input("Type the shift number:\n"))


#def encrypt():
    
    
    
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        new_letter=alphabet[new_position]
        cipher_text += new_letter
    print(f"The Encoded Text is : {cipher_text}")
    
    
#encrypt(text,shift)


def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        plain_text += alphabet[new_position]
    print(f"Decoded text : {plain_text}")
    
if direction=='encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction=='decode':
    decrypt(cipher_text=text, shift_amount=shift)
    
'''
 
    
## IN DIFFERENT WAY TO DO THIS CODE 

#import art Add the ASCII LOGO


    
def caeser_cipher(start_text,shift_amount,cipher_direction):
    end_text =""
    #for letter in start_text:
        #position=alphabet.index(letter)
    if cipher_direction=='decode':
       shift_amount *= -1
    for char in start_text:
        if char in alphabet:
           position=alphabet.index(char)
           new_position= position +shift_amount
           end_text += alphabet[new_position]
        else:
           end_text += char
                
    print(f"Here is the Cipher Text based on {cipher_direction}d and the Text is: {end_text}")



should_continue=True
while should_continue:
    direction=input("Type 'Encode' to Encrypt, type 'decode' to decrypt:\n")
    text=input("Please type your Message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    shift=shift % 25
    caeser_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)     
    result=input("Do you want to continue Yes or No :")
    if result=='no':
        should_continue=False
        print("GOOD BYE")

    


       
            
    
    