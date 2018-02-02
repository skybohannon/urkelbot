"""
urkelbot v1.5
           _________._____ /\__.____.
           \    ___/     //   /_   / \_
         __ \\__   /   _/ \____/__,   /
   _____/__________\___\____ / /_    /
   \     _/__._______\   ___/_.__\  /_._______._______._______.________
   /    _    \  __   //       \___\/   \_   _  \_   _  \_  __  \_   _  \_
  /    _/    /  \   _/    /  _/   _/    /   /   /   /   /  \    /   /   /
  \____\____/\\_____\____/___\  ______//___/___/___/___/\\_____/___/___/
                              \/
"""
from __future__ import print_function
from datetime import datetime
from bs4 import BeautifulSoup
import plugins
import random
import re
import subprocess
import urllib.parse
import urllib.request
import json
import os
import pytz
import aiohttp
import io

file_path = "/home/sky/hangoutsbot/hangupsbot/plugins/"

def _initialize(bot):
    plugins.register_user_command(["uptime"])
    plugins.register_user_command(["rising"])
    plugins.register_user_command(["standings"])
    plugins.register_user_command(["dogfacts"])
    plugins.register_user_command(["catfacts"])
    plugins.register_user_command(["hackers"])
    plugins.register_user_command(["majorleague"])
    plugins.register_user_command(["quote"])
    plugins.register_user_command(["crypto"])
    plugins.register_user_command(["symbol"])
    plugins.register_user_command(["table"])
    plugins.register_user_command(["scores"])
    plugins.register_user_command(["fortune"])
    plugins.register_user_command(["binance"])
    plugins.register_user_command(["np"])
    plugins.register_user_command(["top10"])


def uptime(bot, event):
    proc1 = subprocess.check_output(['uptime']).decode('utf-8').strip("\n")
    time = re.search(r'up (.* days)?', proc1)
    proc2 = subprocess.check_output(['uptime', '-p']).decode('utf-8').strip("\n")
    time_pretty = re.search(r'up (.*)?', proc2)
    if time.group(1) is not None:
        time_strings = [time_pretty.group(1), "(" + time.group(1) + ")"]
        time_stuff = " ".join(time_strings)
    else:
        time_strings = [time_pretty.group(1)]
        time_stuff = " ".join(time_strings)
    yield from bot.coro_send_message(event.conv_id, time_stuff)


def dogfacts (bot, event):
    lines = open(file_path + "dogfacts.txt","r").read().splitlines()
    dogFact=random.choice(lines)
    print(dogFact)
    dogFactAll = "<b>DOG FACTS!!!</b>\n\n" + dogFact
    
    yield from bot.coro_send_message(event.conv_id, dogFactAll)


def catfacts(bot, event):
    catFact = "<b>CAT FACTS!!!</b>\n\n" + "Cats are stupid"
    yield from bot.coro_send_message(event.conv_id, catFact)


def hackers (bot, event):
    lines = open(file_path + "hackers.txt","r").read().splitlines()
    hackersQuote=random.choice(lines)
    print(hackersQuote)
    
    yield from bot.coro_send_message(event.conv_id, hackersQuote)


def majorleague(bot, event):
    lines = open(file_path + "majorleague.txt", "r").read().splitlines()
    mlQuote = random.choice(lines)
    print(mlQuote)

    yield from bot.coro_send_message(event.conv_id, mlQuote)


def quote(bot,event):
    hackers_quotes = open(file_path + 'hackers.txt', 'r').read().splitlines()
    ml_quotes = open(file_path + 'majorleague.txt', 'r').read().splitlines()
    d = {}
    d["Hackers"] = hackers_quotes
    d["Major League"] = ml_quotes
    which_list = random.choice(list(d))
    quote = random.choice(d[which_list])
    quote_output = "<b>" + which_list + " Quote!!!</b>\n\n" + quote
    print(quote_output)
    yield from bot.coro_send_message(event.conv_id, quote_output)


