a=input()
b=0
while(a>0):
    r=a%10
    b=b+r
    a=a//10
print("sum of all digits is",b)
