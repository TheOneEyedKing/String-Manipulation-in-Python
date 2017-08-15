#Program to remove punctuations in a sentence

import string

strin=input("Enter a sentence: ")
string1=''
for x in strin:
    if x not in string.punctuation:
        string1+=x
print(string1)
