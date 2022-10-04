import csv
from pathlib import Path

csv_file = Path("south.csv")
html_file = Path("south.html")


def read_csv(csv_file):
 csv_contents = []
 with open(csv_file) as csvfile:
   reader = csv.reader(csvfile, delimiter=",")
   next(reader)
   for row in reader:
     csv_contents.append(row)
 return csv_contents

def read_html(html_file):
 htmlfile = open(html_file, "r")
 html_contents = (htmlfile.read())
 return html_contents



if __name__ == "__main__":
    csv = read_csv(csv_file)
    html = read_html(html_file)
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


i = 0
open_tr = html.find('.el:nth-child(1)', i)
close_tr = html.find("</script>", open_tr)
html_string = html[open_tr:close_tr]

position = 'url('
pos_start = html_string.find(position)
pos_end = html_string.find(')', pos_start)
link_position = html_string[pos_start + len(position):pos_end]
a = html.replace(link_position, link_list[0])


print(a)
