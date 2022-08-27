print(r'Hellow \how are you')  #r- raw string
spam = "What's Up"
spam.upper()
spam.lower()
spam.islower()
spam.isupper() #boolean values
spam.isalpha()
spam.isalnum()
spam.isdecimal()
spam.isspace() 
spam.istitle() #begins with uppercase char 

spam.startswith('Hellow')
spam.endswith('you')

','.join(['cats','rats', 'bats']) #seperates the strings with comma

'My name is cole'. split('m') #splits with the letter m

'Hello'.rjust(10)   #justifies string with whitespaces left or right
'Hello'.ljust(10)
'Hello'.center(20, '=') #centers the text

spam.strip() #removes the white space
spam.lstrip() 
spam.rstrip()

spam = "Hi there!"
spam.replace('e', 'XYZ')

