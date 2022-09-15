import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    league_table = {}

    for row in file_contents:
        home, away, home_goals, away_goals, winner = row[1], row[2], row[3], row[4], row[5]

        if home not in league_table:
            league_table[home] = [0, 0]
        if away not in league_table:
            league_table[away] = [0, 0]

        if winner == 'D':
            league_table[home][0] += 1
            league_table[away][0] += 1

        if winner == 'A':
            league_table[home][0] += 0
            league_table[away][0] += 3

        if winner == 'H':
            league_table[home][0] += 3
            league_table[away][0] += 0

        league_table[home][1] = int(league_table[home][1]) + int(home_goals) - int(away_goals)
        league_table[away][1] = int(league_table[away][1]) + int(away_goals) - int(home_goals)

    print(f"{'Team':<20} {'Points':<15} {'Goal Difference':<10}")
    for key, value in sorted(league_table.items(), key=lambda e: e[1], reverse=True):
        points, goal_difference = value
        print(f'{key:<20} {points:<15} {goal_difference:<10}')

