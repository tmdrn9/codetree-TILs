from collections import deque
#2:33 시작
#2:48 설계 끝
#
dxs,dys=[-1,0,1,0],[0,1,0,-1]
r,c,k= map(int,input().split())
grid=None
def make_grid():
    global grid
    grid=[[-1]+[0]*c+[-1] for _ in range(r+3)]
    grid.append([-1]*(c+2))
make_grid()


exit=[]
def move_g(n,ci,di):
    reset=False
    #골렘위치는 n
    ri=1
    # 1-1 못내려가면 서쪽으로 갔다가 내려감 => 출구 반시계방향으로
    # 1-2 못내려가면 동쪽으로 갔다가 내려감 => 출구는 시계방향
    # 1-3 골렘이 최대한 내려갔는데 몸의 일부가 숲을 벗어나면 숲 리셋
    while True:
        if grid[ri+2][ci]==0 and grid[ri+1][ci-1]==0 and grid[ri+1][ci+1]==0:
            ri+=1
        elif grid[ri-1][ci-1]==0 and grid[ri][ci-2]==0 and grid[ri+1][ci-1]==0 and grid[ri+1][ci-2]==0 and grid[ri+2][ci-1]==0:
            ri+=1
            ci-=1
            di-=1
            if di<0:
                di=3
        elif grid[ri-1][ci+1]==0 and grid[ri][ci+2]==0 and grid[ri+1][ci+1]==0 and grid[ri+2][ci+1]==0 and grid[ri+1][ci+2]==0:
            ri+=1
            ci+=1
            di=(di+1)%4
        else:
            break
    if ri<=2 or ci<2 or ci>c:
        reset=True
    else:
        grid[ri][ci]=n
        for d in range(4):
            if d==di:
                exit.append((ri+dxs[d],ci+dys[d]))
            grid[ri+dxs[d]][ci+dys[d]]=n
    return reset,ri,ci

def can_go(x,y,nx,ny):
    return grid[x][y]==grid[nx][ny] or ((x,y) in exit and grid[x][y]!=grid[nx][ny])
    
def bfs(ri,ci):
    visited=[[0]*(c+2) for _ in range(r+3)]
    # if ri-2==r-1:
    #     return r
    # else:
    pq=deque([(ri,ci)])
    visited[ri][ci]=1
    while pq:
        x,y=pq.popleft()
        for d in [2,3,0,1]:
            nx,ny=x+dxs[d],y+dys[d]
            if grid[nx][ny]>0 and can_go(x,y,nx,ny) and not visited[nx][ny]:
                visited[nx][ny]=1
                pq.append((nx,ny))
    # print(visited)  
    for rr in range(r+2,0,-1):
        if 1 in visited[rr]:
            return rr-2


# 2-1정령은 어떤 방향에서든 탑승가능/탈출은 출구만을 사용
# 2-2 정령이 이동하는 최종 위치의 행 누적


result=0
for i in range(1,k+1):
    #i번째 골렘은 중앙이 c,초기 골레 출구는 d
    ci,di=map(int,input().split())
    #1 가능할때까지 남쪽으로 골렘 이동[move_g]
    reset,ri,ci=move_g(i,ci,di)
    # print(grid)
    # print(ri,ci)
    if reset:
        make_grid()
        exit=[]
        continue
    #2 가능한때까지 남쪽으로 정령 이동[bfs]
    final_n=bfs(ri,ci)

    result+=final_n
print(result)