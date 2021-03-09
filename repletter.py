a=["abc","xyz","aba","1221","wpw"]
i=0
c=0
while i<len(a):
    if a[i][0]==a[i][-1]:
        c=c+1
    i=i+1
print(c)
    