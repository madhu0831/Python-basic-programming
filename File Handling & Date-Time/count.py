file=open('abc.txt')
lines=0
words=0
char=0
for line in file:
    lines+=1
    for ch in line:
        if ch.isalpha():
            char+=1
        elif ch.isspace():
            words+=1
print("lines=",lines)
print("words=",words)
print("chars=",char)
file.close()