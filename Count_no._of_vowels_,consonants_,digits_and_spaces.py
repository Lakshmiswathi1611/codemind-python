s=input()
count_v=0
count_c=0
count_d=0
count_sp=0
n=len(s)
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count_v+=1
    elif(ord(i)>=48 and ord(i)<=57):
        count_d+=1
    elif(ord(i)==32):
        count_sp+=1
    else:
        count_c+=1
print("Vowels:",count_v)
print("Consonants:",count_c)
print("Digits:",count_d)
print("White spaces:",count_sp)
