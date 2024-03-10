n=int(input())
li=list(map(int,input().split()))
cnt=0
cur=1
while cur<=n-1:
    # print(cur)
    tempmax=li[cur]
    cnt+=1
    if cur+tempmax>=n-1:
        break
    elif tempmax==1:
        cur+=1
        continue
    elif tempmax == 0:
        cnt=-1
        break
    else:
        l=li[cur+1:cur+tempmax+2]
        cur+=(l.index(max(l))+1)
print(cnt)