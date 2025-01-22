#import the random package
import random


#dice roll function
def roll():
    min_value = 2
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
while True:
    players = input("Enter the numbers of people who will be playing (2-4): ")
    #is digit
    if players.isdigit():
        #ensure input converts to integer
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again")    

#score variables
max_score = 50
player_scores = [0 for _ in range(players)]


#loop trough the player turns

while max(player_scores) < max_score:
    for player_i in range(players):
        print(f"Player number {player_i + 1} has just started! \n")
        print(f"Your total score is: {player_scores[player_i]} \n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y) ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
                
        #sum up the players score after turn        
        player_scores[player_i] += current_score
        print(f"Your score is: {current_score}")
        
#present the winner            
max_score = max(player_scores)
winning_i = player_scores.index(max_score)
print(f"Player number {winning_i + 1} is the winner with the score of: {max_score}")  