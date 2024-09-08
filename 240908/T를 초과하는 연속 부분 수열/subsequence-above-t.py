n,t=map(int,input().split())
cnt,ans=0,0
li=list(map(int,input().split()))
for i in range(n):
    if li[i]>t:
        cnt+=1
    else:
        if ans<cnt:
            ans=cnt
        cnt=0

if ans<cnt:
    ans=cnt
print(ans)