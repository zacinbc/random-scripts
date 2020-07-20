from itertools import product
from string import ascii_letters, digits
import urllib.request, urllib.error
import requests
for i in product(ascii_letters + digits, repeat=7):
    with open('all_list.txt', 'a+') as f:
        f.write("%s\n" % ''.join(i))
for links in open("all_list.txt", "r"):
    b=requests.get("http://discordapp.com/api/v6/invites/"+links+'?with_counts=true')
    if b=='<Response [200]>':
        with open('good_list.txt', 'w') as x:
            x.write("%s\n" % 'https://discord.gg/'+links)
print("done")