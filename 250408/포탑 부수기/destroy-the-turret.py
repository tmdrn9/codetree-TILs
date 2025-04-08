#시작3:25
#설계끝3:38
#코딩끝5:03

import heapq
from collections import deque

N,M,K=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
attack_time=[[0]*M for _ in range(N)]

def select_attacker():
    ##부서지지 않은 포탑중 공격력 가장 약함>가장최근 공격>행+열 큰거>열값 가장 큰
    q=[]
    for i in range(N):
        for j in range(M):
            if grid[i][j]!=0:
                heapq.heappush(q,(grid[i][j],-attack_time[i][j],-(i+j),-j))
    _,_,hap,c=heapq.heappop(q)
    hap=-hap
    c=-c
    return hap-c,c

def select_damager(attacker_r,attacker_c):
    #공격력 가장 강함>공격한지 오래된 포탑>행+열 작은거>열값작은거
    q = []
    for i in range(N):
        for j in range(M):
            if grid[i][j]!=0 and (i,j) != (attacker_r,attacker_c):
                heapq.heappush(q, (-grid[i][j], attack_time[i][j], i + j, j))
    if q:
        _, _, hap, c = heapq.heappop(q)
        return hap - c, c
    else:
        return -1,-1
def lazer(ar,ac,dr,dc):
    global attack_related
    # 우하좌상 순서대로 움직일 수 있음
    dxs,dys=[0,1,0,-1],[1,0,-1,0]
    pq=deque([(ar,ac)])
    visited=[[0]*M for _ in range(N)]
    visited[ar][ac]=1
    while pq:
        r,c=pq.popleft()
        for dx,dy in zip(dxs,dys):
            nr,nc=(r+dx)%N,(c+dy)%M#가장자리에서 막힌 방향이동하고자하면 반대편으로 나옴
            if grid[nr][nc]!=0 and not visited[nr][nc]: #부서진포탑 못지나감
                visited[nr][nc]=(r,c)
                pq.append((nr,nc))
                if (nr,nc)==(dr,dc):
                    break
    if visited[dr][dc]==0:
        return 0
    else:
        path=[]
        r,c=dr,dc
        while visited[r][c]!=1:
            nr,nc=visited[r][c]
            path.append((nr,nc))
            r,c=nr,nc
        ### 공격대상은 공격자의 공격력만큼 피해,경로에 포탑은 공격자의 공격력//2만큼 피해 (visited에 이전경로 저장)
        damage=grid[ar][ac]
        grid[dr][dc]= 0 if grid[dr][dc]<damage else grid[dr][dc]-damage
        damage//=2
        if len(path)!=1:
            for pr,pc in path[:-1]:
                grid[pr][pc]= 0 if  grid[pr][pc]<damage else grid[pr][pc]-damage
            attack_related.extend(path)
    return 1

def boom(ar,ac,dr,dc):
    global attack_related
    dxs, dys = [1,1,1,0,-1,-1,-1,0], [-1,0,1,1,1,0,-1,-1]
    damage = grid[ar][ac]
    grid[dr][dc]= 0 if grid[dr][dc]<damage else grid[dr][dc]-damage
    damage //= 2
    for dx,dy in zip(dxs,dys):
        nr,nc=(dr + dx) % N, (dc + dy) % M
        if (nr,nc)!=(ar,ac) and grid[nr][nc]!=0:
            grid[nr][nc]=0 if grid[nr][nc]<damage else grid[nr][nc]-damage
            attack_related.append((nr,nc))
###공격대상은 공격자의 공격력만큼 피해.주위 8개 방향에 있는 포탑은 공격자의 공격력//2만큼 피해
###공격자는 피해받지않음

for turn in range(1,K+1):
    attack_related=[]
    # 1공격자 선정
    ##M+N만큼 공격력 증가
    attacker_r,attacker_c=select_attacker()
    attack_time[attacker_r][attacker_c]=turn
    grid[attacker_r][attacker_c]+=(N+M)
    attack_related.append((attacker_r,attacker_c))
    #2공격자 공격
    ##2-1 공격대상 선정
    damager_r,damager_c=select_damager(attacker_r, attacker_c)
    if (damager_r,damager_c)==(-1,-1):
        break
    attack_related.append((damager_r,damager_c))
    ##2-2레이저 공격
    ok=lazer(attacker_r,attacker_c,damager_r,damager_c)
    ##2-3 레이저 안되면 포탄공격
    if not ok:
        boom(attacker_r,attacker_c,damager_r,damager_c)
    #3포탑 부서짐
    #4포탑정비
    ##부서지지않은 포탑중 공격과 무관했던 포탑이 공격력 +1
    for i in range(N):
        for j in range(M):
            if grid[i][j]!=0 and (i,j) not in attack_related:
                grid[i][j]+=1

result=0
for row in grid:
    result=max(max(row),result)
print(result)