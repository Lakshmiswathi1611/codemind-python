n=input()
m=list(n)
z=0
o=0
for i in m:
    if i=='z':
        z+=1
    else:
        o+=1
if z*2==o:
    print("Yes")
else:
    print("No")
    