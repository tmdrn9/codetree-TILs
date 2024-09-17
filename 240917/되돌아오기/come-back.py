dr,dc=[0,1,0,-1],[1,0,-1,0]#동남서북
r,c=0,0
dic={'E':0,
    'S':1,
    'W':2,
    'N':3}
n=int(input())
cnt=0
for _ in range(n):
    d,m=input().split()
    for _ in range(int(m)):
        r,c=r+dr[dic[d]],c+dc[dic[d]]
        cnt+=1
        if (r,c)==(0,0):
            break
    if (r,c)==(0,0):
            break

if (r,c)==(0,0):
    print(cnt)
else:
    print(-1)