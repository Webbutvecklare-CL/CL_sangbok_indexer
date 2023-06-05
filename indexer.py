from os import listdir
from os.path import isfile, isdir, join
import json

def exportIndex(index):
    outfileName = "index.json"

    with open(outfileName, "w", encoding="utf8") as outfile:
        json.dump(index, outfile)
    print("\033[93m\n> Dumped index as .json file to: \n\033[0m", outfileName)

def indexFile(index, f):
    words = []
    with open(f[0], "r", encoding="utf8") as file:
        for line in file:
            words += sanitizeString(line).split()

    for w in words:
        if w not in index:
            index[w] = f[1]
        elif f[1] not in index[w]:
            index[w] = index[w] + " " + f[1]

def makeIndex(files):
    print("\033[93m\n> Indexing following files:\033[0m")
    if len(files) < 10:
        for f in files:
            print(" " + f[1])
    else:
        for f in files[:10]:
            print(" " + f[1])
        print("\033[93m And ({num}) other files...\033[0m".format(num= len(files)-10))

    index = {}
    for f in files:
        indexFile(index, f)

    print("\033[92m\n>[SUCCESS] Indexed {keycount} words!\033[0m".format(keycount = len(index.keys())))

    return index

def getFiles(path):
    print("\033[93m\n> Getting files in path:\n\033[0m", path)

    names = [f for f in listdir(path) if isfile(join(path, f))]
    files = [(path + "/" + f, f) for f in names if f[-3:] == ".md"]

    return files

def getFolder():
    folderpath = ""
    while not folderpath:
        path = input("\033[93m> Enter folder to be indexed: \033[0m")
        if not isdir(path):
            print("\033[31mSpecified path does not seem to exist...\033[0m")
            continue
        folderpath = path

    return folderpath

def sanitizeString(text):
    return ''.join(c for c in text if c not in "#_:.,*|/\"\'\\!?()[]\{\}+’´'").lower()


def main():
    print("\033[95mThis script indexes all markdown (.md) files in a given directory and exports the results as a json file.\nWritten by: Armin Baymani, jun 2023\033[0m", "\n")
    
    folderpath = getFolder()
    files = getFiles(folderpath)
    indexDict = makeIndex(files) 
    exportIndex(indexDict)
    #searchTester(indexDict)

    input("\033[4m\n> Press any key to continue...\033[0m")

#Crude search for testing purposes
"""
def searchTester(index):
    while True:
        query = sanitizeString(input("Query: ")).split()

        print("searching for:", query)

        matches = []
        for token in query:
            if not token in index:
                continue
            ms = index[token].split(" ")
            matches = [m for m in ms if m in matches or not matches]
        
        print(matches)
"""

main()