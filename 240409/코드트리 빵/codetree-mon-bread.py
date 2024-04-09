import heapq,math
from collections import deque
DX,DY=[-1,0,0,1],[0,-1,1,0]

def in_range(x,y):
    return 0<=x<N and 0<=y<N
def bfs(x,y):
    global grid
    cp_grid=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cp_grid[i][j]=grid[i][j]
    q=deque([[x,y]])
    cp_grid[x][y]=-1
    while q:
        x,y=q.popleft()
        for dx, dy in zip(DX, DY):
            nx,ny=x+dx,y+dy
            if in_range(nx,ny) and cp_grid[nx][ny]!=-1:
                if cp_grid[nx][ny]==1:
                    return (nx,ny)
                cp_grid[nx][ny]=-1
                q.append([nx,ny])


N,M=map(int,input().split())
stop=[0]*(M+1)
stop[0]=1
m=[[-1,-1] for _ in range(M+1)]
arrive=[[-1,-1] for _ in range(M+1)]
grid=[list(map(int,input().split())) for _ in range(N)]

base=[(i//N,i%N) for i,p in enumerate(sum(grid,[])) if p==1]

for i in range(1,M+1):
    arrive[i]=list(map(lambda x:int(x)-1,input().split()))
t=0
while len(set(stop))!=1:
    t += 1
    del_=[]
    # 1 모두가 한칸씩 움직임 상좌우하 [-1,0,0,1],[0,-1,1,0]
    for i in range(1,min(t,M+1)):
        if stop[i]==1:
            continue
        x,y=m[i]
        ax,ay=arrive[i]
        result=[]
        mm=math.inf
        for dx,dy in zip(DX,DY):
            nx,ny=x+dx,y+dy
            if not in_range(nx,ny) or grid[nx][ny]==-1:
                continue
            dist=abs(nx-ax)+abs(ny-ay)
            if dist==0:
                fx, fy = nx, ny
                break
            if mm>dist:
                mm=dist
                fx,fy=nx,ny
        m[i]=[fx,fy]
        # grid[nx][ny]=i

        # 2 도착하면 해당 편의점이 있는칸을 지나갈수 없게됨 -1로 표시하기
        if m[i]==arrive[i]:
            stop[i]=1
            del_.append(m[i])

    while del_:
        rr,rc=del_.pop(-1)
        grid[rr][rc]=-1

    #3 만약 t<=m이면 t번 사람이 자기가 갈 편의점과 가장 가까이 있는 베캠으로 이동
    if t<M+1:
        ax, ay = arrive[t]
        tx,ty=bfs(ax, ay)
        # pq=[]
        # for camp in base: #abs(nx-ax)>abs(x-ax)
        #     heapq.heappush(pq,(abs(camp[0]-ax)+abs(camp[1]-ay),camp[0],camp[1]))
        # _,tx,ty=heapq.heappop(pq)
        m[t]=[tx,ty]
        grid[tx][ty]=-1
        # base.remove((tx,ty))

print(t)