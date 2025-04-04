import heapq
from collections import deque
dxs,dys=[0,0,1,-1],[1,-1,0,0]

def in_range(x,y):
    return 0<=x<5 and 0<=y<5

def rotate90(x,y):
    new=[x[:] for x in grid]
    for i in range(3):
        for j in range(3):
            new[x+j][y+2-i]=grid[x+i][y+j]
    return new

def rotate180(x,y):
    new=[x[:] for x in grid]
    for i in range(3):
        for j in range(3):
            new[x+2-i][y+2-j]=grid[x+i][y+j]
    return new

def rotate270(x,y):
    new=[x[:] for x in grid]
    for i in range(3):
        for j in range(3):
            new[x+2-j][y+i]=grid[x+i][y+j]
    return new


K,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(5)]
new_fill=deque(list(map(int,input().split())))

def find_center():
    pq=[]
    ##3x3 격자선택
    ##90, 180, 270도 회전
    ##1차획득가치 최대화>회전각도 작은순>열 작은순>행작은순
    for i in range(3):
        for j in range(3):
            for degree in [90,180,270]:
                if degree==90:
                    new=rotate90(i,j)
                elif degree==180:
                    new=rotate180(i,j)
                else:
                    new=rotate270(i,j)
                s=bfs(new)
                heapq.heappush(pq,(-len(s),degree,j,i))
    return heapq.heappop(pq)
    

def bfs(new_grid):
    ##조각들이 3개이상 연결된 경우 사라짐
    ##사라진 조각애 새로 조각 입력: 열번호 작은순>행번호큰순
    score=0
    visited=[[0]*5 for _ in range(5)]
    total_remove=[]
    for i in range(5):
        for j in range(5):
            temp_remove=[(j,-i)]
            n=new_grid[i][j]
            visited[i][j]=1
            pq=deque([(i,j)])
            while pq:
                x,y=pq.popleft()
                for dx,dy in zip(dxs,dys):
                    nx,ny=x+dx,y+dy
                    if in_range(nx,ny) and new_grid[nx][ny]==n and not visited[nx][ny]:
                        visited[nx][ny]=1
                        pq.append((nx,ny))
                        temp_remove.append((ny,-nx))
            if len(temp_remove)>=3:
                total_remove.extend(temp_remove)
    return total_remove

def fill_(li):
    heapq.heapify(li)
    for _ in range(len(li)):
        j,i=heapq.heappop(li)
        grid[-i][j]=new_fill.popleft()
    
result=[]
for turn in range(K):
    #탐사진행
    score,degree,cy,cx=find_center()
    # print(score,degree,cy,cx)
    score=-score
    if score<=0:
        break
    if degree==90:
        grid=rotate90(cx,cy)
    elif degree==180:
        grid=rotate180(cx,cy)
    else:
        grid=rotate270(cx,cy)

    temp_result=0
    #유믈획득
    while True:
        rm_li=bfs(grid)
        # print(rm_li)
        if len(rm_li)>0:
            temp_result+=(len(rm_li))
            fill_(rm_li)
            # print(grid)
        else:
            break
    ##유물 연쇄 획득
    result.append(temp_result)
for i in result:
    print(i, end=' ')