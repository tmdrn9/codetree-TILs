n=int(input())
cnt=1
temp=int(input())
for i in range(n-1):
    now=int(input())
    if now!=temp:
        cnt+=1
    temp=now
print(cnt)