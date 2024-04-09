import heapq,math
from collections import deque
DX,DY=[-1,0,0,1],[0,-1,1,0]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

N,M=map(int,input().split())
stop=[0]*(M+1)
stop[0]=1
m=[[-1,-1] for _ in range(M+1)]
arrive=[[-1,-1] for _ in range(M+1)]
grid=[list(map(int,input().split())) for _ in range(N)]

base=[(i//N,i%N) for i,p in enumerate(sum(grid,[])) if p==1]

for i in range(1,M+1):
    arrive[i]=list(map(lambda x:int(x)-1,input().split()))
t=1
while True:
    # 1 모두가 한칸씩 움직임 상좌우하 [-1,0,0,1],[0,-1,1,0]
    for i in range(1,min(t,M+1)):
        if stop[i]==1:
            continue
        x,y=m[i]
        ax,ay=arrive[i]
        for dx,dy in zip(DX,DY):
            nx,ny=x+dx,y+dy
            if not in_range(nx,ny) and grid[nx][ny]!=0 or (abs(nx-ax)>abs(x-ax) or abs(ny-ay)>abs(y-ay)):
                continue
            else:
                m[i]=[nx,ny]
                # grid[nx][ny]=i
                if t==i+1:
                    grid[x][y]=-1
                # else:
                #     grid[x][y] =0
                break
    # 2 도착하면 해당 편의점이 있는칸을 지나갈수 없게됨 -1로 표시하기
    for i in range(1,min(t,M+1)):
        if stop[i]==1:
            continue
        if m[i]==arrive[i] and grid[m[i][0]][m[i][1]]==0:
            grid[m[i][0]][m[i][1]]=-1
            stop[i]=1

    #3 만약 t<=m이면 t번 사람이 자기가 갈 편의점과 가장 가까이 있는 베캠으로 이동
    if t<M+1:
        ax, ay = arrive[t]
        pq=[]
        for camp in base: #abs(nx-ax)>abs(x-ax)
            heapq.heappush(pq,(abs(camp[0]-ax)+abs(camp[1]-ay),camp[1],camp[0]))
        _,ty,tx=heapq.heappop(pq)
        m[t]=[tx,ty]
        # grid[tx][ty]=t
        base.remove((tx,ty))
    #다 도착했는지 확인
    if t<M+1:
        t+=1
    else:
        if len(set(stop))!=1:
            t+=1
        else:
            break
print(t)