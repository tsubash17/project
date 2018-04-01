a=input()
b=input()
c=[]
s=0
for i in range(0,a):
    d=input()
    c.append(d)
for i in range(0,len(c)):
    if(c[i]==b):
        s=s+1
print c
print(s)
