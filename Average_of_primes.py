def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
            if (n%i==0):
                return False
    else:
        return True
n=int(input())
m=list(map(int,input().split()))
c=0
s=0
for i in m:
    if isprime(i):
        c+=i
        s+=1
c=c/s
print("%.2f"%c)