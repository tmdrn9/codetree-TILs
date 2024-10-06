import heapq
from collections import deque


dxs,dys=[-1,1,0,0],[0,0,-1,1] #상하좌우

def can_go(x,y):
    return 0<=x and x<N and 0<=y and y<N and grid[x][y]<=0


N, M, K= map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
for i in range(M):
    r,c=map(lambda x: int(x) - 1, input().split())
    grid[r][c]-=1

exit=tuple(map(lambda x: int(x)-1,input().split()))
grid[exit[0]][exit[1]]=-11

ans=0

def min_dist(x1,x2,y1,y2):
    return abs(x1-x2)+abs(y1-y2)

def unit_move():
    ## 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야함
    #움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
    ##출구 도착시 바로 탈출
    global ans,grid,cnt
    temp=[row[:] for row in grid]
    for i in range(N):
        for j in range(N):
            if grid[i][j]<0:
                b=False
                mm=min_dist(i,exit[0],j,exit[1])
                for dx,dy in zip(dxs,dys):
                    tr,tc=i+dx,j+dy
                    if can_go(tr,tc) and min_dist(tr,exit[0],tc,exit[1])<mm:
                        ans-=grid[i][j]
                        temp[i][j]-=grid[i][j]
                        if (tr, tc)!= exit:
                            temp[tr][tc]+=grid[i][j]
                        else:
                            cnt+=grid[i][j]
                        break
    grid=temp
def rotate90(dist,sr,sc):
    global grid, exit
    result = [row[:] for row in grid]
    temp_exit=None
    for i in range(dist):
        for j in range(dist):
            # 벽이면 -1
            result[sr+j][sc+dist - i - 1] = grid[sr+i][sc+j]-1 if grid[sr+i][sc+j]>0 else grid[sr+i][sc+j]
            #정사각형 안에 출구 있으면 위치변경
            if (sr+i,sc+j) ==exit:
                temp_exit=(sr+j,sc+dist - i - 1)
    exit=temp_exit
    grid = result

def rotate_square():
    ##한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 잡아 90도 회전, 안에 벽 -1
    ##r작음>c작음
    q=[]
    ## 0,0/2,3
    for r in range(N):
        for c in range(N):
            if grid[r][c]<0 and grid[r][c]>-11:
                side=max(abs(r-exit[0])+1,abs(c-exit[1])+1) #변의 크기
                if r <= exit[0]:
                    sr = 0 if exit[0] - side +1<= 0 else exit[0] - side+1
                else:
                    sr = exit[0]

                if c <= exit[1]:
                    sc = 0 if exit[1] - side+1 <= 0 else exit[1] - side+1
                else:
                    sc = exit[1]
                heapq.heappush(q,(side,sr,sc))
    side,i,j=heapq.heappop(q)
    rotate90(side,i,j)

cnt=M
for kk in range(K):
    print(kk)

    #1모두 한칸씩 움직이기
    unit_move()

    if cnt==0:
        break

    #2미로 회전
    rotate_square()

#출력:모든 참가자들의 이동 거리 합과 출구 좌표
print(ans)
print(f'{exit[0]+1} {exit[1]+1}')