#!/usr/bin/env python3  # this is the path to the python interpreter

# import modules
import random  #to determine what move the computer will throw
import time

#setting each move to a specific number
rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

#variables to keep track of the scores.
player_score = 0
computer_score = 0

def start():
    print("Let's play a game of Rock, Paper, Scissors.")
    while game(): #starting a while loop that allow us to keep playing the game as many times as we want
        pass   #pass statement allows while loop to stop once we have finished and could be used to perform other tasks if wished
    scores()  #if we do stop playing, the score function is then called upon

def game():
    player = move()
    computer = random.randint(1,3)  #uses random module's randint function to get an integer between 1 and 3
    result(player, computer)
    return play_again()

def move():
    while True:
        print
        player = input("Rock=1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:  #try statement is to clean up code and handle errrors or other exception
            player = int(player)  #change whatever the player entered into integer form
            if player in (1,2,3):  #check the input player whether it is 1,2,3 if yes, move returns this back up to the game function
                return player
        except ValueError:  #if got valueerror, we use except to do nothing. it prints error and then start while loop again until acceptable move is made.
                pass
        print ("Oops! I did not understand that! Please enter 1,2 or 3.")

def result(player, computer):
    #start with having countdown to the result. 
    #sleep pauses the execution code by number of seconds in the brackets
    print ("1...")
    time.sleep(1)
    print ("2...")
    time.sleep(1)
    print ("3!")
    time.sleep(0.5)
    print ("Computer threw {0}!".format(names[computer])) #this will print out what the computer threw in the text version of the move by calling names
    global player_score, computer_score  #using global function allows for variable to be changed and used outside of the variable, esp after we have appended a number to one of their scores
    #the way of checking the results is through elimination
    if player == computer:  #if move player and computer is the same, then its a tie
        print ("Tie game")
    else:      #if not a tie, check if win or loss
        if rules[player]==computer:  #if the losing move to the player's move is the same as computer's
            print ("Your victory has been assured")
            player_score +=1
        else:
            print ("The computer laughs as you realise you have been defeated")
            computer_score +=1

def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y","Y","yes","Yes","Of course!"):
        return answer
    else:
        print("Thank you for playing our game. See you next time!")

def scores():
    global player_score, computer_score
    print ("HIGH SCORES")
    print ("PLAYER:  ", player_score)
    print ("Computer: ", computer_score)

#this part allows for script to be use in two ways
#executed in the command line
#import into another python script
if __name__ == '__main__':
    start()