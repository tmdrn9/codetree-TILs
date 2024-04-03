n=int(input())
li=list(map(int,input().split()))
cnt=0
map(lambda x:1 if x==0 else 0,li)
for i in range(0,n-3+1):
    temp=li[i:i+3]
    if temp[1]==0 and temp[0]==0:
        cnt+=1
        li[i:i+3]=map(lambda x:1 if x==0 else 0,temp)
    elif temp[0]==1:
        continue
    else:
        cnt+=1
        li[i:i+3]=map(lambda x:1 if x==0 else 0,temp)
if li==[1]*n:
    print(cnt)
else:
    print(-1)