n=int(input())
li=list(map(int,input().split()))
cnt=0
cur=0
while cur<=n-1:
    temp=li[cur]
    if temp ==0:
        break
    cnt+=1
    cur+=temp
print(cnt)