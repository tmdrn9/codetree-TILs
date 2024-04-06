n=int(input())
grid=[list(map(int,input().split())) for _ in range(n)]
#동남서북
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
    
dx,dy=[1,0,-1,0],[0,1,0,-1]
answer=0
for i in range(n):
    for j in range(n):
        cnt=0
        for dxx,dyy in zip(dx,dy):
            x=i+dxx
            y=j+dyy
            if in_range(x,y) and grid[x][y]==1:
                cnt+=1
        if cnt>=3:
            answer+=1
print(answer)