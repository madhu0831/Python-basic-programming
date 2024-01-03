def unique(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique([1,2,1,3,4,5,3,4]))
