#Program to Sort the words in a sentence

string=[""]
string1=input("Enter a sentence: ")
string=string1.split(" ")
string=sorted(string,key=str.lower)
for x in string:
    print(x,end=" ")

