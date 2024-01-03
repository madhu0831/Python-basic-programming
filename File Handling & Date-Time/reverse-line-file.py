file=open('abc.txt')
for s in file:
    s1=" "
    for ch in s:
        s1=ch+s1
    print(s1)