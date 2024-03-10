n=int(input())
li=list(map(int,input().split()))
cnt=0
cur=0
while cur<n:
    temp=li[cur]
    if temp == 0:
        cnt=-1
        break
    cnt+=1
    cur+=temp
print(cnt)