import os

print(os.getcwd()) #current working directory
# print(os.chdir())  #changing the direcotory
print(os.path.abspath('spam.png')) #shows the absolute path for the given file 
print(os.path.relpath('c:\\folder1\\folder2\\spam.png', "c:\\folder1")) #shows the relative path 

print(os.path.dirname('c:\\folder1\\folder2\\spam.png')) #prints the directory name
print(os.path.basename('c:\\folder1\\folder2\\spam.png')) #prints the base file

os.path.isfile() #checks if the given arugument is a file
os.path.isdir() #checks if the given argument is a directory

os.path.getsize() #returns the bytes of the size
os.listdir() #retruns the directories in folder

os.makedirs('c:\\delicious\\walnut\\waffles') #makes the directory with walnut waffles

#deleting a file
os.unlink('thefile')
os.rmdir() #folder has to be competely empty
