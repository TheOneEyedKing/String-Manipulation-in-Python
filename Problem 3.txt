#Program to check whether a string is a palindrome or not

string=input("Enter a string: ")
i=0
flag=1
n=len(string)
while(i<n//2):
    if(string[i]!=string[n-i-1]):
        flag=0
    i+=1
if flag==1:
    print("It's a palindrome.")
elif flag==0:
    print("It's not a palindrome.")
    
