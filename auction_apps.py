# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 01:07:10 2020

@author: asumon
"""

from replit import clear

auction_bid={}

bidding_finish=False

while not bidding_finish:

    name=input("Please Enter Your Name: ")
    price=float(input("What is your Bid $:"))
    auction_bid[name]=price
    should_continue=input("Are you want to continue ? Type Yes or No :")
    if should_continue =='no':
        bidding_finish=True
    elif should_continue =='yes':
        clear()
    

def highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid $ {highest_bid}")
    
    

highest_bidder(auction_bid)