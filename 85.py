a=raw_input()
b=[]
c=[]
for i in range(0,len(a)):
    if(i%2!=0):
        b.append(a[i])
    else:
        c.append(a[i])
print ("".join(c))
print ("".join(b))
