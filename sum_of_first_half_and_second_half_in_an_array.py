n=int(input())
m=list(map(int,input().split()))
s1=0
s2=0
k=len(m)
for i in range(k//2):
    s1+=m[i]
for j in range(k//2,k):
    s2+=m[j]
print(s1)
print(s2)
