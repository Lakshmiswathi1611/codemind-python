n=int(input())
for i in range(n):
    for j in range(n):
        s=i+j
        if s<=n-1:
            print(j+1,end='')
        else:
            print('',end='')
    print()
