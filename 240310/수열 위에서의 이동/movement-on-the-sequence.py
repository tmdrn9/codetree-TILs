n=int(input())
li=list(map(int,input().split()))
cnt=0
cur=0
while cur<=n-1:
    temp=li[cur]
    cnt+=1
    if temp == 0:
        cnt=-1
        break
    cur+=temp
print(cnt)