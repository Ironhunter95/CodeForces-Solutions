numofLines = int(input())
c=0
c2=0
for x in range(numofLines):
    n = input()
    newn =''.join(n.split())
    for x in newn:
        x2=int(x)
        if x2>0:
            c=c+1
    if c>1:
        c2+=1
        c=0
    else:
        c=0
print(c2)