import heapq,math
from collections import deque
def bfs(start, end):
    DX, DY = [0, 1, 0, -1], [1, 0, -1, 0]
    pq = deque([])
    path = [[[] for _ in range(M)] for _ in range(N)]
    pq.append(start)
    path[start[0]][start[1]]=(start[0],start[1])
    while pq:
        ci, cj = pq.popleft()
        for dx,dy in zip(DX, DY):
            ni,nj=(ci+dx)%N,(cj+dy)%M
            if len(path[ni][nj])==0 and grid[ni][nj]!=0:
                path[ni][nj]=(ci,cj)
                pq.append((ni,nj))

    if len(path[end[0]][end[1]])!=0:
        x,y = end
        v = [(x,y)]
        while (x,y) != start:
            (x,y) = path[x][y]
            v.append((x,y))
        return v[1:-1]
    else:
        return -1

N, M, K = map(int, input().split())
plus = N + M
grid = [list(map(int, input().split())) for _ in range(N)]
grid_t = [[-1] * M for _ in range(N)]

for turn in range(1, K + 1):
    temp = [i for i in sum(grid, []) if i > 0]
    if len(temp) == 1:
        break
    contain = []
    # 1가장 약한 포탑 선정
    # 가장 최근에 공격한 포탑>행열합이 가장 큰 포탑>열값이 가장 큰 포탑
    weak = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] <= 0:
                continue
            heapq.heappush(weak, (
                grid[i][j], -grid_t[i][j], -(i + j), -j, -i))
    _, _, _, attack_c, attack_r = heapq.heappop(weak)

    attack_c, attack_r = -attack_c, -attack_r
    grid_t[attack_r][attack_c] = turn
    contain.append((attack_r, attack_c))
    # n+m만큼의 공격력   증가
    grid[attack_r][attack_c] += plus
    damage = grid[attack_r][attack_c]
    half_damage = damage // 2

    # 2공격자 공격
    # 가장 강한 포탑 선정
    ## 공격한지 가장 오래된 포탑>행열합이 가장 작은 포탑>열값이 가장 작은 포탑
    strong = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] <= 0 or (i == attack_r and j == attack_c):
                continue
            heapq.heappush(strong,
                            (-grid[i][j], grid_t[i][j], (i + j), j, i))
    _, _, _, loser_c, loser_r = heapq.heappop(strong)
    contain.append((loser_r, loser_c))
    # 최단경로가 존재하면 레이저 아님 포탄공격
    what = bfs((attack_r, attack_c), (loser_r, loser_c))
    if what != -1:
        grid[loser_r][loser_c] -= damage
        for nn in what:
            lr, lc = nn
            grid[lr][lc] -= half_damage
            contain.append(nn)

    # 레이저
    # 우/하/좌/상로 움직임,부서진 포탑이 있는 위치 지날 수 x,경로에있는애들은 공격력//2만큼 피해, 공격대상은 공격력만큼 피해
    else:
        # 포탄
        # 대상은 공격력만큼 피해,주위 8개방향의 포탑은 공격력//2만큼 피해
        grid[loser_r][loser_c] -= damage
        loser_nr, loser_nc = -1, -1
        aDX, aDY = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
        for dxx, dyy in zip(aDX, aDY):
            loser_nr, loser_nc = loser_r + dxx, loser_c + dyy
            if 0 <= loser_nr < N and 0 <= loser_nc < M:
                if (loser_nr, loser_nc)==(attack_r,attack_c):
                    continue
                if grid[loser_nr][loser_nc] != 0:
                    grid[loser_nr][loser_nc] -= half_damage
                    contain.append((loser_nr, loser_nc))
            else:
                loser_nr, loser_nc = loser_nr % N, loser_nc % M
                if (loser_nr, loser_nc)==(attack_r,attack_c):
                    continue
                if grid[loser_nr][loser_nc] != 0:
                    grid[loser_nr][loser_nc] -= half_damage
                    contain.append((loser_nr, loser_nc))

    ####공격끝####
    # 부서지지 않은 포탑중 공격자와 공격자대상빼고 포탄 공격력+1
    for i in range(N):
        for j in range(M):
            if grid[i][j] < 0:
                grid[i][j] = 0
            if (i, j) in contain or grid[i][j] == 0:
                continue
            grid[i][j] += 1
print(max(sum(grid,[])))