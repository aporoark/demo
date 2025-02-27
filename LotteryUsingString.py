#Description: Reworking the lottery program

#Import the random module
import random

#Generate a lottery number
lottery = str(random.randint(0,9)) + str(random.randint(0,9))

#prompt the user to input a guess
guess = input("Enter your lottery pick(two-digits): ")

#Display the winning numbers
print("The Winning loterry number is :", lottery)

#Check the guess for a winning case
if guess == lottery:
    print("exact match: You win $10,000")
elif guess[1] == lottery[0] and guess[0] == lottery[1]:
     print("Match all digits: You win $5,000")
elif guess[0] == lottery[0] or guess[0] == lottery[1]\
     or guess [1] == lottery[0] or guess[1] == lottery[1]:
    print("Match one Digit: You win $1,000")
else:
    print("Better luck next time!")
         
