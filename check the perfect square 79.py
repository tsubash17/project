x=input()
y=input()
z=x*y
for i in range(1,z):
    if i*i==z:
        print "yes"
        break        
else:
    print "no"
