a=input()
x=list(str(a))
for c in range(0,len(x)):
    if(((int(x[c]))%2)!=0):
        print(x[c])
