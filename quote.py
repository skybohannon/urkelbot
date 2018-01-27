import random
file_path = "/home/sky/hangoutsbot/hangupsbot/plugins/"
hackers_quotes = open('hackers.txt','r').read().splitlines()
ml_quotes = open('majorleague.txt','r').read().splitlines()
d = {}
d["Hackers"] = hackers_quotes
d["Major League"] = ml_quotes
which_list = random.choice(list(d))
quote = random.choice(d[which_list])
quote_output = "<b>" + which_list + " Quote!!!</b>\n\n" + quote
print(quote_output)