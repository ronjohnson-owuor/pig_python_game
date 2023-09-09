import random

number_of_players = input("Enter the number of players (2-4): ")


def roll():
    random_number = random.randint(1, 6)
    return random_number


while True:
    if number_of_players.isdigit():
        number_of_players = int(number_of_players)
        if 2 <= number_of_players <= 4:
            break
        else:
            print("enter between 2-4")
            number_of_players = input("Enter the number of players (2-4): ")

    else:
        print("Not a valid number please!")
        number_of_players = input("Enter the number of players (2-4): ")

players_score = [0 for _ in range(number_of_players)]
max_score = 50

while max(players_score) < max_score:
    for player_index in range(number_of_players):
        print('player: ', player_index + 1, 'has just started!')
        current_score = players_score[player_index]
        while True:
            value = roll()
            if value != 1:
                current_score += value
                print("current score: ", current_score)
                like_to_roll = input("Would you like to roll again: (y/n): ").lower()
                if like_to_roll != 'y':
                    break
            else:
                current_score = 0
                print("you rolled a !", value)

        players_score[player_index] = current_score
        print(f"Your total score {players_score[player_index]}")

    if max(players_score) > max_score:
        top_score = max(players_score)
        winning_index = players_score.index(top_score)
        print("We found a winner!🎉")
        print(f'The winner is player number, {winning_index + 1} with {top_score} points ')
        print(f'BONUS: {top_score-max_score}')
        break
