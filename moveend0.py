a=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]==0:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1
print(a)