import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me 415-555-1011 tomorrow, or at 415-555-9999.')
print(mo.group())

#for area code only we divide them in group using paranethesis

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-9999')
print(mo.group(1))

# for finding the actual paranthesis in the string.

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is (415) 555-9999')
print(mo.group())

#prefix patterns
batRegex = re.compile(r'bat(man|mobile|copter|bat)')
mo = batRegex.search("I am batman and i have a batmobile with batcopter inside it.")
print(mo.group())

#? expression = 0 or one
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("I am the Batwoman")
print(mo.group())

#* expression = 0 or more
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search("I am the Batwoman and Batman")
print(mo.group())

# + expression = 1 or more
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search("I am the Batwoman and Batman")
print(mo.group())

# {} expression = exact
haRegex = re.compile(r'(ha){3}')
mo = haRegex.search(r'He said "hahaha"')
print(mo.group())

# three phone number in a row
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group())

#findaall and characters
lyrics ='12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking , 7 swans swimming, 6 geese alaying, 5 golden rings, 4 collaing birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

#finding names using .* patterns
name = "First Name: Bijay Last Name: Khadka"
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(name))

#finding all newline string
prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law.'
primeRegex = re.compile(r'.*', re.DOTALL)
print(primeRegex.findall(prime))

#vowels
vowelRegex = re.compile(r'[aeiou]', re.I) #ignonres case sensitivity
print(vowelRegex.findall('What is you Name AAAAA'))

#substitute method
namesRegex = re.compile(r'Agent \w+')
namesRegex.findall('Agent Binod gave the secret documents to Agent scarn.')
print(namesRegex.sub('REDACTED','Agent Binod gave the secret documents to Agent scarn.'))