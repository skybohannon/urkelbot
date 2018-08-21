import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.fplstatistics.co.uk/Home/IndexWG?gridPriceData_sort=NTIPERCENTNJD&gridPriceData_sortdir=DESC'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

string = 'tbody tr:nth-of-type(1) td:nth-of-type(1), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(6), tbody tr:nth-of-type(2) td:nth-of-type(1), tbody tr:nth-of-type(2) td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(6), tbody tr:nth-of-type(3) td:nth-of-type(1), tbody tr:nth-of-type(3) td:nth-of-type(2), tbody tr:nth-of-type(3) td:nth-of-type(6), tbody tr:nth-of-type(4) td:nth-of-type(1), tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(6)'

data = soup.select(string)
print(data)

player1Name = data[0].contents[0].strip()
player1Team = data[1].contents[0].strip()
player1Price = data[2].contents[0].strip()


string = 'tbody tr:nth-of-type(1) td:nth-of-type(1), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(6), \
tbody tr:nth-of-type(2) td:nth-of-type(1), tbody tr:nth-of-type(2) td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(6), \
tbody tr:nth-of-type(3) td:nth-of-type(1), tbody tr:nth-of-type(3) td:nth-of-type(2), tbody tr:nth-of-type(3) td:nth-of-type(6), \
tbody tr:nth-of-type(4) td:nth-of-type(1), tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(6)'

data = soup.select(string)
print(data)

player1Name = data[0].text.strip()
player1Team = data[1].text.strip()
player1Price = data[2].text.strip()
player2Name = data[3].text.strip()
player2Team = data[4].text.strip()
player2Price = data[5].text.strip()
player3Name = data[6].text.strip()
player3Team = data[7].text.strip()
player3Price = data[8].text.strip()
player4Name = data[9].text.strip()
player4Team = data[10].text.strip()
player4Price = data[11].text.strip()


lineup = {
    1: {"playerName": player1Name,
        "playerTeam": player1Team,
        "playerPrice": player1Price},
    2: {"playerName": player2Name,
        "playerTeam": player2Team,
        "playerPrice": player2Price},
    3: {"playerName": player3Name,
        "playerTeam": player3Team,
        "playerPrice": player3Price},
    4: {"playerName": player4Name,
        "playerTeam": player4Team,
        "playerPrice": player4Price},
    }


loc = 1
while loc <= 4:
    globals()['player%s' % loc] = '<b>' + lineup[loc]["playerName"] + '</b> ' + lineup[loc]["playerTeam"] + ' <i>' + lineup[loc]["playerPrice"] + '</i>'
    loc += 1

risingOutput = '<b>FPL Soon To Rise</b><br /><br />'+''.join(player1)+'<br/>' + ''.join(player2)+'<br/>' + ''.join(player3)+'<br/>' + ''.join(player4)
print(risingOutput)