#copy module
import copy

# lists are mutable but strings are immutable
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8: 12]
print(newName)

#lists reference example

spam = [0, 1, 2, 3, 4, 5]
cheese = spam 
cheese[1] = 'Hello!'

print(cheese)
print(spam)

cheese = copy.deepcopy(spam)
cheese[1] = 'wassup'

print(cheese)
print(spam)