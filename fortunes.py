import subprocess
import os

fortune = subprocess.getoutput("/usr/games/fortune fortunes")
print(fortune)