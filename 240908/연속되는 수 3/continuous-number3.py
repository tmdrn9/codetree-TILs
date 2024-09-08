n=int(input())
cnt=1
ans=1
temp=input()
for i in range(n-1):
    now=input()
    if ('-' in temp and '-' in now) or ('-' not in temp and '-' not in now):
        cnt+=1
    else:
        if ans<cnt:
            ans=cnt
        cnt=1
    temp=now
if ans<cnt:
    ans=cnt

print(ans)