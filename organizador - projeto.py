import os
import shutil

to_dir = "c:/Users/maxfr/Documents/"
from_dir = "c:/Users/maxfr/Downloads/"

list_files = os.listdir(from_dir)
print(list_files)

for fileName in list_files:
    name,extension = os.path.splitext(fileName)
    print(name)
    print(extension)

    if(extension == " "):
        continue
    if(extension in [".txt", ".doc", ".docx", ".pdf"]):
        path1 = from_dir + fileName
        path2 = to_dir + "downloads"
        path3 = to_dir + "downloads/" + fileName
        
        if(os.path.exists(path2)):
            print("movendo o arquivo " + fileName)
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("movendo o arquivo " + fileName)
            shutil.move(path1,path3)

