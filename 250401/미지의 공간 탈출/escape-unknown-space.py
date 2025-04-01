import sys
from collections import deque
# sys.stdin = open("./input.txt")
# input = sys.stdin.readline
dxs,dys=[0,0,1,-1],[1,-1,0,0] #동서남북

n,m,f=map(int,input().split()) #공간한변길이, 시간의벽한변길이, 이상현상 개수
grid=[list(map(int,input().split())) for _ in range(n)]
startx,starty=None,None
mountain=[[-1]*(m*4) for _ in range(2*m)]
for i in range(5):
    if i==0: #동
        for j in range(m):
            mountain[m+j][2*m:3*m]=list(map(int,input().split()))
    elif i==1: #서
        for j in range(m):
            mountain[m+j][:m]=list(map(int,input().split()))

    elif i==2: #남
        for j in range(m):
            mountain[m+j][m:2*m]=list(map(int,input().split()))
    elif i==3: #북
        for j in range(m):
            mountain[m+j][3*m:]=list(map(int,input().split()))
    else:
        for j in range(m):
            mountain[j][m:2*m]=list(map(int,input().split()))
            if 2 in mountain[j][m:2*m]:
                startx,starty=j,m+mountain[j][m:2*m].index(2)
fire=[]
for i in range(f):
    fire.append(list(map(int,input().split())))
    grid[fire[i][0]][fire[i][1]]=-1
# fire=[list(map(int,input().split())) for _ in range(f)] #초기위치 r,c ,확산방향 d, 확산상수 v
day=0
endx,endy,mountain_x,mountain_y=None,None,None,None
for i in range(n):
    for j in range(n):
        if grid[i][j]==4:
            endx,endy=i,j
        elif grid[i][j]==3 and mountain_y==None:
            mountain_x,mountain_y=i,j

ingridx,ingridy=2*m-1,None
for i in range(m+2):
    if 0 in grid[mountain_x-1+i][mountain_y-1:mountain_y+m+1]:
        temp=grid[mountain_x-1+i][mountain_y-1:mountain_y+m+1].index(0)
        outMountainx,outMountainy=mountain_x-1+i,mountain_y-1+temp
        if temp==0: #1
            ingridy=i-1
        elif temp==m+1: #0
            ingridy=2*m+(m-i)
        elif 0<temp<m+2 and i==0: #3
            ingridy=3*m+(m-temp)
        else: #2
            ingridy=m+temp
        break

def bfs(mountainis,startx,starty,endx,endy):
    if mountainis:
        visited=[[0]*(m*4) for _ in range(2*m)]
        pq=deque([(startx,starty)])
        visited[startx][starty]=1
        while pq:
            x,y=pq.popleft()
            if (x,y)==(endx,endy):
                return visited[x][y],visited
            for dx,dy in zip(dxs,dys):
                nx,ny=x+dx,y+dy
                if 0<=x<m:
                    if nx<0:
                        nx,ny=m,3*n+ny-n
                    elif ny<m:
                        ny=nx
                        nx=m
                    elif ny>=2*m:
                        ny=2*m+(m-nx-1)
                        nx=m
                else:
                    if ny>=4*m:
                        ny=0
                    elif ny<0:
                        ny=(4*m)-1

                    if nx<m:
                        if ny<m:
                            nx=ny
                            ny=m
                        elif 2*m<=ny<3*m:
                            nx=m-1-(2*m-ny)
                            ny=2*m-1
                        elif ny>=3*m:
                            nx=0
                            ny=m+(m-1-(3*m-ny))

                if 0<=nx<(2*m) and 0<=ny<(m*4) and mountain[nx][ny]==0 and visited[nx][ny]==0:
                    pq.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
        return -1,None
    else:
        visited=[[0]*n for _ in range(n)]
        pq=deque([(startx,starty)])
        visited[startx][starty]=1
        while pq:
            x,y=pq.popleft()
            if (x,y)==(endx,endy):
                return visited[x][y],visited
            for dx,dy in zip(dxs,dys):
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and (grid[nx][ny]==0 or grid[nx][ny]==4) and visited[nx][ny]==0:
                    pq.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
        return -1,None

def move_fire(day):
    check=False
    for i,(r,c,d,v) in enumerate(fire):
        if day>0 and day%v==0:
            nx,ny=r+dxs[d],c+dys[d]
            if 0<=nx<n and 0<=ny<n and (nx,ny)!=(endx,endy) and grid[nx][ny]!=1:
                grid[nx][ny]=-1
                fire[i]=[nx,ny,d,v]
            if (nx,ny)==(outMountainx,outMountainy):
                check=True
    return check



############################################################################
result=0
days=0
if ingridy==None:
    print(-1)
else:
    t1,_=bfs(True,startx,starty,ingridx,ingridy)
    if t1==-1:
        print(-1)
    else:
        for d in range(t1):
            if move_fire(d):
                print(-1)

    move_fire(t1)
    days=t1
    # print(days)
    loop=True
    while loop:
        t2,visitedd=bfs(False,outMountainx,outMountainy,endx,endy)
        # print(t2)
        if t2==-1:
            loop=False
        else:
            out=False
            for d in range(t2):
                move_fire(days+1+d)
                for x,y,_,_ in fire:
                    if visitedd[x][y]!=0:
                        grid[x][y]
                        out=True
                if out==True:
                    break
        if out:
            continue
        loop=False
    if t2==-1:
        print(-1)
    else:
        print(days+t2-1)