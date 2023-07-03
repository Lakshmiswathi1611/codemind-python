n=int(input())
b=n*n
a=str(n)
c=len(a)
d=b%pow(10,c)
if n==d:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")