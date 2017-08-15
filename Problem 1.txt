#Program to Concatenate Two or More Strings

n=input("Enter the number of strings you want to concatenate: ")
n=int(n)
count=1
strcat=''
while count<=n:
    str1=input()
    strcat+=str1
    count+=1

print(strcat)
