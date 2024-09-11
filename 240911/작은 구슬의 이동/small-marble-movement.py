dx,dy=[0, 1, -1, 0], [1, 0, 0, -1]
di = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

n,t = map(int,input().split())

def in_range(x,y):
    return 1<=x and x<n+1 and 1<=y and y<n+1

r, c, d=input().split()
d=di[d]
r=int(r)
c=int(c)

for _ in range(t):
    tr,tc=r+dx[d],c+dy[d]
    if in_range(tr,tc):
        r,c=tr,tc
    else:
        d=3-d
print(r,c)