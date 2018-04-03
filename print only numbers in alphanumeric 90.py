a=input()
b=[]
for i in range(0,len(a)):
   if(a[i].isdigit()):
       b.append(a[i])
d="".join(b)
print(d)
