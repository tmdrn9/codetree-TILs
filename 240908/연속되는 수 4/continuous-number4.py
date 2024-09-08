n=int(input())
pre=int(input())
ans,cnt=1,1

for _ in range(n-1):
    now=int(input())
    if now>pre:
        cnt+=1
    else:
        if ans<cnt:
            ans=cnt
        cnt=1
    pre=now
if ans<cnt:
    ans=cnt
print(ans)