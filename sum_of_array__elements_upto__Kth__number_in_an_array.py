n=int(input())
m=list(map(int,input().split()))
s=int(input())
c=0
for i in m:
    if i==s:
        break
    else:
      c+=i
print(c+s)