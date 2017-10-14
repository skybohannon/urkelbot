import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.fplstatistics.co.uk/Home/IndexWG'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

string = 'tbody tr:nth-of-type(1) td:nth-of-type(1), tbody tr:nth-of-type(1) td:nth-of-type(2), \
tbody tr:nth-of-type(1) td:nth-of-type(6), tbody tr:nth-of-type(2) td:nth-of-type(1), \
tbody tr:nth-of-type(2) td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(6), \
tbody tr:nth-of-type(3) td:nth-of-type(1), tbody tr:nth-of-type(3) td:nth-of-type(2), \
tbody tr:nth-of-type(3) td:nth-of-type(6), tbody tr:nth-of-type(4) td:nth-of-type(1), \
tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(6)'

data = soup.select(string)
player1Name = data[0].text.strip()
player1Team = data[1].text.strip()
player1Price = data[2].text.strip()
player2Name = data[3].text.strip()
player2Team = data[4].text.strip()
player2Price = data[5].text.strip()
player3Name = data[6].text.strip()
player3Team = data[7].text.strip()
player3Price = data[8].text.strip()

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
    }

player1 = '<b>' + lineup[1]["playerName"] + '</b> ' + lineup[1]["playerTeam"] + ' <i>' + lineup[1]["playerPrice"] + '</i><br />'
player2 = '<b>' + lineup[2]["playerName"] + '</b> ' + lineup[2]["playerTeam"] + ' <i>' + lineup[2]["playerPrice"] + '</i><br />'
player3 = '<b>' + lineup[3]["playerName"] + '</b> ' + lineup[3]["playerTeam"] + ' <i>' + lineup[3]["playerPrice"] + '</i>'

risingOutput = '<b>FPL Soon To Rise</b><br /><br />'+''.join(player1)+''.join(player2)+''.join(player3)
print(risingOutput)
