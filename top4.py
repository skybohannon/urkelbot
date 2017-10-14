import urllib.request
from bs4 import BeautifulSoup

url = 'https://fplmystats.com/league/116940/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

string = 'tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(3), \
        tbody tr:nth-of-type(2) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(3), \
        tbody tr:nth-of-type(3) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(3) td:nth-of-type(3), \
        tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(3)'


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
        }
    }


loc = 1
while loc <= 4:
    globals()['team%s' % loc] = str(loc) + '. <b>' + top[loc]["teamName"] + '</b>'
    loc += 1

top4Output = '<b>FPL Top 4</b><br /><br />' + ''.join(team1) + '<br/>' + ''.join(team2) + '<br/>' + ''.join(team3) + '<br/>' + ''.join(team4)
print(top4Output)