def rising(bot, event):
    url = 'http://www.fplstatistics.co.uk/Home/IndexWG'
    header = {'User-Agent': 'Mozilla/5.0'}

    r = urllib.request.Request(url=url, headers=header)
    page = urllib.request.urlopen(r)
    soup = BeautifulSoup(page.read(), "lxml")
    string = 'tbody tr:nth-of-type(1) td:nth-of-type(1), tbody tr:nth-of-type(1) td:nth-of-type(2), \
    tbody tr:nth-of-type(1) td:nth-of-type(6), tbody tr:nth-of-type(2) td:nth-of-type(1), tbody tr:nth-of-type(2) \
    td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(6), tbody tr:nth-of-type(3) td:nth-of-type(1), \
    tbody tr:nth-of-type(3) td:nth-of-type(2), tbody tr:nth-of-type(3) td:nth-of-type(6), tbody tr:nth-of-type(4) \
    td:nth-of-type(1), tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(6)'
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

    player1 = '<b>' + lineup[1]["playerName"] + '</b> ' + lineup[1]["playerTeam"] + ' <i>' + lineup[1][
        "playerPrice"] + '</i><br />'
    player2 = '<b>' + lineup[2]["playerName"] + '</b> ' + lineup[2]["playerTeam"] + ' <i>' + lineup[2][
        "playerPrice"] + '</i><br />'
    player3 = '<b>' + lineup[3]["playerName"] + '</b> ' + lineup[3]["playerTeam"] + ' <i>' + lineup[3][
        "playerPrice"] + '</i>'

    risingOutput = '<b>FPL Soon To Rise</b><br /><br />' + ''.join(player1) + ''.join(player2) + ''.join(player3)
    yield from bot.coro_send_message(event.conv_id, risingOutput)


def standings(bot, event):
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

    topOutput = '<b>FPL Standings</b><br /><br />' + ''.join(team1) + '<br/>' + ''.join(team2) + '<br/>' + ''.join(
        team3) + '<br/>' + ''.join(team4) + '<br/>' + ''.join(team5) + '<br/>' + ''.join(team6) + '<br/>' + ''.join(
        team7) + '<br/>' + ''.join(team8) + '<br/>' + ''.join(team9) + '<br/>' + ''.join(team10) + '<br/>' + ''.join(
        team11) + '<br/>' + ''.join(team12)
    print(topOutput)
    yield from bot.coro_send_message(event.conv_id, topOutput)


def crypto(bot, event):
    urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=0"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    crypto_list = json.loads(data.decode(encoding))

    for coin in crypto_list:
        if coin["id"] == "bitcoin":
            btc_price = float(coin["price_usd"])
            btc_change = float(coin["percent_change_24h"])
        elif coin["id"] == "bitcoin-cash":
            bch_price = float(coin["price_usd"])
            bch_change = float(coin["percent_change_24h"])
        elif coin["id"] == "ethereum":
            eth_price = float(coin["price_usd"])
            eth_change = float(coin["percent_change_24h"])
        elif coin["id"] == "icon":
            icx_price = float(coin["price_usd"])
            icx_change = float(coin["percent_change_24h"])
        elif coin["id"] == "litecoin":
            ltc_price = float(coin["price_usd"])
            ltc_change = float(coin["percent_change_24h"])
        elif coin["id"] == "stellar":
            xlm_price = float(coin["price_usd"])
            xlm_change = float(coin["percent_change_24h"])
        elif coin["id"] == "raiblocks":
            xrb_price = float(coin["price_usd"])
            xrb_change = float(coin["percent_change_24h"])
        elif coin["id"] == "kucoin-shares":
            kcs_price = float(coin["price_usd"])
            kcs_change = float(coin["percent_change_24h"])
        elif coin["id"] == "ripple":
            xrp_price = float(coin["price_usd"])
            xrp_change = float(coin["percent_change_24h"])
        elif coin["id"] == "vechain":
            ven_price = float(coin["price_usd"])
            ven_change = float(coin["percent_change_24h"])
        elif coin["id"] == "binance-coin":
            bnb_price = float(coin["price_usd"])
            bnb_change = float(coin["percent_change_24h"])

    crypto_output = "<b>BTC</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>BCH</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>ETH</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>LTC</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>BNB</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>ICX</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>KCS</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>VEN</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>XLM</b>: ${:,.3f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>XRB</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                    "<b>XRP</b>: ${:,.2f}  (<i>{:+.2f}%</i>)" \
        .format(btc_price, btc_change, bch_price, bch_change, eth_price, eth_change, ltc_price, ltc_change, bnb_price, bnb_change, icx_price, icx_change, kcs_price, kcs_change, ven_price, ven_change, xlm_price, xlm_change, xrb_price, xrb_change, xrp_price, xrp_change)

    yield from bot.coro_send_message(event.conv_id, crypto_output)


