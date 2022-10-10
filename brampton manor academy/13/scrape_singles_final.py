import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def find_tr(html, i):
    open_tr = html.find('<tr>', i)
    close_tr = html.find("</tr>", open_tr)
    row = html[open_tr:close_tr]
    return row, close_tr

def find_position(row):
    position = '"position">'
    pos_start = row.find(position)
    pos_end = row.find('</', pos_start)
    actual_position = row[pos_start + len(position):pos_end]
    return actual_position

def find_title(row):
    title = 'alt="'
    title_start = row.find(title)
    title_end = row.find('" width', title_start)
    actual_title = row[title_start + len(title):title_end]
    return actual_title

def find_artist(row):
    artist = '<div class="artist">'
    url = '         <a href="/artist/'
    start_url = row.find(url)
    artist_start = row.find(artist)
    artist_end = row.find('</a', artist_start)
    end_url = row.find('/">', start_url)
    remove_url = end_url - start_url
    actual_artist = row[artist_start + len(artist) + len(url) + remove_url:artist_end]
    return actual_artist

if __name__ == "__main__":
    html = scrape(url)
    print(f"{'Position':<10} {'Title':<35} {'Artist':<25}")
    i = 0
    for x in range(10):
        row, i = find_tr(html, i)
        position = find_position(row)
        title = find_title(row)
        artist = find_artist(row)
        print(f"{position:<10} {title:<35} {artist:<25}")
