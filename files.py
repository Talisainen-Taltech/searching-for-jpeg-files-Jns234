import os

fileFolder = "./random_files/"

files = os.listdir(fileFolder)


for file in files:
    fileBin = open(fileFolder + file, "rb")
    binRow = fileBin.read()
    oldFileName = fileFolder + file

    if binRow[0] == 255 and binRow[1] == 216:
        newFileName = oldFileName + ".jpg"
        os.rename(oldFileName, newFileName)
        print(newFileName)
    else:
        os.remove(oldFileName)
    