#위오아왼
dx=[0,1,0,-1]
dy=[1,0,-1,0]
x,y=0,0

n=int(input())
for _ in range(n):
    d,v=input().split()
    v=int(v)
    if d=='N':
        x+=v*dx[0]
        y+=v*dy[0]
    elif d=='E':
        x+=v*dx[1]
        y+=v*dy[1]
    elif d=='S':
        x+=v*dx[2]
        y+=v*dy[2]
    else:
        x+=v*dx[3]
        y+=v*dy[3]
print(x, y)