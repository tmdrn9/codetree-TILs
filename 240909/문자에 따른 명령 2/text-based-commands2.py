direc=list(input())
#동남서북
dx,dy=[1,0,-1,0],[0,-1,0,1]
x,y=0,0
n=3

for d in direc:
    if d=='F':
        x+=dx[n]
        y+=dy[n]
    elif d=='L':
        n=(n-1)%4
    else:
        n=(n+1)%4

print(x,y)