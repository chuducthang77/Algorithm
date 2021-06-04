#Fun program to generate randomly 3 questions for review
#Concentrate on the program with the tag #TOREVIEW will have more weight
#Print out the file to keep track how many times to question have been reviewed
#Keep track the time spent on the review program
#Update the list of questions as the source of question is updating everyday

import os 
import tokenize
import random

def fileList(currentDir):
    #List all the files name in the current files and store in the list 
    #Input: currentDir
    #Return: list of all files
    fileName = []
    directory = os.listdir(currentDir)
    for dir in directory:
        if dir == '__pycache__':
            continue
        elif '.py' in dir:
            fileName.append(os.path.join(currentDir, dir))
        else:
            fileName += fileList(os.path.join(currentDir, dir))
    return fileName

if __name__ == '__main__':
    #Get the list of the files
    problems = fileList('Leetcode')

    #Randomly pick 3 problems
    randomPick = random.sample(range(0, len(problems)), 3)
    randomPick = [1,2,3]

    #Create a new practice file with the instructions
    practiceFile = open('practice.py', 'w')

    for i in randomPick:
        #Load the instruction from the original files
        with open(problems[i], 'r') as fileObj:
            for toktype, tok, _, _, _ in tokenize.generate_tokens(fileObj.readline):
                if toktype == tokenize.COMMENT and '#Instructions:' in tok:
                    practiceFile.writelines(tok + '\n\n')

    #Close the file
    practiceFile.close()

