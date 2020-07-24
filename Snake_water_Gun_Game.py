import random

player =["Snake", "Water", "Gun"]
Computer = ["Snake", "Water", "Gun"]
player_score =0
computer_score =0

def welcome():
    print("***********************************")
    print("Welcome to Snake Water Gun Game")
    print("***********************************")

def player_input():
    global player
    Player_input = input("\nPlease enter 'S' for 'Snake' 'W' for 'Water' and 'G' for 'Gun': ")
    if Player_input.capitalize() =='S':
        return player[0]
    elif Player_input.capitalize()=='W':
        return player[1]
    elif Player_input.capitalize()=='G':
        return player[2]


def computer_input():
    global Computer
    choice = random.choice(Computer)
    return choice
# Computer_choice = computer_choice

def start_play():
    global player_score, computer_score

    n = 1
    while n<11:
        player_choice = player_input()
        computer_choice = computer_input()

        if player_choice =='Snake' and (computer_choice!='Gun' and computer_choice!='Snake'):
            print(f'Player Choice is: {player_choice}')
            print(f'Computer Choice is: {computer_choice}')
            print("Player Wins")
            player_score+=1
        elif player_choice =='Water' and (computer_choice!='Snake' and computer_choice !='Water'):
            print(f'Player Choice is: {player_choice}')
            print(f'Computer Choice is: {computer_choice}')
            print("Player Wins")
            player_score+=1
        elif player_choice =='Gun' and (computer_choice!='Water' and computer_choice !='Gun'):
            print(f'Player Choice is: {player_choice}')
            print(f'Computer Choice is: {computer_choice}')
            print("Player Wins")
            player_score+=1
        elif player_choice == computer_choice:
            print(f'Player Choice is: {player_choice}')
            print(f'Computer Choice is: {computer_choice}')
            print("Its a Tie")
        else:
            print(f'Player Choice is: {player_choice}')
            print(f'Computer Choice is: {computer_choice}')
            print('Computer Wins')
            computer_score+=1
        n+=1


def total_score():
    print('\n'f'Player Total Score is:{player_score}')
    print('\n'f'Computer Total Score is:{computer_score}')
    if player_score>computer_score:
        print("\nYou are a Winner!\n")
    elif player_score == computer_score:
        print("\nIts a Tie Game. Nobody Won!\n")
    else:
        print("\nComputer Won!\n")
    print("**************************************")
    print("\t\t  Game Over ")
    print("**************************************")


welcome()
start_play()
total_score()