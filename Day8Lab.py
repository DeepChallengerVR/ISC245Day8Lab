# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#myName = input("type your name: ")
#firstLetter = myName[0]
#firstTwoLetters = myName[0:2]
#lastLetter = myName[-1:]
#roundedMiddleP = round((len(myName))/2)
#
#print("hello " + myName + " it is nice to meet you!")
#print(firstLetter)
#print(firstTwoLetters)
#print(myName[roundedMiddleP])


def pigLatiner(word):
    word = word.lower()
    fLetter = word[0]
    remainder = word[1:]
    newWord = remainder + fLetter + "ay"
    return newWord

name = input("type your name: ")
print("hello, " + name + ", it is nice to meet you.")
newWord = pigLatiner(name)
word = input(newWord + " please type some words to convert into Pig Latin: ")
wordList = word.split()

output = ""
for element in wordList:
   #newWord = pigLatiner(element) + "" 
    pigWord = pigLatiner(element)
    output = output + pigWord + " "

print("Translation of '" + word + "' into Pig Latin: " + output)


