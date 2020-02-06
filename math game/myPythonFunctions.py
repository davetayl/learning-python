# myPythonFunctions.py
from random import randint
from os import remove, rename

def getUserPoint(userName):
    f = open('userScores.txt', 'r')
    for l in f:
        content = l.split(', ')
        if content[0] == userName:
            return content[1]
    return -1