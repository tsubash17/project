n=input()

prime=1

i=2

while(i<n):

	if(n%i==0):

		prime=0

	i=i+1

if(prime==1):

	print("It is a prime number")
else:
	
        print("it is not a prime number")
