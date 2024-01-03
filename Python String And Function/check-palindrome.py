s=input("enter a string")
flag=0
for i in range (0,int(len(s)/2)):
    if s[i]==s[len(s)-i-1]:
        flag=1
if flag==1:
    print("string is palindrome")
else:
    print("string is not palindrome")
