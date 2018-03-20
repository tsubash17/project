n=int(input("Enter the size"))
g=list(map(int,input("Enter the values").split(' ')))
for x in g:
    print(x,g.index(x))
