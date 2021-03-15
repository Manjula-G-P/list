N = int(input())
i=0
c=[]
while i<N:
    a=input()
    b=list(a.split())
    if b[0]=="insert":
        c.insert(int(b[1]),int(b[2]))
    elif b[0]=="append":
        c.append(int(b[1]))
    elif b[0]=="remove":
        c.remove(int(b[1]))
    elif b[0]=="sort":
        c.sort()
    elif b[0]=="pop":
        c.pop()
    elif b[0]=="reverse":
        c.reverse()
    elif b[0]=="print":
        print(c)
    i=i+1
        