import csv
from pathlib import Path

csv_file = Path("south.csv")
html_file = Path("south.html")


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

def read_html(html_file):
        with open(html_file, "r") as html_file:
            html_contents = html_file.read()
            return html_contents

print(html_file.read)
#def process(csv, html):
    #html_contents = html_file.read()
   # html = html_contents
    #for row in csv:
       # link, initial, name = row[0], row[1], row[2]

        #i = html.find('<div class="el">')
       # print(i)




























    #if __name__ == "__main__":
    #csv = read_csv(path="south.csv")
    #html = read_html(path="south.html")
    #html = process(csv=csv, html=html)
    #write_html(path="south_final.html", html=html)