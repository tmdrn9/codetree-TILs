dx,dy=[0, 1, -1, 0], [1, 0, 0, -1]
di = {}  # dict 초기화
di['R'] = 0
di['D'] = 1
di['U'] = 3
di['L'] = 2

n,t = map(int,input().split())

def in_range(x,y):
    return 1<=x and x<n+1 and 1<=y and y<n+1

r, c, d=input().split()
d=di[d]
r=int(r)
c=int(c)

for _ in range(t):
    tx,ty=r+dy[d],c+dx[d]
    if in_range(tx,ty):
        r,c=tx,ty
    else:
        d=3-d
print(r,c)