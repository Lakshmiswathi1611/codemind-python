n=int(input())
for i in range(n):
    for j in range(n):
        s=i+j
        if i==j or s==n-1:
            print('x',end='')
        else:
            print('0',end='')
    print()