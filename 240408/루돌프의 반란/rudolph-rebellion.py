import heapq
from collections import deque
def distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def move_santa(i, r, c, dr, dc, power):
    pq = deque([])
    pq.append((i, r, c, dr, dc, power))
    while pq:
        i, r, c, dr, dc, power = pq.popleft()
        nr, nc = r + (dr * power), c + (dc * power)
        if not in_range(nr, nc):
            alive[i] = 0
            return
        else:
            new_i = grid[nr][nc]
            grid[nr][nc] = i
            santa[i] = [nr, nc]
            if new_i != 0:
                pq.append((new_i, nr, nc, dr, dc, 1))

N, M, P, C, D = map(int, input().split())
Rr, Rc = map(int, input().split())
Rr -= 1
Rc -= 1

grid = [[0] * N for _ in range(N)]
grid[Rr][Rc] = -1
santa = [[-1, -1] for _ in range(P + 1)]
score = [0] * (P + 1)
alive = [1] * (P + 1)
alive[0] = 0
wakeup = [1] * (P + 1)


for _ in range(P):
    index, r, c = map(int, input().split())
    r -= 1
    c -= 1
    santa[index] = [r, c]
    grid[r][c] = index

sDX, sDY = [-1, 0, 1, 0], [0, 1, 0, -1]


##########게임 start#############
for turn in range(1,M+1):
    # 다죽었는지 확인
    if len(set(alive)) == 1:
        break

    pq = []
    # 가장 가까운 산타 정하기
    for i in range(1, P + 1):
        if alive[i] == 0:
            continue
        sr, sc = santa[i]
        heapq.heappush(pq, (distance(Rr, Rc, sr, sc), -sr, -sc, i))
    min_dist, S_r, S_c, targetS = heapq.heappop(pq)
    S_r, S_c=-S_r, -S_c
    mdr, mdc = 0, 0
    if Rr > S_r:
        mdr = -1
    elif Rr < S_r:
        mdr = 1

    if Rc > S_c:
        mdc = -1
    elif Rc < S_c:
        mdc = 1

    grid[Rr][Rc] = 0
    Rr, Rc = Rr + mdr, Rc + mdc
    grid[Rr][Rc] = -1

    if [Rr,Rc] == [S_r, S_c]:
        wakeup[targetS] = turn+2
        score[targetS] += C
        move_santa(targetS, S_r, S_c, mdr, mdc, C)

    for i in range(1, P + 1):
        if alive[i] == 0:
            continue
        if wakeup[i] >turn:
            continue
        sr, sc = santa[i]
        min_dist = distance(Rr, Rc, sr, sc)
        tlst = []
        for ddr, ddc in zip(sDX, sDY):
            nsr, nsc = sr + ddr, sc + ddc
            dist=distance(Rr, Rc, nsr, nsc)
            if min_dist > distance(Rr, Rc, nsr, nsc) and in_range(nsr, nsc) and grid[nsr][nsc] <= 0:
                min_dist=dist
                tlst.append((nsr, nsc, ddr, ddc))
        if len(tlst)==0:
            continue
        nsr, nsc, ddr, ddc=tlst[-1]
        grid[sr][sc] = 0
        original=grid[nsr][nsc]
        if original == 0:
            grid[nsr][nsc] = i
            santa[i]=[nsr,nsc]
        else:
            wakeup[i] =2+turn
            score[i] += D
            move_santa(i, nsr, nsc, -ddr, -ddc, D)

    # 살아있는애들 score+1
    for i in range(1, P + 1):
        if alive[i] == 0:
            continue
        score[i] += 1

for i in range(1, P + 1):
    print(score[i], end=' ')