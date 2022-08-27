# work with shutil module 
import shutil

shutil.copy('file location', 'destination') 
shutil.copy('file location', 'destination\\spam.txt') #helps to rename to spam.txt

#copying a folder
shutil.copytree('folder location', 'destination') #renaming is also same for the folders

#moving a file
shutil.move('file location', 'destination')

#renaming is done by moving a file to same folder with new name
shutil.move('filelocation/name', 'filelocation/name')

 