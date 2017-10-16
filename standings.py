import urllib.request
from bs4 import BeautifulSoup

url = 'https://fplmystats.com/league/116940/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

string = 'tbody tr:nth-of-type(1) td:nth-of-type(2), \
        tbody tr:nth-of-type(2) td:nth-of-type(2), \
        tbody tr:nth-of-type(3) td:nth-of-type(2), \
        tbody tr:nth-of-type(4) td:nth-of-type(2), \
        tbody tr:nth-of-type(5) td:nth-of-type(2), \
        tbody tr:nth-of-type(6) td:nth-of-type(2), \
        tbody tr:nth-of-type(7) td:nth-of-type(2), \
        tbody tr:nth-of-type(8) td:nth-of-type(2), \
        tbody tr:nth-of-type(9) td:nth-of-type(2), \
        tbody tr:nth-of-type(10) td:nth-of-type(2), \
        tbody tr:nth-of-type(11) td:nth-of-type(2), \
        tbody tr:nth-of-type(12) td:nth-of-type(2)'

data = soup.select(string)
print(data)

team1Owner = data[0].text.strip()
team2Owner = data[1].text.strip()
team3Owner = data[2].text.strip()
team4Owner = data[3].text.strip()
team5Owner = data[4].text.strip()
team6Owner = data[5].text.strip()
team7Owner = data[6].text.strip()
team8Owner = data[7].text.strip()
team9Owner = data[8].text.strip()
team10Owner = data[9].text.strip()
team11Owner = data[10].text.strip()
team12Owner = data[11].text.strip()

top = {
    1: {"teamName": team1Owner},
    2: {"teamName": team2Owner},
    3: {"teamName": team3Owner},
    4: {"teamName": team4Owner},
    5: {"teamName": team5Owner},
    6: {"teamName": team6Owner},
    7: {"teamName": team7Owner},
    8: {"teamName": team8Owner},
    9: {"teamName": team9Owner},
    10: {"teamName": team10Owner},
    11: {"teamName": team11Owner},
    12: {"teamName": team12Owner}
    }



loc = 1
while loc <= 12:
    globals()['team%s' % loc] = str(loc) + '. <b>' + top[loc]["teamName"] + '</b>'
    loc += 1

topOutput = '<b>FPL Standings</b><br /><br />' + ''.join(team1) + '<br/>' + ''.join(team2) + '<br/>' + ''.join(team3) + '<br/>' + ''.join(team4) + '<br/>' + ''.join(team5) + '<br/>' + ''.join(team6) + '<br/>' + ''.join(team7) + '<br/>' + ''.join(team8) + '<br/>' + ''.join(team9) + '<br/>' + ''.join(team10) + '<br/>' + ''.join(team11) + '<br/>' + ''.join(team12)
print(topOutput)