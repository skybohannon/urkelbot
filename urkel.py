"""
Rust server status
"""

import plugins
import requests
import re
import subprocess
import urllib.parse
from bs4 import BeautifulSoup
from datetime import date
import json
import io
import os
import aiohttp

def _initialize(bot):
    plugins.register_user_command(["rust"])
    plugins.register_user_command(["players"])
    plugins.register_user_command(["uptime"])
    plugins.register_user_command(["wipe"])
    plugins.register_user_command(["recipe"])

def rust(bot, event, *args):
    if "ping" in args:
        ping_stuff = ping()
        yield from bot.coro_send_message(event.conv_id, ping_stuff)
    else:
        server_stuff = get_status()
        yield from bot.coro_send_message(event.conv_id, server_stuff)


def players(bot, event, *args):
    players = get_status(players=True)
    yield from bot.coro_send_message(event.conv_id, players)


def uptime(bot, event, *args):
    proc = subprocess.check_output(['uptime']).decode('utf-8')
    time = re.search(r'up (.*?),', proc)
    proc2 = subprocess.check_output(['uptime', '-p']).decode('utf-8').strip("\n")
    time_pretty = re.search(r'up (.*)?', proc2)
    time_strings = [time_pretty.group(1), "(" + time.group(1) + ")"]
    time_stuff = " ".join(time_strings)
    yield from bot.coro_send_message(event.conv_id, time_stuff)


def wipe(bot, event, *args):
    # get todays date info
    year = date.today().year
    month = date.today().month
    next_month = date(year, month + 1, 1)
    # A janky work around for when server wipe is 1 day away
    days_till = 1

    # How many days until first thursday?
    for num in range(0, 7):
        test_day = (next_month.weekday() + num)
        if test_day == 3:
            first_thursday = date(year, month + 1, 2 + num)
            days_till = (first_thursday - date.today()).days
            print(days_till)
            break
        else:
            continue

    serverwipe_strings = [str(days_till), 'days until server wipe']
    serverwipe_stuff = " ".join(serverwipe_strings)
    yield from bot.coro_send_message(event.conv_id, serverwipe_stuff)


def recipe(bot, event, *args):
    # parse the hangouts command arguments
    query_strings = []
    for a in args:
        query_strings.append(a)

    # Set API stuff from f2k
    api_key = '99682f94b4a4c3498ca3c691cbcf751b'
    url = 'http://food2fork.com/api/search?key=' + api_key + '&q=' + "%20".join(query_strings)

    # Make the request and turn it into something readable
    response = requests.get(url)
    jase = json.loads(response.text)

    # parse the good stuff out of the JSON
    title = jase['recipes'][0]['title']
    link_image = jase['recipes'][0]['image_url']
    source_url = jase['recipes'][0]['source_url']

    # Set things up to send to hangouts
    recipe_strings = [title, source_url]
    recipe_stuff = " ".join(recipe_strings)
    filename = os.path.basename(link_image)
    r = yield from aiohttp.request('get', link_image)
    raw = yield from r.read()
    image_data = io.BytesIO(raw)
    image_id = yield from bot._client.upload_image(image_data, filename=filename)
    yield from bot.coro_send_message(event.conv.id_, recipe_stuff, image_id=image_id)


def get_status(players=False):
    url = 'https://rust-servers.net/server/79936/'
    header = {'User-Agent': 'Mozilla/5.0'}
    r = urllib.request.Request(url=url, headers=header)
    page = urllib.request.urlopen(r)
    soup = BeautifulSoup(page.read(), "lxml")
    string = '.span7 tr:nth-of-type(4) strong , .table-bordered small , .span7 .badge-success , .span7 tr:nth-of-type(2) strong , .fa-power-off+ strong'
    data = soup.select(string)

    servername = data[5].contents[0].strip()
    numplayers = "Current players: " + data[1].contents[0].strip()
    last_check = data[2].contents[0].strip()
    status = data[3].contents[0].strip()
    rust_strings = [servername, status, numplayers, last_check]

    if players is True:
        return numplayers
    else:
        print(" ".join(rust_strings))
        return ("<br/>".join(rust_strings))


def ping():
    server = "209.95.56.13"
    proc = subprocess.check_output(['ping', '-c1', server])
    return ping == 0