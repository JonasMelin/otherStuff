from os import listdir
from os.path import isfile, join
import collections

from translate import Translator

#print(translator.translate('boken'))


# ###############################################################
# class....
# ###############################################################
class swedishMain():

    # ###############################################################
    # construct
    # ###############################################################
    def __init__(self, path):


        self.translatorEnSv = Translator(provider='mymemory', from_lang='en', to_lang='sv')
        self.translatorSvEn = Translator(provider='mymemory', from_lang='sv', to_lang='en')

        self.words = {}
        self.parseAllFiles(self.readFilesFromDisk(path))

        self.orderdByLetter = collections.OrderedDict(sorted(self.words.items()))
        self.printNice(self.orderdByLetter)
        #print(self.orderdByLetter)

        self.orderedByCount = sorted(self.words.items(), key=lambda kv: kv[1])
        self.printNice(self.orderedByCount)
        #print(self.orderedByCount)

        print(len(self.orderedByCount))


    def printNice(self, list):
        for nextElement in list:
            print("({count}) {sv} - {en}".format(count=list[nextElement]['count'],sv=nextElement, en=list[nextElement]['translation']))



    # ###############################################################
    # parseAllFiles
    # ###############################################################
    def parseAllFiles(self, fileList):

        for nextFile in fileList:
            self.parseFile(nextFile)

    # ###############################################################
    # construct
    # ###############################################################
    def removeBadCharacters(self, line):
        line = line.replace(".", " ")
        line = line.replace("?", " ")
        line = line.replace(",", " ")
        line = line.replace(":", " ")
        line = line.replace(";", " ")
        line = line.replace("!", " ")
        line = line.replace("-", " ")
        line = line.replace(">", " ")
        line = line.replace("<", " ")
        line = line.replace("#", " ")
        line = line.replace("&", " ")
        line = line.replace("(", " ")
        line = line.replace(")", " ")
        line = line.replace("=", " ")
        line = line.replace("\"", " ")

        line = line.replace("\n", "")
        return line

    # ###############################################################
    # construct
    # ###############################################################
    def isWordDigit(self, word):
        try:
            int(word)
            return True
        except:
            return False

    # ###############################################################
    # construct
    # ###############################################################
    def parseFile(self, file):

        #translator = Translator()

        with open(file) as f:
            for line in f:

                try:


                    if "-->" in line:
                        continue
                    if len(line) < 2:
                        continue
                    line = self.removeBadCharacters(line)

                    words = line.split(" ")

                    for word in words:
                        word = word.replace(" ", "")
                        if len(word) < 2:
                            continue

                        word = word.lower()

                        if self.isWordDigit(word):
                            continue


                        if word in self.words:
                            self.words[word]['count'] += 1
                        else:
                            self.words[word] = {'count' : 1, 'translation': self.translatorSvEn.translate(word).lower()}
                            print("{a} - {b}".format(a=word, b=self.words[word]['translation']))
                except Exception as ex:
                    pass




    # ###############################################################
    # Reads relevant files from a path
    # ###############################################################
    def readFilesFromDisk(self, mypath):

        everything = listdir(mypath)
        onlyFiles = []

        for nextElement in everything:
            fullPath = join(mypath,nextElement)
            if isfile(fullPath) and ".srt" in fullPath:
                onlyFiles.append(fullPath)

        return onlyFiles





sm = swedishMain('C:/Users/jonas/PycharmProjects/swedish/venv/src/data')
