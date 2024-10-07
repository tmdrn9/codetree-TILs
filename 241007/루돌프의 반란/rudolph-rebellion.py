import heapq
from collections import deque


dxs,dys=[-1,0,1,0],[0,1,0,-1]


def dist(x1,y1,x2,y2):
    return ((x1-x2)**2)+((y1-y2)**2)

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

N, M, P, C, D=map(int,input().split())
grid=[[0]*N for _ in range(N)]
lr,lc=map(lambda x:int(x)-1,input().split())
grid[lr][lc]=-1

score=[0]*(P+1)
timing=[0]*(P+1) #기절
santa={}
for _ in range(P):
    i,r,c=map(lambda x:int(x)-1,input().split())
    santa[i+1]=(r,c)
    grid[r][c] = i+1

def lu_move():
    ## 탈락하지않은 가장 가까운 산타를 향해 1칸 돌진
    ## r큼>c큼
    global lr,lc,grid
    grid[lr][lc]=0
    q=[]
    dx,dy=0,0
    for idx in santa:
        d=dist(lr,lc,santa[idx][0],santa[idx][1])
        heapq.heappush(q,(d,-santa[idx][0],-santa[idx][1]))
    _,sr,sc=heapq.heappop(q)
    if lr<-sr:
        dx=1
    elif lr>-sr:
        dx=-1
    if lc < -sc:
        dy=1
    elif lc > -sc:
        dy=-1

    lr,lc=lr+dx,lc+dy

    #충돌
    if grid[lr][lc]!=0:
        ###산타+=C/루돌프가 이동해온 방향으로 산타 C만큼 밀림
        s_idx=grid[lr][lc]
        timing[s_idx]+=2
        score[s_idx]+=C
        bfs(s_idx,lr,lc,dx,dy,C)
    grid[lr][lc] = -1

def bfs(idx,r,c,dx,dy,k):
    nr,nc=r+(k*dx), c+(k*dy)
    if not in_range(nr,nc):
        s_remove.append(idx)
        return
    if grid[nr][nc]>0:
        n_idx=grid[nr][nc]
        grid[nr][nc] = idx
        santa[idx] = (nr, nc)
        bfs(n_idx,nr,nc,dx,dy,1)
    elif grid[nr][nc]==0:
        grid[nr][nc] = idx
        santa[idx] = (nr, nc)



def st_move(idx):
    ##case2) 산타->루돌프
    ###산타+=D/자신이 이동해온 반대방향으로 D만큼밀림
    global grid,santa
    p=[]
    r,c=santa[idx]
    mn=dist(lr,lc,r,c)
    for i,(dx,dy) in enumerate(zip(dxs,dys)):
        nr,nc=r+dx,c+dy
        td=dist(lr, lc, nr, nc)
        # 다른산타있는 칸은 못움직임
        if in_range(nr,nc) and grid[nr][nc] <= 0 and td<mn:
            heapq.heappush(p,(td,i))
    if p!=[]:

        _,dr=heapq.heappop(p)
        nr,nc=r+dxs[dr],c+dys[dr]
        grid[r][c] = 0

        if grid[nr][nc] == 0:
            santa[idx]=(nr,nc)
            grid[nr][nc]=idx
        else:
            score[idx]+=D
            timing[idx] += 2
            bfs(idx, nr, nc, -dxs[dr], -dys[dr], D)



for turn in range(1,M+1):
    for i in range(1,len(timing)):
        if timing[i]<turn:
            timing[i]+=1
    s_remove = []
    #1루돌프 움직임
    lu_move()

    #2산타 순서대로 움직임
    for idx,_ in sorted(santa.items()):

        ##기절해있거나 격자밖으로 빠져 탈락한 산타들은 제외
        ## 루돌프와 충돌한 산타는 k번째 턴이었다면, (k+1)번째 턴까지 기절하게 되어 (k+2)번째 턴부터 다시 정상상태
        if timing[idx]>turn:
            continue
        st_move(idx)
    for idx in s_remove:
        santa.pop(idx)

    ## 만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료
    if len(santa)==0:
        break
    ##매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여
    for idx in santa:
        score[idx]+=1

for p in range(1,P+1):
    print(score[p],end=' ')