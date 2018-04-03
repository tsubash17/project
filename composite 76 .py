x=input()
if x>1:
    for i in range(2,x):
        if(x%i==0):
           print (x,"it's composite num")
           break
        else:
           print ("prime num",x)
           break
