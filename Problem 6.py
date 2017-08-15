#Program to count the no. of each vowels

a=0;e=0;i=0;o=0;u=0
string=input("Enter a sentence: ")
for x in string:
    if x=='a' or x=='A':
        a+=1
    elif x=='e' or x=='E':
        e+=1
    elif x=='i' or x=='I':
        i+=1
    elif x=='o' or x=='O':
        o+=1
    elif x=='u' or x=='U':
        u+=1
print("a or A="+str(a)+"\n"+
      "e or E="+str(e)+"\n"+
      "i or I="+str(i)+"\n"+
      "o or O="+str(o)+"\n"+
      "u or U="+str(u)+"\n")
