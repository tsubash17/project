num=0
n=input()
sum=n
while n>0:
   r=n%10
   sum=sum+(r**3)
   n=n/10
if sum==num:
	print("yes")
else:
	print(" no")
