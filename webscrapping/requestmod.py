import requests
res = requests.get('link')

print(res.raise_for_status())

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)

playFile.close()