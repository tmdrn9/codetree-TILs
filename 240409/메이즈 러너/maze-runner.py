import heapq, math
from collections import deque

DX,DY=[-1,1,0,0],[0,0,-1,1]#상하좌우

def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def rotate90(arr,bx,by):
    n,m=len(arr[0]),len(arr)
    new_arr=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if arr[i][j]<0:
                tr,tc=bx+i,by+j
                p[p.index([tr,tc,-arr[i][j]])]=[j+bx,m-i-1+by,-arr[i][j]]

            new_arr[j][m-i-1]=arr[i][j]-1 if 1<=arr[i][j]<=9 else arr[i][j]

    return new_arr

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
group=[]

p=[]
for i in range(1,M+1):
    x,y = list(map(int, input().split()))
    x-=1
    y-=1
    p.append([x,y,1])
    grid[x][y]-=1

dist = 0  # 이동거리
end_r,end_c=map(int, input().split())
end_r-=1
end_c-=1
grid[end_r][end_c]=100 #출구 표시
# check()
##########게임 시작###############
for turn in range(1, K + 1):
    if len(p)==0:
        break
    del_=[]
    add_=[]
    for i,pp in enumerate(p):
        x, y, n = pp
        for dx,dy in zip(DX,DY):
            nx,ny=x+dx,y+dy
            if in_range(nx,ny):
                if (nx,ny)==(end_r,end_c):
                    del_.append(pp)
                    grid[x][y]+=n
                    dist += n
                    break
                if grid[nx][ny]<=0 and distance(end_r,end_c,nx,ny)<distance(end_r,end_c,x,y):
                    del_.append(pp)
                    if grid[nx][ny]==0:
                        add_.append([nx, ny, n])
                    else:
                        p[i][2]+=n
                        # del_.append(pp)
                    grid[x][y]+=n
                    grid[nx][ny]-=n
                    dist+=n
                    break

    while del_:
        p.remove(del_.pop(-1))
    while add_:
        p.append(add_.pop(-1))
    ###이동끝###
    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형(r작은거,c작은거)
    min_p = []
    min_box=[]
    min_d=math.inf
    for pp in p:
        temp=distance(end_r,end_c,pp[0],pp[1])
        heapq.heappush(min_p,[temp,pp])
        if min_d>temp:
            min_d=temp

    min_p=[i[1] for i in min_p if i[0]==min_d]

    for i in min_p:
        w=max(abs(i[1]-end_c),abs(i[0]-end_r))
        if i[0]<=end_r:
            bx=end_r-w if end_r-w>=0 else 0
        else:
            bx=i[0]-w if i[0]-w>=0 else 0
        if i[1]<=end_c:
            by=end_c-w if end_c-w>=0 else 0
        else:
            by = i[1] - w if i[1] - w >= 0 else 0
        heapq.heappush(min_box,(bx, by,w))
    bx, by, width=heapq.heappop(min_box)

    temp=[]
    for i in grid[bx:bx+width+1]:
        temp.append(i[by:by+width+1])
    rotate_temp=rotate90(temp,bx,by)
    for i in range(width+1):
        grid[bx+i][by:by+width+1]=rotate_temp[i]
        if 100 in rotate_temp[i]:
            end_r,end_c=bx+i,rotate_temp[i].index(100)+by

    # 회전된 벽은 -1
print(dist)
print(end_r+1,end_c+1)