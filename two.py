a=[2,4,5,6]
n=int(input("enter the number:"))
i=0
c=2
while i<len(a):
    j=i
    while j<c:
        print(a[j],end=" ")
        j=j+1
    print()
    i=i+1
    c=c+1