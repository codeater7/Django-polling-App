
l = input().split()

ans=sum(-int(i) if int(i)&1 else int(i) for i in l)
print((ans))




l =[int(i) for i in input().split()]

s=0
for i in l:
    if i%2==0:
        s+=i
    else:
        s-=i


print(s)
