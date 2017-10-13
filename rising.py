import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.fplstatistics.co.uk/Home/IndexWG'
header = {'User-Agent': 'Mozilla/5.0'}

r = urllib.request.Request(url=url, headers=header)
page = urllib.request.urlopen(r)
soup = BeautifulSoup(page.read(), "html.parser")
string = 'tbody tr:nth-of-type(1) td:nth-of-type(1), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(6), tbody tr:nth-of-type(2) td:nth-of-type(1), tbody tr:nth-of-type(2) td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(6), tbody tr:nth-of-type(3) td:nth-of-type(1), tbody tr:nth-of-type(3) td:nth-of-type(2), tbody tr:nth-of-type(3) td:nth-of-type(6), tbody tr:nth-of-type(4) td:nth-of-type(1), tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(6)'

data = soup.select(string)

player1Name = data[0].contents[0].strip()
player1Team = data[1].contents[0].strip()
player1Price = data[2].contents[0].strip()

player2Name = data[3].contents[0].strip()
player2Team = data[4].contents[0].strip()
player2Price = data[5].contents[0].strip()

player3Name = data[6].contents[0].strip()
player3Team = data[7].contents[0].strip()
player3Price = data[8].contents[0].strip()

fpl_strings1 = ["<b>"+player1Name+"</b>", player1Team, "<i>"+player1Price+"</i>"]
fpl_strings2 = ["<b>"+player2Name+"</b>", player2Team, "<i>"+player2Price+"</i>"]
fpl_strings3 = ["<b>"+player3Name+"</b>", player3Team, "<i>"+player3Price+"</i>"]

print(" ".join(fpl_strings1))
print(" ".join(fpl_strings2))
print(" ".join(fpl_strings3))