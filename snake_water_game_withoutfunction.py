
#Snake Water Gun Game
import random
print(".......................................".strip())
print("Welcome to Snake Water Gun Game".strip())
print(".......................................\n".strip())

player =["Snake", "Water", "Gun"]
Computer = ["Snake", "Water", "Gun"]
player_score =0
computer_score =0

n =1

while n<11:
    player_input = input("\nPlease enter 'S' for 'Snake' 'W' for 'Water' and 'G' for 'Gun': ")
    computer_choice = random.choice(Computer)

    if player_input.capitalize()=='S':
        player_choice=player[0]
        print(f'Player choice is: {player_choice}')
        print(f'Computer choice is: {computer_choice}')

        if player_choice== computer_choice:
            print("Its a Tie")

        elif player_choice == 'Snake' and (computer_choice!='Gun' and computer_choice!='Snake'):
         print("Player Wins")
         player_score+=1

        else:
            print("Computer wins")
            computer_score+=1

    elif player_input.capitalize()=='W':
        player_choice=player[1]
        print(f'Player choice is: {player_choice}')
        print(f'Computer choice is: {computer_choice}')

        if player_choice== computer_choice:
            print('Its a Tie')
        elif player_choice=='Water' and (computer_choice!='Snake' and computer_choice!='Water'):
            print("Player wins")
            player_score+=1
        else:
            print("Computer Wins")
            computer_score+=1
    elif player_input.capitalize()=='G':
        player_choice=player[2]
        print(f'Player choice is: {player_choice}')
        print(f'Computer choice is: {computer_choice}')
        if player_choice== computer_choice:
            print("Its a Tie")
        elif player_choice=='Gun' and (computer_choice!='Water' and computer_choice!='Gun'):
            print("Player wins")
            player_score+=1
        else:
            print("Computer Wins")
            computer_score+=1
    n=n+1


print('\n'f'Player Total score is {player_score}')
print(f'Computer total score is {computer_score}\n')

if player_score>computer_score:
    print("You are Winner!")
elif player_score==computer_score:
    print("Its a Tie Game")
else:
    print("Computer Won The Game!")

print("...............................................")
print("\t\t ***** Game Over *****")
print("...............................................")

























