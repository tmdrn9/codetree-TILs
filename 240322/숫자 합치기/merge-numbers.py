n=int(input())
li=list(map(int,input().split()))
s=0
while len(li)>1:
    a=min(li)
    li.remove(a)
    b=min(li)
    li.remove(b)
    s+=a+b
    li.append(a+b)
print(s)