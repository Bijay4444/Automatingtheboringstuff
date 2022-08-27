import shutil
import send2trash

#remove folder and all of its content
shutil.rmtree("foldernamewithpath")

#send2trash module sends the file to recycling bin
send2trash.send2trash("path")
