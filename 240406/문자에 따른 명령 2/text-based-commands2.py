direc=list(input())
#동남서북
dx,dy=[1,0,-1,0],[0,-1,0,1]
x,y=0,0
n=3

for i in direc:
    if i =='F':
        x+=dx[n]
        y+=dy[n]
    elif i=='R':
        n=(n+1)%4
    else:
        n=(n-1)%4

print(x,y)