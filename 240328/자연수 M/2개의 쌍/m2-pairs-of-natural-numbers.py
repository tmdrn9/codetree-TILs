n=int(input())
li=[]
for _ in range(n):
    x,y=map(int,input().split())
    li.extend([y]*x)
li=sorted(li)
MIN=0
for i in range(int(len(li)/2)):
    temp=li[i]+li[len(li)-1-i]
    if temp>MIN:
        MIN=temp

print(MIN)