from random import randint

turn = ["rock","paper","scissors"]
computer_options = turn[randint(0,2)]

player = False

while player == False:
    player = input(" rock , paper , scissors")
    if player == computer_options:
        print("its a tie")

    if  player == "rock" :
        if computer_options == "paper":
            print("you lose!")
        else:
            print("you win")


    if player == "paper":

        if computer_options =="scissors":
            print("you lose")
        else:
            print("you win")

    if player == "scissors":
        if computer_options =="rock":
            print("you lose")
        else:
            print("you won")




