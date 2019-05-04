import os
import time
import zipfile
import pathlib

## Config me!
ROOT_DIR = "C:/Users/jonas/temp"
COMPRESS_FILES_OLDER_THAN_MINUTES = 180

## Dont touch!
FOLDER_ZIP_KEYWORD = "katalog"
FOLDER_EXCLUDE_KEYWORD = "COMPRESSED"

# #######################################################
# Returns all files in a dir that are older than x hours
# #######################################################
def getAllOldFilesInDir(path):

    timeNow = time.time()
    oldFiles = {}
    listedFilesRaw = os.listdir(path)

    for nextEntry in listedFilesRaw:
        completeFilePath = os.path.join(path, nextEntry)

        if os.path.isfile(completeFilePath):
            fileCreation = os.path.getctime(completeFilePath)
            twoHoursAgo = timeNow - COMPRESS_FILES_OLDER_THAN_MINUTES
            if fileCreation < twoHoursAgo:
                # This file should be compressed!
                oldFiles[nextEntry] = {"completeFilePath": completeFilePath, "fileName": nextEntry, "rootPath": path}

    return oldFiles

# #######################################################
# Returns all directories where we shall do compression
# #######################################################
def listAllValidDirs(rootPath, zipKeyword, excludeKeyword):

    directories = os.listdir(ROOT_DIR)
    finalDirList = []

    for nextDir in directories:

        if FOLDER_ZIP_KEYWORD not in nextDir or FOLDER_EXCLUDE_KEYWORD in nextDir:
            # Our keyword is not present, or our exclude word is present. Ignore
            continue

        finalDirList.append(os.path.join(rootPath, nextDir))

    return finalDirList

# #######################################################
# Compresses provided file according to fileInfo and removes
# file if compression was successful
# #######################################################
def compressAndMoveFile(fileInfo):

    zippedRootFolder = fileInfo['rootPath'] + "_" + FOLDER_EXCLUDE_KEYWORD
    zippedFileName = fileInfo['fileName'] + ".zip"
    zippedFilePath = os.path.join(zippedRootFolder, zippedFileName)

    try:
        pathlib.Path(zippedRootFolder).mkdir(parents=True, exist_ok=True)

        outZipHandle = zipfile.ZipFile(zippedFilePath, 'w')
        outZipHandle.write(fileInfo["completeFilePath"], arcname=fileInfo['fileName'], compress_type = zipfile.ZIP_DEFLATED)
        outZipHandle.close()
        os.remove(fileInfo["completeFilePath"])
        print(f"Compressed and deleted {fileInfo['completeFilePath']} and created {zippedFilePath}")
    except Exception as ex:
        print(f"ERROR while compressing a file {fileInfo},  {ex}")
        return


# #######################################################
# MAIN!
# #######################################################
if "__name__" == "__main__":
    allValidDirs = listAllValidDirs(ROOT_DIR, FOLDER_ZIP_KEYWORD, FOLDER_EXCLUDE_KEYWORD)

    for nextValidDir in allValidDirs:
        listedFiles = getAllOldFilesInDir(nextValidDir)

        for nextFile, fileInfo in listedFiles.items():
            compressAndMoveFile(fileInfo)







apa = 88

if apa > 0:
    print("pappa är noob")

while  apa <10:
    print ("apa")
    apa = apa + 1






exit(0)







variabel = 0
pappa = "näst sämst"




while variabel < 777:
    print(" pappa är best#inte så troligt men kanske")
    variabel = variabel+1
    print( pappa + " alla dagar")
    print(variabel)


exit(0)















minText = "pappa är en idiot"

print("theodor elskar pappa# " + minText)




a = 3
b=10000000000000
print(f"hej {b}")

print("pappa är den besta pappa i världen# " + minText)

x = "nisse"

while True:
    print(f"Pappa är {x} gånger bättre än alla")
    x = x +minText





