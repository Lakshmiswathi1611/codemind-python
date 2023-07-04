s=input()
a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 "
c=0
for i in s:
    if i not in a:
        c+=1
print(c)