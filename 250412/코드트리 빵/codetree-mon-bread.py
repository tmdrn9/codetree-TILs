#시작 4:31
#설계끝 4:42
#코딩끝 5:14

from collections import deque
import heapq


N,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
store={}
for i in range(1,M+1):
    store[i]=tuple(map(lambda x:int(x)-1,input().split()))
path={}
people={}
no=[]
def bfs(i, ir,ic):
    ## 최단 거리로 움직이고 상좌우하 순
    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]
    visited=[[0]*N for _ in range(N)]
    visited[ir][ic]=1
    q=deque([(ir,ic)])
    sr,sc=store[i]
    find=False
    while q:
        r,c=q.popleft()
        for dx,dy in zip(dxs,dys):
            nr,nc=r+dx,c+dy
            if 0<=nr<N and 0<=nc<N and grid[nr][nc]!=-1 and not visited[nr][nc]:
                visited[nr][nc]=(r,c)
                q.append((nr,nc))
                if (sr,sc)==(nr,nc):
                    find=True
                    break
        if find:
            break

    r,c=sr,sc
    path=[(sr,sc)]
    while visited[r][c]!=1:
        nr,nc=visited[r][c]
        path.append((nr,nc))
        r,c=nr,nc
    path=path[:-1]
    return path[-1]

def find_camp(p_i):
    ## 최단 거리로 움직이고 상좌우하 순
    # 행이 작은>열이 작은
    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]
    hq=[]
    for i in range(N):
        for j in range(N):
            if grid[i][j]==1:
                visited = [[0] * N for _ in range(N)]
                sr, sc = store[p_i]
                visited[sr][sc] = 1
                q = deque([(sr, sc)])
                while q:
                    r,c=q.popleft()
                    for dx,dy in zip(dxs,dys):
                        nr,nc=r+dx,c+dy
                        if 0<=nr<N and 0<=nc<N and grid[nr][nc]!=-1 and not visited[nr][nc]:
                            visited[nr][nc]=visited[r][c]+1
                            q.append((nr,nc))
                            if (i,j)==(nr,nc):
                                break
                heapq.heappush(hq,(visited[i][j],i,j))
    _,i,j=heapq.heappop(hq)
    return i,j


time=0
while True:
    time+=1
    bye=[]
    #1 격자안에 있는 사람 모두가 편의점 방향을 향해 1칸이동
    for i in people:
        r,c=people[i]
        nr,nc=bfs(i, r, c)
        people[i]=(nr,nc)
        if people[i]==store[i]:
            bye.append(i)

    #2 편의점 도착한다면 멈추고 해당 칸은 이제 지나갈 수 없음(단 모두 이동 후 지나갈 수 없게 되는 것)
    for i in bye:
        r,c=people.pop(i)
        grid[r][c]=-1
    if time>M and not people:
        break
    #3 현재시간 t이고 t<=m을 만족한다면,t번 사람은 최단거리가 가장 짧은 베이스 캠프에 들어감
    ## 이때부터 다른 사람들은 베이스 캠프가 있는 칸 지나갈 수 없음(단 모두 이동 후 지나갈 수 없게 되는 것)
    if time<=M:
        i,j=find_camp(time)
        people[time]=(i,j)
        grid[i][j]=-1


print(f'{time}')