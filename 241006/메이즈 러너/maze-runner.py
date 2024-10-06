import heapq
from collections import deque


dxs,dys=[-1,1,0,0],[0,0,-1,1] #상하좌우

def can_go(x,y):
    return 0<=x and x<N and 0<=y and y<N and grid[x][y]==0


N, M, K= map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
unit=[]
for i in range(1,M+1):
    unit.append(tuple(map(lambda x: int(x)-1,input().split())))
exit=tuple(map(lambda x: int(x)-1,input().split()))
ans=0

def min_dist(x1,x2,y1,y2):
    return abs(x1-x2)+abs(y1-y2)

def unit_move():
    ## 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야함
    #움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
    ##출구 도착시 바로 탈출
    global unit, ans
    rm=[]
    ap=[]
    for idx in range(len(unit)):
        b = False
        r,c=unit[idx]
        mm=min_dist(r,exit[0],c,exit[1])
        for dx,dy in zip(dxs,dys):
            tr,tc=r+dx,c+dy
            if can_go(tr,tc):
                if min_dist(tr,exit[0],tc,exit[1])<mm:
                    b=True
                    break
        if b:
            ans+=1
            if (tr, tc)!= exit:
                rm.append((r,c))
                ap.append((tr, tc))
            else:
                rm.append((r,c))

    for r,c in rm:
        unit.remove((r,c))
    for r,c in ap:
        unit.append((r,c))

    #unit=list(set(unit))

def rotate90(dist,sr,sc):
    global grid, exit
    rm=[]
    ap=[]
    temp_exit=None

    result = [row[:] for row in grid]
    for i in range(dist):
        for j in range(dist):
            # 벽이면 -1
            result[sr+j][sc+dist - i - 1] = grid[sr+i][sc+j]-1 if grid[sr+i][sc+j]>0 else grid[sr+i][sc+j]

            # 정사각형 안에 unit 있으면 위치변경
            if (sr+i,sc+j) in unit:
                for _ in range(unit.count((sr+i,sc+j))):
                    rm.append((sr+i,sc+j))
                    ap.append((sr+j,sc+dist - i - 1))
            #정사각형 안에 출구 있으면 위치변경
            if (sr+i,sc+j) ==exit:
                temp_exit=(sr+j,sc+dist - i - 1)

    for r,c in rm:
        unit.remove((r,c))
    for r,c in ap:
        unit.append((r,c))
    exit=temp_exit
    grid = result

def rotate_square():
    ##한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 잡아 90도 회전, 안에 벽 -1
    ##r작음>c작음
    q=[]
    ## 0,0/2,3
    temp=list(set(unit))
    for idx in range(len(temp)):
        r,c=temp[idx]
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
    print(f'size:{side},r:{i+1},c:{j+1}')

for kk in range(K):
    print(kk)

    #1모두 한칸씩 움직이기
    unit_move()

    if len(unit)==0:
        break

    #2미로 회전
    rotate_square()
    print(f'exit:{exit[0]+1},{exit[1]+1}')

#출력:모든 참가자들의 이동 거리 합과 출구 좌표
print(ans)
print(f'{exit[0]+1} {exit[1]+1}')