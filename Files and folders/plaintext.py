import shelve

#opening file in read mode
helloFile = open('text.txt')
content = helloFile.read()

#readlines method return list of strings
helloFile.readline()

#opening a file in write mode
helloFile = open('text2.txt', 'w') #to open in append mode pass 'a'
helloFile.write('Hello!!!!, how are you?. Whats up')
helloFile.close()

#working in append mode which doesnt overwite the content
helloFile = open('text2.txt', 'a')
helloFile.write('\n I am good.')
helloFile.close()

#working with shelve library which acts like a dictioniary
shelFile = shelve.open('mydata')
shelFile['dogs'] = ['burno', 'tommy', 'kun']
shelFile.close()

shelFile = shelve.open('mydata')
print(shelFile['dogs'])
shelFile.close()

shelFile.keys()     #they also have key values pairs
shelFile.values()
