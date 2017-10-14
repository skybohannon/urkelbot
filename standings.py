import urllib.request
from bs4 import BeautifulSoup

url = 'https://fplmystats.com/league/116940/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

string = 'tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(3), \
        tbody tr:nth-of-type(2) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(3), \
        tbody tr:nth-of-type(3) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(3) td:nth-of-type(3), \
        tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(3), \
        tbody tr:nth-of-type(5) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(5) td:nth-of-type(3), \
        tbody tr:nth-of-type(6) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(6) td:nth-of-type(3), \
        tbody tr:nth-of-type(7) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(7) td:nth-of-type(3), \
        tbody tr:nth-of-type(8) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(8) td:nth-of-type(3), \
        tbody tr:nth-of-type(9) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(9) td:nth-of-type(3), \
        tbody tr:nth-of-type(10) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(10) td:nth-of-type(3), \
        tbody tr:nth-of-type(11) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(11) td:nth-of-type(3), \
        tbody tr:nth-of-type(12) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(12) td:nth-of-type(3)'

data = soup.select(string)
print(data)

team1Owner = data[0].text.strip()
team1Points = data[1].text.strip()
team2Owner = data[2].text.strip()
team2Points = data[3].text.strip()
team3Owner = data[4].text.strip()
team3Points = data[5].text.strip()
team4Owner = data[6].text.strip()
team4Points = data[7].text.strip()
team5Owner = data[8].text.strip()
team5Points = data[9].text.strip()
team6Owner = data[10].text.strip()
team6Points = data[11].text.strip()
team7Owner = data[12].text.strip()
team7Points = data[13].text.strip()
team8Owner = data[14].text.strip()
team8Points = data[15].text.strip()
team9Owner = data[16].text.strip()
team9Points = data[17].text.strip()
team10Owner = data[18].text.strip()
team10Points = data[19].text.strip()
team11Owner = data[20].text.strip()
team11Points = data[21].text.strip()
team12Owner = data[22].text.strip()
team12Points = data[23].text.strip()

top = {
    1: {"teamName": team1Owner,
        "teamPoints": team1Points
        },
    2: {"teamName": team2Owner,
        "teamPoints": team2Points
        },
    3: {"teamName": team3Owner,
        "teamPoints": team3Points
        },
    4: {"teamName": team4Owner,
        "teamPoints": team4Points
        },
    5: {"teamName": team5Owner,
        "teamPoints": team5Points
        },
    6: {"teamName": team6Owner,
        "teamPoints": team6Points
        },
    7: {"teamName": team7Owner,
        "teamPoints": team7Points
        },
    8: {"teamName": team8Owner,
        "teamPoints": team8Points
        },
    9: {"teamName": team9Owner,
        "teamPoints": team9Points
        },
    10: {"teamName": team10Owner,
        "teamPoints": team10Points
        },
    11: {"teamName": team11Owner,
        "teamPoints": team11Points
        },
    12: {"teamName": team12Owner,
        "teamPoints": team12Points
        }
    }


loc = 1
while loc <= 12:
    globals()['team%s' % loc] = str(loc) + '. <b>' + top[loc]["teamName"] + '</b>'
    loc += 1

topOutput = '<b>FPL Standings</b><br /><br />' + ''.join(team1) + '<br/>' + ''.join(team2) + '<br/>' + ''.join(team3) + '<br/>' + ''.join(team4) + '<br/>' + ''.join(team5) + '<br/>' + ''.join(team6) + '<br/>' + ''.join(team7) + '<br/>' + ''.join(team8) + '<br/>' + ''.join(team9) + '<br/>' + ''.join(team10) + '<br/>' + ''.join(team11) + '<br/>' + ''.join(team12)
print(topOutput)