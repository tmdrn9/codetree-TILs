n=int(input())
li=list(map(int,input().split()))
cnt=0
ok=False
def change(temp):
    return map(lambda x:1 if x==0 else 0,temp)

# for _ in range(2):
for i in range(1,n):
    if i==n-1:
        temp=li[i-1:i+1]
        if temp[0]==0 and temp[1]==0:
            cnt+=1
            li[i-1:i+1]=change(temp)
    else:
        temp=li[i-1:i+2]
        if i-1==0 and temp[0]==0:
            cnt+=1
            li[i-1:i+2]=change(temp)
        else:
            if temp[0]==0:
                cnt+=1
                li[i-1:i+2]=change(temp)
            elif temp[0]==1:
                continue
            else:
                cnt+=1
                li[i-1:i+2]=change(temp)
    if li==[1]*n:
        ok=True
        break

if ok:
    print(cnt)
else:
    print(-1)