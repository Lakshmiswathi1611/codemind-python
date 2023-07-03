n=int(input())
l=list(map(int,input().split()))
s=[]
c=0
for i in l:
    if l.count(i)>(n//2):
        s.append(i)
j=set(s)
print(*j)