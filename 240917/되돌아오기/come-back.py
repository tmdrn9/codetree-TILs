dr,dc=[0,1,0,-1],[1,0,-1,0]#동남서북
r,c=0,0
dic={'E':0,
    'S':1,
    'W':2,
    'N':3}
n=int(input())
cnt=0

def mov(d,m):
    global cnt, r, c
    for _ in range(int(m)):
        r,c=r+dr[dic[d]],c+dc[dic[d]]
        cnt+=1
        if (r,c)==(0,0):
            return True
    return False

for _ in range(n):
    d,m=input().split()
    check= mov(d,m)
    if check:
        break
if check:
    print(cnt)
else:
    print(-1)