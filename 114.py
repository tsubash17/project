n=input()
k=input()
b=[]
c=[]
for x in range(0,n):
    d=input()
    b.append(d)
for i in b:
    if i%2!=0:
        c.append(i)
        c.sort()
print c 
print c[k-1]