def symbol(bot, event, sym):

    urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=0"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    crypto_list = json.loads(data.decode(encoding))

    sym = sym.upper()

    for coin in crypto_list:

        if coin["symbol"] == sym:
            coin_name = coin["name"]
            usd_price = float(coin["price_usd"])
            btc_price = float(coin["price_btc"])
            change_7d = float(coin["percent_change_7d"])
            change_24h = float(coin["percent_change_24h"])
            change_1h = float(coin["percent_change_1h"])

            symbol_output = "<b>" + coin_name + " (" + sym + ")</b>\n\n<b>USD</b>: ${:,.3f}\n" \
                            "<b>BTC</b>: {:.7f}\n" \
                            "<b>7D Change</b>: {:+.2f}%\n" \
                            "<b>24H Change</b>: {:+.2f}%\n" \
                            "<b>1H Change</b>: {:+.2f}%" \
                            .format(usd_price, btc_price, change_7d, change_24h, change_1h)
            break
        else:
            symbol_output = "There was no match for <b>\"{}\"</b>".format(sym)

    yield from bot.coro_send_message(event.conv_id, symbol_output)


def table(bot, event):

    with open(file_path + "premkey.txt", "r") as apikey:
        key = apikey.read()

    urlData = "http://api.football-api.com/2.0/standings/1204?Authorization=" + key

    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    prem_table = json.loads(data.decode(encoding))

    table_dict = {}
    game_week = prem_table[0]["round"]

    for team in prem_table:
        team_posi = int(team["position"])

        table_dict[team_posi] = {
            "name": team["team_name"],
            "points": team["points"],
            "form": team["recent_form"],
            "gd": team["gd"],
            "gs": team["overall_gs"],
            "ga": team["overall_ga"],
            "position": team["position"]
        }

    print_string = ""
    for i in range(len(table_dict)):
        print_string = print_string + "<b>" + str(i + 1) + "</b> - " + table_dict[i + 1]["name"] + " (" + \
                       table_dict[i + 1]["points"] + ")\n"

    print_string = "<b>Premier League GW{}</b>\n\n".format(game_week) + print_string[:-1]

    yield from bot.coro_send_message(event.conv_id, print_string)


def scores(bot, event):

    with open(file_path + "premkey.txt", "r") as apikey:
        key = apikey.read()

    # Convert time to normal time instead of military time, change time zone to Central
    def time_convert(time):

        mil_time = time
        hours, minutes = mil_time.split(":")
        hours, minutes = int(hours) - 6, int(minutes)
        am_pm = "AM"

        if hours > 12:
            am_pm = "PM"
            hours -= 12
        return "{}:{:02d}".format(hours, minutes) + am_pm

    # Check events for goals, then return goals
    def get_events(l):
        events = ""
        event_list = []
        for i in range(len(l)):
            if l[i]["type"] == "goal":
                player = l[i]["player"]
                minute = l[i]["minute"]
                single_event = player + " " + minute + "'"
                event_list.append(single_event)
                events = ", ".join(event_list)
                i += 1
        return events

    tz = pytz.timezone('America/Chicago')
    current_date = datetime.now(tz=tz).strftime("%d.%m.%Y")

    urlData = "http://api.football-api.com/2.0/matches?comp_id=1204&match_date=" + current_date + "&Authorization=" + key

    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    matches = json.loads(data.decode(encoding))

    matches_dict = {}
    matches_date = matches[0]["formatted_date"]
    matches_date = datetime.strptime(matches_date, '%d.%m.%Y').strftime('%m/%d/%Y')

    def get_events(l):
        events = ""
        event_list = []
        for i in range(len(l)):
            if l[i]["type"] == "goal":
                player = l[i]["player"]
                minute = l[i]["minute"]
                single_event = player + " " + minute + "'"
                event_list.append(single_event)
                events = ", ".join(event_list)
                i += 1
        return events

    count = 1
    for match in matches:
        match_id = count
        matches_dict[match_id] = {
            "home": match["localteam_name"],
            "visitor": match["visitorteam_name"],
            "home_score": match["localteam_score"],
            "visitor_score": match["visitorteam_score"],
            "status": match["status"],
            "events": match["events"]
        }

        try:
            matches_dict[match_id]["status"] = str(int(matches_dict[match_id]["status"])) + "'"
        except ValueError:
            matches_dict[match_id]["status"] = matches_dict[match_id]["status"]

        if len(matches_dict[match_id]["status"]) == 5:
            matches_dict[match_id]["status"] = time_convert(matches_dict[match_id]["status"])

        count += 1

    print_string = ""
    for i in range(len(matches_dict)):
        print_string = print_string + matches_dict[i + 1]["home"] + " <b>" + matches_dict[i + 1]["home_score"] + " - " + \
                       matches_dict[i + 1]["visitor_score"] + "</b> " + matches_dict[i + 1]["visitor"] + " " + \
                       matches_dict[i + 1]["status"] + "\n"
        if len(get_events(matches_dict[i + 1]["events"])) > 0:
            print_string = print_string + "<i>(" + get_events(matches_dict[i + 1]["events"]) + ")</i>\n\n"
        else:
            print_string = print_string + "\n"

    print_string = "<b>Match scores for " + matches_date + "</b>\n\n" + print_string[:-1]
    print(print_string)

    yield from bot.coro_send_message(event.conv_id, print_string)


