n=int(input())
l=list(map(int,input().split()))
b=set(l)
b=sorted(b)
if(len(b)>=3):
    print(b[-3])
else:
    print(max(b))