a=[2,9,5,3,7,1,4]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1
print(a)



