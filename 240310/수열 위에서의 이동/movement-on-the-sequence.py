n=int(input())
li=list(map(int,input().split()))
cnt=0
cur=0
while cur<=n-1:
    # print(cur)
    tempmax=li[cur]
    # print(tempmax)
    if cur+tempmax>n-1:
        cnt+=1
        break
    if tempmax==1:
        cnt+=1
        cur+=1
        continue
    elif tempmax == 0:
        cnt=-1
        break
    else:
        cnt+=1
        l=li[cur+1:cur+tempmax+1]
        cur+=(l.index(max(l))+1)
print(cnt)