#Program to Count No. of letters in a word

sent=input("Enter a sentence: ")
sent=sent.lower()
count=0
for x in sent:
    if (x>='a' and x<='z'):
        count+=1
print("Number of letters: "+str(count))
