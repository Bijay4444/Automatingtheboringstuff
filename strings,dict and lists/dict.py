myCat = {
        'size': 'fat',
        'color': 'gray', 
        'dispositionn': 'loud'
}

print('size' in myCat)
print(myCat.keys())
print(myCat.values())
print(myCat.items())


for k,v in myCat.items():
    print(k, v)

print(myCat.get('size', ''))