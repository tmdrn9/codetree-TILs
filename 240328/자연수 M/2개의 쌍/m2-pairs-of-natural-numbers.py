n=int(input())
li=[]
total=0
for _ in range(n):
    x,y=map(int,input().split())
    li.extend([y]*x)
    total+=x
li=sorted(li)
MIN=0
for i in range(int(total/2)):
    temp=li[i]+li[total-1-i]
    if temp>MIN:
        MIN=temp

print(MIN)