n=int(input())
direc=[tuple(input().split()) for _ in range(n)]
dx,dy=[-1,0,0,1],[0,-1,1,0]
x,y=0,0
for d,c in direc:
    c=int(c)
    if d=='W':
        x+=c*dx[0]
        y+=c*dy[0]
    elif d=='S':
        x+=c*dx[1]
        y+=c*dy[1]
    elif d=='N':
        x+=c*dx[2]
        y+=c*dy[2]
    else:
        x+=c*dx[3]
        y+=c*dy[3]
print(x,y)