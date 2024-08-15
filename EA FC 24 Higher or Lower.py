import pandas as pd
import random
#Table with all data of EA FC 24 players but I have limited it only to Name and Overall rating
df = pd.read_csv(r"C:\Users\kezze\Downloads\archive (1)\male_players.csv",usecols=["Name", "Overall"])

#Set the rating of player based on condition e.g. greater than 82
new_df = df[df["Overall"]>=70]

#Pandas no limit for rows no ...
pd.set_option('display.max_rows', None)

#Storing data as variables then using .tolist() to place names and rating to list
names = new_df["Name"].tolist()
ratings = new_df["Overall"].tolist()

#Points set at 0
points = 0

#This will iterate through name and ratings and combine together e.g player 1 , rating 1.The reason commented is to hide the answer from output

#for both in zip(names, ratings):
    #print(both)

#This is the while loop to have multiple rounds and picks the player's name and rating from list
while True:
    indices = random.sample(range(len(names)), 2)
    player1_name = names[indices[0]]
    player1_rating = ratings[indices[0]]
    player2_name = names[indices[1]]
    player2_rating = ratings[indices[1]]
#User enter player they think is higher with first player being mapped to the letter A and second player mapped to the letter B
    print(f"Who has a higher rating")
    print(f"A:{player1_name}")
    print(f"B:{player2_name}")

#Once input has been entered I had added an .strip() and .upper() to remove any white space and Capitalisation sensitivity errors.Based on the answer the user has put
    #they would be allocated either 3 points for a win,1 for a draw and 0 for loss in which the game would as if the user would want to continue playing
    Player_Decision = input(f"Type A or B?").strip().upper()
    if (
            Player_Decision == "A" and player1_rating > player2_rating or Player_Decision == "B" and player2_rating > player1_rating):
        print("You were correct")
        points += 3
    elif (player2_rating == player1_rating):
        print("You drew")
        points += 1
    else:
        print("You were incorect")
        print(f"Game over your score is {points} ")
        player_input = input("Do you want to continue (yes/no)?").lower()
        if player_input == "no":
            print(f"Thanks for playing you got {points} points")
            break
