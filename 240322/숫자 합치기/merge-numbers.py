n=int(input())
li=list(map(int,input().split()))
s=0
while len(li)>1:
    a=min(li)
    li.remove(a)
    b=min(li)
    li.remove(b)
    c=a+b
    s+=c
    li.append(c)
print(s)