p1 = input("Player 1, Enter rock/paper/scissors: ")
p2 = input("Player 2, Enter rock/paper/scissors: ")

def rock_paper_scissors(player_1, player_2):
    a_list = ["rock", "paper", "scissors"]

    while player_1 not in a_list or player_2 not in a_list:
        player_1 = input("Player 1, Enter rock/paper/scissors: ")
        player_2 = input("Player 2, Enter rock/paper/scissors: ")

    while player_1 == player_2:
        player_1 = input("Player 1, Enter rock/paper/scissors: ")
        player_2 = input("Player 2, Enter rock/paper/scissors: ")

    if player_1 == "rock" and player_2 == "paper":
        print ("Player 2 wins!")

    elif player_1 == "paper" and player_2 == "rock":
        print ("Player 1 wins!")

    elif player_1 == "rock" and player_2 == "scissors":
        print ("Player 1 wins!")

    elif player_1 == "scissors" and player_2 == "rock":
        print ("Player 2 wins")

    elif player_1 == "paper" and player_2 == "scissors":
        print ("Player 2 wins!")

    elif player_1 == "scissors" and player_2 == "paper":
        print ("Player 1 wins!")
print ("congragulations" , p1 or p2)
rock_paper_scissors(p1, p2)

print("play_again")
