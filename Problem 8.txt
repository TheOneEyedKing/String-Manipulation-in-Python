#Program to access the strings literals
#first character
#last character
#slicing 2nd to 5th character
#slicing 6th to 2nd last character

string=input("Enter a string: ")
a=string[0]
print("First character="+a)
b=string[len(string)-1]
print("Last character="+b)
c=string[1:5]
print("2nd to 5th characters = "+c)
d=string[-6:-1]
print("6th to 2nd last characters = "+d)
