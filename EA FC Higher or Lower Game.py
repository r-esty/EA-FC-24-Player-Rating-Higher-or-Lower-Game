import pandas as pd
import random
#url of player database
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS8SBtWL7or0KnXp-MZbvMJ4fBwYQELutvwLfnaqq5ZR8vRyk3xgJQQRs1vWDz_biCB9S8xjWnzxdNW/pub?output=csv"

#Table with all data of EA FC 24 players but I have limited it only to Name and Overall rating
df = pd.read_csv(url,usecols=["Name", "Overall"])

#Set the rating of player based on condition e.g. greater than 82
new_df = df[df["Overall"]>=70]

#Pandas no limit for rows no ...
pd.set_option('display.max_rows', None)

names = new_df["Name"].tolist()
ratings = new_df["Overall"].tolist()

while True:
    points = 0

    while True:
        indices = random.sample(range(len(names)), 2)
        player1_name = names[indices[0]]
        player1_rating = ratings[indices[0]]
        player2_name = names[indices[1]]
        player2_rating = ratings[indices[1]]
        # User enter player they think is higher with first player being mapped to the letter A and second player mapped to the letter B
        print(f"Who has a higher rating")
        print(f"A:{player1_name}")
        print(f"B:{player2_name}")

        Player_Decision = input(f"Type A or B?").strip().upper()
        if(Player_Decision == "A" and player1_rating > player2_rating or Player_Decision == "B" and player2_rating > player1_rating):
            print("You were correct")
            points += 3
        elif (player2_rating == player1_rating):
            print("You drew")
            points += 1
        else:
            print("You were incorect")
            print(f"Game over your score is {points} ")
            break
    player_input = input("Do you want to continute (yes/no)?").lower()
    if player_input == "no":
        print(f"Thanks for playing you got {points} points")
        break




