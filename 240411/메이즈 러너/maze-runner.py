import heapq,math

DX,DY=[-1,1,0,0],[0,0,-1,1]

def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def rotate90(width,bx, by):
    for i in range(width):
        for j in range(width):
            if 1<=grid[bx+i][by+j]<=9:
                n_arr[bx+j][by+width-i-1]=grid[bx+i][by+j]-1
            else:
                n_arr[bx+j][by+width - i - 1] = grid[bx+i][by+j]
def move(r,c):
    for dx,dy in zip(DX,DY):
        nr,nc=r+dx,c+dy
        if in_range(nr,nc) and not 1<=grid[nr][nc]<=9 and distance(r,c,exitr,exitc)>distance(nr,nc,exitr,exitc):
            return (nr,nc)
    return -1

def select_box():
    mdist = math.inf
    fr,fc=-1,-1
    # 가장 가까운 사람찾기
    for pr, pc in [(i,j) for i in range(N) for j in range(N) if grid[i][j]<0]:
        p_dist = distance(pr, pc, exitr, exitc)
        if p_dist < mdist:
            mdist = p_dist
            fr,fc = pr, pc
    width = max(abs(fc - exitc), abs(fr - exitr))
    for i in range(N-width):
        for j in range(N-width):
            if i<=exitr<=i+width and j<=exitc<=j+width:
                for ni in range(i,i+width+1):
                    for nj in range(j,j+width+1):
                        if grid[ni][nj]<0:
                            return width+1,i,j


cnt=0
N, M, K=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    x,y=map(lambda x:int(x)-1,input().split())
    grid[x][y]-=1
exitr,exitc=map(lambda x:int(x)-1,input().split())
grid[exitr][exitc] = 1000
arrive=0
n_arr=[x[:] for x in grid]
for turn in range(1,K+1):
    # 사람 한명씩 다 움직이기(벽 없는 곳으로), 움직일 수 없으면 안움직임
    # 여러명 함께 가능
    add_ = []
    rm = []
    n_arr = [x[:] for x in grid]
    for pr, pc in [(i,j) for i in range(N) for j in range(N) if grid[i][j]<0]:
        new = move(pr, pc)
        if new == -1:
            continue
        else:
            cnt += -grid[pr][pc]
            n_arr[new[0]][new[1]] += grid[pr][pc]
            n_arr[pr][pc] -= grid[pr][pc]
            if new==(exitr,exitc):
                arrive+= -grid[pr][pc]

    grid = n_arr
    # 모든 참가자가 도착했는지 확인해서 다 도착하면 끛
    if arrive==M:
        break
        
    # 출구와 한명이상 포함하는 가장작은 정사각형 잡기
    width, bx, by=select_box()
    temp=[[0]*width for _ in range(width)]
    for i in range(width):
        for j in range(width):
            temp[i][j]=grid[bx+i][by+j]

    #90도 회전
    n_arr = [x[:] for x in grid]
    rotate90(width, bx, by)
    grid=n_arr

    for i in range(N):
        for j in range(N):
            if grid[i][j]> 9:
                exitr,exitc=i, j
                break


# 모든 참가자들의 이동거리 합과 출구 좌표를 출력
print(cnt)
print(exitr+1, exitc+1)