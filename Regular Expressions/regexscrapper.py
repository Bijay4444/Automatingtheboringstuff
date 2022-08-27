import re, pyperclip

#  Create a regex for phone numbers
numRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345, ext. 12345, x12345
    (
    ((\d\d\d)|(\(\d\d\d\)))?    #areacode(optional)
    (\s|-)    #first separator
    \d\d\d    #first three digit
    -    #sepator
    \d\d\d\d    #last 4 digits
    (((ext(\.)?\s)|x)   #extension word-part(optional)
    (\d{2,5}))?    #extension number part(optional)
    )
''', re.VERBOSE)

#Create a regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5})?.com

[a-z0-9A-Z_.+]+    #name part
@                  # @symbol
[a-z0-9A-Z_.+]+    #domain name part

''', re.VERBOSE)

#Get the tex off the clipboard
text = pyperclip.paste()

#Extract the email/phone from the text
extractedNum = numRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedNum:
    allPhoneNumbers.append(phoneNumber[0])

#Copy the extracted email/phone to the clipboard
resutls = '\n'.join(allPhoneNumbers) + '\n' +'\n'.join(extractedEmail)
pyperclip.copy(resutls)