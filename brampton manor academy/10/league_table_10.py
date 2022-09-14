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

def process_results(rows):
    league_table = {}
    for row in rows:
        home, away, homegoals, awaygoals, winner = row[1], row[2], row[3], row[4], row[5]

        if home not in league_table:
         league_table[home] = [0,0]
        if away not in league_table:
         league_table[away] = [0,0]

        if winner == "D":
         league_table[home][0] += 1
         league_table[away][0] += 1
      
        if winner == "H":
         league_table[home] += 3
         league_table[away] += 0
       
        if winner == "A":
         league_table[home] += 0
         league_table[away] += 3
        
        #goal difference also needs to be calculated
         league_table['home'][1] = league_table[home][1] + homegoals - awaygoals
        #goal difference for away team here
         league_table['away'][1] = league_table[away][1] + awaygoals - homegoals
        #after this is done, you'll have all of the points and goal differences for each team
    return league_table


if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    results = process_results(file_contents)
    print(results)
    #instead of printing, you'll need to sort function to sort...the league - this should help - https://stackoverflow.com/questions/1217251/sorting-a league_table-with-lists-as-values-according-to-an-element-from-the-list
    #then print the league table in a pretty output function
