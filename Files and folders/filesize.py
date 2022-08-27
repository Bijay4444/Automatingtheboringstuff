import os

totalSize = 0
for filename in os.listdir('C:\\Users\\Personal\\OneDrive\\My Projects\\Automating The Boring Stuff(Python)'):
    if not os.path.isfile(os.path.join('C:\\Users\\Personal\\OneDrive\\My Projects\\Automating The Boring Stuff(Python)', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\Personal\\OneDrive\\My Projects\\Automating The Boring Stuff(Python)', filename))

print(totalSize)


