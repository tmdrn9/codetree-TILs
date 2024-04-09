import heapq,math
from collections import deque
DX,DY=[-1,0,0,1],[0,-1,1,0]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def bfs(start_pos):
    # visited, step 값을 전부 초기화합니다.
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
            step[i][j] = 255
    
    # 초기 위치를 넣어줍니다.
    q = deque()
    q.append(start_pos)
    sx, sy = start_pos
    visited[sx][sy] = True
    step[sx][sy] = 0

    # BFS를 진행합니다.
    while q:
        # 가장 앞에 원소를 골라줍니다.
        x, y = q.popleft()

        # 인접한 칸을 보며 아직 방문하지 않은 칸을 큐에 넣어줍니다.
        for dx, dy in zip(DX,DY):
            nx, ny = x + dx, y + dy
            # 갈 수 있는 경우에만 진행합니다.
            if in_range(nx,ny) and visited[nx][ny]==False and grid[nx][ny]!=-1:
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))

N,M=map(int,input().split())
stop=[0]*(M+1)
stop[0]=1
m=[[-1,-1] for _ in range(M+1)]
arrive=[[-1,-1] for _ in range(M+1)]
grid=[list(map(int,input().split())) for _ in range(N)]

for i in range(1,M+1):
    arrive[i]=list(map(lambda x:int(x)-1,input().split()))
t=0
while len(set(stop))!=1:
    step = [[255] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    # print(stop)
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
        bfs((ax,ay))
        for dx,dy in zip(DX,DY):
            nx,ny=x+dx,y+dy
            if not in_range(nx,ny) or grid[nx][ny]==-1:
                continue
            if mm>step[nx][ny]:
                mm=step[nx][ny]
                fx, fy = nx, ny
        m[i]=[fx,fy]

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
        bfs((ax, ay))
        min_dist = math.inf
        min_x, min_y = -1, -1
        for i in range(N):
            for j in range(N):
                if visited[i][j] and grid[i][j] == 1 and min_dist > step[i][j]:
                    min_dist = step[i][j]
                    min_x, min_y = i, j
        m[t]=[min_x,min_y]
        grid[min_x][min_y]=-1

print(t)