def fortune(bot, event):
    fortune = subprocess.getoutput("/usr/games/fortune fortunes")
    print(fortune)
    yield from bot.coro_send_message(event.conv_id, fortune)


def np(bot, event, user):
    user = user.lower()

    if user == "sky":
        username = "sbohannon"
    elif user == "brett":
        username = "southcore"
    elif user == "brandon":
        username = "superprime"

    try:
        with open(file_path + "lastfm-" + user + "-api.txt", "r") as api_key:
            api_key = api_key.read()

        urlData = "https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + username + "&api_key=" + api_key + "&format=json"

        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        recent_tracks = json.loads(data.decode(encoding))
        recent_tracks.update(recent_tracks["recenttracks"])

        track_artist = recent_tracks["track"][0]["artist"]["#text"]
        track_title = recent_tracks["track"][0]["name"]
        track_art = recent_tracks["track"][0]["image"][3:4]
        track_art = track_art[0]["#text"]
        now_playing = "false"

        try:
            if recent_tracks["track"][0]["@attr"]["nowplaying"] == "true":
                now_playing = "true"
        except KeyError:
            now_playing = "false"

        if now_playing == "true":
            now_playing = "<b>{}'s Now Playing</b>:\n".format(user.capitalize()) + track_artist + " - " + track_title
        else:
            now_playing = "<b>{}'s Last Played Track</b>:\n".format(
                user.capitalize()) + track_artist + " - " + track_title
        try:
            filename = os.path.basename(track_art)
            r = yield from aiohttp.request('get', track_art)
            raw = yield from r.read()
            image_data = io.BytesIO(raw)
            image_id = yield from bot._client.upload_image(image_data, filename=filename)
            yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)
        except ValueError:
            pass

    except FileNotFoundError:
        now_playing = "Could not find user {}".format(user)

    yield from bot.coro_send_message(event.conv_id, now_playing)


def top10(bot, event, user):
    user = user.lower()

    if user == "sky":
        username = "sbohannon"
    elif user == "brett":
        username = "southcore"
        user = "brett"
    elif user == "brandon":
        username = "superprime"

    try:
        with open(file_path + "lastfm-" + user + "-api.txt", "r") as api_key:
            api_key = api_key.read()
    except FileNotFoundError:
        return "Could not find user {}".format(user)

    urlData = "https://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user=" + username + "&api_key=" + api_key + "&format=json"

    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    weekly_chart = json.loads(data.decode(encoding))
    weekly_chart.update(weekly_chart["weeklyartistchart"])

    top_artists = {}
    counter = 0
    for item in weekly_chart["artist"]:
        top_artists[counter] = {
            "artist": item["name"],
            "playcount": item["playcount"],
            "rank": item["@attr"]["rank"]
        }
        counter += 1

    top_10 = "<b>{}'s Top 10 Artists of the Week</b>:\n\n".format(user.capitalize())
    for i in range(0,10):
        top_10 = top_10 + "<b>" + str(i+1) + "</b>. " + top_artists[i]["artist"] + " (<i>" + top_artists[i]["playcount"] + "</i>)\n"

    top_10 = top_10[:-1]

    print(top_10)
    yield from bot.coro_send_message(event.conv_id, top_10)
