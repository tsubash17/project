a=input()
b=input()
if(a>b):
    num=a
else:
    num=b
while(1):
    if(num%a==0 and num%b==0):
        print("LCM is:",num)
        break
    num=num+1
