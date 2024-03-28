n=int(input())
li=[]
for _ in range(n):
    x,y=map(int,input().split())
    li.append([y,x])
li.sort()

l,r=0,n-1
answer=0

while True:
    ly,ry=li[l],li[r]
    if ly[1]==ry[1]:
        answer=max(answer,ly[0]+ry[0])
        l+=1
        r-=1
    else:
        if ly[1]<ry[1]:
            li[r][1]-=ly[1]
            answer=max(answer,ly[0]+ry[0])
            l+=1
        else:
            li[l][1]-=ry[1]
            answer=max(answer,ly[0]+ry[0])
            r-=1
    if l>=r:
        break

print(answer)