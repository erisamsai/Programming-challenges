import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


if __name__ == "__main__":
    html = scrape(url)

i = 0
while 69990 > i > -1:
    open_tr = html.find('<tr>', i)
    close_tr = html.find("</tr>", open_tr)
    newstring = html[open_tr:close_tr]

    position = '"position">'
    pos_start = newstring.find(position)
    pos_end = newstring.find('</', pos_start)
    actual_position = newstring[pos_start+len(position):pos_end]
    print(actual_position)


    title = 'alt="'
    title_start = newstring.find(title)
    title_end = newstring.find('" width', title_start)
    actual_title = newstring[title_start+len(title):title_end]
    print(actual_title)

    artist = '<div class="artist">'
    url = '         <a href="/artist/'
    start_url = newstring.find(url)
    artist_start = newstring.find(artist)
    artist_end = newstring.find('</a', artist_start)
    end_url = newstring.find('/">', start_url)
    remove_url = end_url - start_url
    actual_artist = newstring[artist_start + len(artist) + len(url) + remove_url:artist_end]
    print(actual_artist)
