import os
from difflib import SequenceMatcher

def read_files(files):
    files_binary = []
    for eachFile in files:
        with open(os.getcwd()+'/sample/' + eachFile, 'rb') as f:
            files_binary.append(f.read())
    return files_binary

def pickValue(p):
    return p[2].size



if __name__ == "__main__":

    myfiles = os.listdir(os.getcwd()+'/sample')
    print(myfiles)
    files_binary = read_files(myfiles)
    foundResult = []
    i = 0
    size1= len(files_binary)
    for fileIndex1 in range(0, len(files_binary)):
        print(len(files_binary[fileIndex1]))
        for fileIndex2 in range(0, len(files_binary)):
            if fileIndex1 == fileIndex2:
                continue
            s = SequenceMatcher(None, files_binary[fileIndex1], files_binary[fileIndex2])
            foundResult.append([fileIndex1, fileIndex2, s.find_longest_match(0, len(files_binary[fileIndex1]), 0, len(files_binary[fileIndex2]))])


    longest = max(foundResult, key=pickValue)

    print("file name : {} ,offset: {}, file name : {}, offset2: {}, strand size: {} ".format(myfiles[longest[0]], longest[2].a,myfiles[longest[1]], longest[2].b , longest[2].size))
