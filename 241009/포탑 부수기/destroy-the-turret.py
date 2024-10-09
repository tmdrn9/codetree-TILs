import heapq
from collections import deque

#입력
N, M, K=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]

#공격한 턴을 적는 자료
attack_t=[[0]*M for _ in range(N)]

def attacker():
    global grid
    q=[]
    for i in range(N):
        for j in range(M):
            if grid[i][j]!=0:
                # 가장 약한 포탑>가장 최근에 공격한 포탑>r+c 큼>c큼
                heapq.heappush(q,(grid[i][j],-attack_t[i][j],-(i+j),-j))
    _,_,hap,c=heapq.heappop(q)
    ar,ac=-hap+c,-c
    # 공격자는 공격력 +N+M
    grid[ar][ac]+=(N+M)
    return ar,ac

def noattacker(attacker):
    global grid
    q = []
    for i in range(N):
        for j in range(M):
            # 자신제외하고 가장 강한 포탑 공격
            ##공격력 높음>공격한지 가장 오래된 포탑>r+c작음>c작음
            if grid[i][j] != 0 and attacker!=(i,j):
                heapq.heappush(q, (-grid[i][j], attack_t[i][j], (i + j), j))
    _, _, hap, c = heapq.heappop(q)
    return hap-c, c

def boom(nr,nc,ar,ac):
    dx,dy=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
    path=[(ar,ac),(nr,nc)]
    ##공격 대상은 공격자의 공격력만큼 피해
    attack_point=grid[ar][ac]
    grid[nr][nc]=grid[nr][nc]-attack_point if grid[nr][nc]>attack_point else 0
    if grid[nr][nc]<0:
        grid[nr][nc]=0


    for ddx,ddy in zip(dx,dy):
        # 가장자리에서 막힌 방향으로 피해
        tr,tc=(nr+ddx)%N,(nc+ddy)%M
        if (tr,tc)==(ar,ac): #공격자는 피해없음
            continue
        if grid[tr][tc]!=0:
            # 주위 8개의 방향에 있는 포탑 공격력//2 만큼 피해
            path.append((tr,tc))
            grid[tr][tc]= grid[tr][tc]-attack_point if attack_point<grid[tr][tc] else 0
    return path
def laser(nr,nc,ar,ac):
    # 우/하/좌/상
    dxs, dys = [0,1,0,-1], [1, 0, -1, 0]
    visited = [[0] * M for _ in range(N)]
    before = [[0] * M for _ in range(N)]
    attack_point=grid[ar][ac]
    path=[(nr,nc),(ar,ac)]

    q=deque([])
    q.append((ar,ac))
    visited[ar][ac]=1


    while q:
        r,c=q.popleft()
        for dx,dy in zip(dxs,dys):
            # 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나옴
            tr,tc=(r+dx)%N,(c+dy)%M
            # 부서진 포탑이 있는 위치는 지날 수 없음
            if not visited[tr][tc] and grid[tr][tc]!=0:
                q.append((tr,tc))
                visited[tr][tc]=1
                before[tr][tc]=(r,c)
                if (tr, tc) == (nr, nc):
                    break

    if visited[nr][nc]==0:
        return None
    else:
        grid[nr][nc]=grid[nr][nc]-attack_point if grid[nr][nc]>attack_point else 0
        x,y=nr,nc
        while True:
            X,Y=before[x][y]
            if (X,Y)==(ar,ac):
                break
            grid[X][Y]=grid[X][Y] - attack_point//2 if grid[X][Y] > (attack_point//2) else 0
            path.append((X,Y))
            x,y=X,Y
        return path




    ##경로의 길이가 똑같은 최단 경로가 2개 이상이라면, 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택
    ##공격 대상은 공격자의 공격력만큼 피해입고
    ##경로에 있는 포탑은 공격자의 공격력//2 만큼 피해


#main
for turn in range(1,K+1):

    #[1] 공격자 선정
    ar,ac=attacker()
    attack_t[ar][ac]=turn


    #[2] 공격 대상자 선정
    nr,nc=noattacker(attacker)

    #[3] 레이저공격 시도 후 안되면 포탄공격
    #[3-1] 레이저 공격: 최단경로로 이동
    path=laser(nr, nc, ar, ac)

    #[3-2]포탄 공격
    if path==None:
        path=boom(nr,nc,ar,ac)

    #[4]
    ##부서지지 않은 포탑 중 공격과 무관했던 포탑은 공격력 +1
    for i in range(N):
        for j in range(M):
            if grid[i][j]!=0 and (i,j) not in path:
                grid[i][j]+=1


    #부서지지 않은 포탑이 1개가 된다면 그 즉시 중지
    cnt = 0
    for row in grid:
        cnt += row.count(0)
    if cnt==(N*M)-1:
        break

ans=-1
for row in grid:
    ans=max(ans,max(row))
print(ans)