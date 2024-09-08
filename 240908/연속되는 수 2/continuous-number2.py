n=int(input())
temp=int(input())
ans=-1
cnt=1
for i in range(n-1):
    now=int(input())
    if now==temp:
        cnt+=1
    else:
        if ans<cnt:
            ans=cnt
        cnt=1
    temp=now
print(ans)