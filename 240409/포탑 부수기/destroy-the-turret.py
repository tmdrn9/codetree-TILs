import heapq,math
from collections import deque
DX, DY = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(start,end):
    pq=[]
    path= [-1] * (N * M)
    dist = [math.inf] * (N * M)
    heapq.heappush(pq,(0,start))
    dist[start]=0
    while pq:
        min_dist,min_index=heapq.heappop(pq)
        if min_dist!=dist[min_index]:
            continue
        for sn in graph[min_index]:
            new_dist=min_dist+1
            if new_dist<dist[sn]:
                dist[sn]=new_dist
                if path[min_index]==-1:
                    path[min_index]=sn
                heapq.heappush(pq, (new_dist, sn))
    if end in path:
        x = start
        v = [x]
        while x != end:
            x =path[x]
            v.append(x)
        return v[1:-1]
    else:
        return -1

N, M, K = map(int, input().split())
plus=N+M
grid = [list(map(int, input().split())) for _ in range(N)]
li = []  # 공격순서넣는 list
for turn in range(1,K+1):
    temp=[i for i in sum(grid, []) if i>0]
    if len(temp)==1:
        break
    contain=[]
    graph = [[] for _ in range(N * M)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] <= 0:
                continue
            node = N * i + j
            back=[]
            for ddx, ddy in zip(DX, DY):
                ni, nj = (i + ddx) , (j + ddy)
                #ni, nj = (i + ddx) % N, (j + ddy) % M
                if 0<=ni<N and 0<=nj<M:
                    if grid[ni][nj] != 0:
                        new_node = N * ni + nj
                        graph[node].append(new_node)
                else:
                    ni, nj = ni % N, nj % M
                    new_node = N * ni + nj
                    if grid[ni][nj] != 0:
                        back.append(new_node)
            graph[node].extend(back)
    # 1가장 약한 포탑 선정
    # 가장 최근에 공격한 포탑>행열합이 가장 큰 포탑>열값이 가장 큰 포탑
    weak = []
    for i in range(N):
        for j in range(M):
            if grid[i][j]<=0:
                continue
            heapq.heappush(weak,(grid[i][j],li[::-1].index(N*i+j) if N*i+j in li else math.inf ,-(i+j),-j,-i))
    _,_,_,attack_c,attack_r=heapq.heappop(weak)
    del weak
    attack_c,attack_r=-attack_c,-attack_r
    attark_n=N*attack_r+attack_c
    li.append(attark_n)
    contain.extend([attark_n])
    # n+m만큼의 공격력   증가
    grid[attack_r][attack_c]+=plus
    damage=grid[attack_r][attack_c]
    half_damage=damage//2
    # 2공격자 공격
    # 가장 강한 포탑 선정
    ## 공격한지 가장 오래된 포탑>행열합이 가장 작은 포탑>열값이 가장 작은 포탑
    strong = []
    for i in range(N):
        for j in range(M):
            if grid[i][j]<=0 or (i==attack_r and j==attack_c):
                continue
            heapq.heappush(strong, (-grid[i][j], li.index(N*i+j) if N*i+j in li else -math.inf, (i + j), j, i))
    _, _, _, loser_c, loser_r = heapq.heappop(strong)
    del strong
    loser_n = N * loser_r + loser_c
    contain.extend([loser_n])
    # 최단경로가 존재하면 레이저 아님 포탄공격
    what=dfs(attark_n,loser_n)
    if what!=-1:
        grid[loser_r][loser_c] -= damage
        for nn in what:
            lr,lc=divmod(nn,N)
            grid[lr][lc] -= half_damage
            contain.extend([nn])

    # 레이저
    # 우/하/좌/상로 움직임,부서진 포탑이 있는 위치 지날 수 x,경로에있는애들은 공격력//2만큼 피해, 공격대상은 공격력만큼 피해
    else:
        # 포탄
        # 대상은 공격력만큼 피해,주위 8개방향의 포탑은 공격력//2만큼 피해
        grid[loser_r][loser_c]-=damage
        loser_nr, loser_nc=-1,-1
        aDX,aDY=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
        for dxx,dyy in zip(aDX,aDY):
            loser_nr, loser_nc = loser_r + dxx, loser_c + dyy
            if 0 <= loser_nr < N and 0 <= loser_nc < M:
                if grid[loser_nr][loser_nc] != 0:
                    grid[loser_nr][loser_nc] -= half_damage
                    contain.extend([loser_nr * N + loser_nc])
            else:
                loser_nr,loser_nc = loser_nr % N, loser_nc % M
                if grid[loser_nr][loser_nc] != 0:
                    grid[loser_nr][loser_nc] -= half_damage
                    contain.extend([loser_nr * N + loser_nc])

    ####공격끝####
    # 부서지지 않은 포탑중 공격자와 공격자대상빼고 포탄 공격력+1
    for i in range(N):
        for j in range(M):
            if grid[i][j]<=0:
                grid[i][j]=0
            curr=N*i+j
            if curr in contain or grid[i][j]<=0:
                continue
            grid[i][j]+=1
print(max(sum(grid,[])))