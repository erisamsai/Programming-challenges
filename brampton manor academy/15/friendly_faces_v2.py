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
        html = html_file.read()
        return html


def process(csv, html):

    link_list = []
    initial_list = []
    name_list = []

    for row in csv:
        link, initial, name = row[0], row[1], row[2]

        if link not in link_list:
            link_list.append(link)

        if initial not in initial_list:
            initial_list.append(initial)

        if name not in name_list:
            name_list.append(name)
            
        for i in range(5):
            html.replace(f"link{i + 1}", link_list[i])
            html.replace(f"initials{i + 1}", initial_list[i])
            html.replace(f"name{i + 1}", name_list[i])
            return html


def write_html(path, html):
    path = Path("south_final.html")
    with open(path, "w") as final_file:
        final_file.write(html)
        return final_file


if __name__ == "__main__":
    csv = read_csv(csv_file)
    html = read_html(html_file)
    html = process(csv=csv, html=html)
    write_html(path="south_final.html", html=html)


