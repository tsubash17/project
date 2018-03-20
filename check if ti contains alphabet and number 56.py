a=input()
c=0
l=0
for d in a:
    if(d.isalpha()):
       c=c+1
    if(d.isdigit()):
        l=l+1
    if(c>1 and l>1):
        print "yes"
        break
else:
    print "no"
