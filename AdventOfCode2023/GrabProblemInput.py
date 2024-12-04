#https://adventofcode.com/auth/github

import requests
import os

year = 2023
day = 5
uri = f'https://adventofcode.com/{year}/day/{day}/input'
payload = {'session': '53616c7465645f5fa1cc8aa400945664f7249041937be7eef0a19685b550df75b8f003dde604bae4becf6c0a75e352064e829272346f7b809df6f04cc414dbad'}
response = requests.get(uri, cookies=payload) #cookies={'session': '53616c7465645f5fa1cc8aa400945664f7249041937be7eef0a19685b550df75b8f003dde604bae4becf6c0a75e352064e829272346f7b809df6f04cc414dbad'}, headers={'User-Agent': 'USER_AGENT'})

if not os.path.exists(f"Day{day}"):
    print("Creating Directory")
    os.makedirs(f"Day{day}")
if not os.path.exists(f"Day{day}/input.txt"):
    print("Creating Input")
    savefile = open(f"Day{day}/input.txt", "w")
    savefile.write(response.text)
    savefile.close()

