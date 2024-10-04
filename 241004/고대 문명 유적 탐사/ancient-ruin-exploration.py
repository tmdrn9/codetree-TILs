from collections import deque
import heapq

dxs,dys=[0,1,0,-1],[1,0,-1,0]

def rotation90(x,y):
    result=[row[:] for row in grid]
    for i in range(3):
        for j in range(3):
            result[x+j][y-i+2]=grid[x+i][y+j]
    return result


def rotation180(x,y):
    result=[row[:] for row in grid]
    for i in range(3):
        for j in range(3):
            result[x+2-i][y-j+2]=grid[x+i][y+j]
    return result

def rotation270(x,y):
    result=[row[:] for row in grid]
    for i in range(3):
        for j in range(3):
            result[x+2-j][y+i]=grid[x+i][y+j]
    return result

def in_range(x,y):
    return 0<=x and x<5 and 0<=y and y<5

def find_center():
    # 유물획득 가치>회전각도 작음>회전중심좌쵸 열작음
    pq=[]
    for i in range(3):
        for j in range(3):
            for d in [90,180,270]:
                if d==90:
                    new=rotation90(i,j)
                elif d==180:
                    new=rotation180(i,j)
                else:
                    new=rotation270(i,j)
                cnt=bfs(new)
                heapq.heappush(pq,(-len(cnt),d,j,i))
    return heapq.heappop(pq)

def bfs(new):
    p=deque([])
    visited=[[0]*5 for _ in range(5)]
    result=[]
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                temp_li=[(i,j)]
                p.append((i,j))
                visited[i][j]=1
                cnt=1
                while p:
                    r,c=p.popleft()
                    nn=new[r][c]
                    for dx,dy in zip(dxs,dys):
                        nr,nc=r+dx,c+dy
                        if in_range(nr,nc) and new[nr][nc]==nn and not visited[nr][nc]:
                            p.append((nr,nc))
                            visited[nr][nc]=1
                            temp_li.append((nr,nc))
                            cnt+=1
                if cnt>=3:
                    result.extend(temp_li)
    return result



def fill_(loc):
    pq=[]
    for i,j in loc:
        heapq.heappush(pq,(j,-i))
    
    while pq:
        c,r=heapq.heappop(pq)
        grid[-r][c]=v.popleft()


k,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(5)]
v=deque(list(map(int,input().split())))
answer=[0]*k

for kk in range(k):
    #1 탐사진행
    # 유물획득 가치>회전각도 작음>회전중심좌쵸 열작음
    cnt,d,c,r= find_center()

    #어떠한 방법을 사용하더라도 유물을 획득할 수 없었다면 모든 탐사는 그 즉시 종료
    if -(cnt)<3:
        break

    if d==90:
        grid=rotation90(r,c)
    elif d==180:
        grid=rotation180(r,c)
    else:
        grid=rotation270(r,c)
    ##아래 두개 획득할거 없을때까지 반복
    while True:
        #2 유물획득:  3개 이상 연결된 경우
        loc=bfs(grid)
        if len(loc)<3:
            break
        #3 유물채우기: 열번호 작음>행번호 큼
        fill_(loc)
        answer[kk]+=len(loc)

for ans in answer:
    if ans==0:
        break
    print(ans, end=' ')