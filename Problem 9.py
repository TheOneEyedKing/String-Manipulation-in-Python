"""Program to find the first appearance of the substring not and poor from a given string, if
bad follows the poor, replace the whole not...poor substring with good. Return the resulting string.
Sample String : The lyrics is not that poor!
Expected Result : The lyrics is good!
"""

#There seems to be a conflict in question and the given example.
#since 'poor' isn't followed by 'bad' ,but still replacement is taking place.
#So I am following the question.

string=input("Enter a sentence: ")
string=string.split(" ")
string1=''
flag=1
bad=string.index('bad')
print(bad)
poor=string.index('poor')
not1=string.index('not')
count=0
if(bad==poor+1):
    for x in string:
        if(count>=not1 and count<=poor and flag==1):
            string1+="good "
            flag=0
        elif(not(count>=not1 and count<=poor)):
            string1+=x+" "

        
        count+=1
print(string1)
