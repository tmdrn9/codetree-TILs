#시작 1:00
#설계끝 1:36
#코딩끝 6:23 포기

# import sys
# sys.stdin=open('input.txt')
# input=sys.stdin.readline

from collections import deque
import heapq

N,M=map(int,input().split())
sr,sc,er,ec= map(int,input().split()) #집, 공원
temp=list(map(int,input().split()))
people={}
p_grid=[[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        p_grid[i].append([])

for i,idx in enumerate(range(0,M*2,2)):
    # people.append([temp[i],temp[i+1]])#전사들 위치
    people[i+1]=(temp[idx],temp[idx+1])
    p_grid[temp[idx]][temp[idx+1]].append(i+1)

grid=[list(map(int,input().split())) for _ in range(N)]
stop=[0]*(M+1)

#전사는 구분하지않고 아무곳으로나 이동
#메두사는 그들을 바라봄으로써 돌로 만들어 움직임 멈출 수 있음
turn=0
def in_range(x,y):
    return 0<=x<N and 0<=y<N

def me_move():
    # 메두사는 도로만으로 이동
    dxs,dys=[-1,1,0,0],[0,0,-1,1]# 여러 최단경로 가능하다면 상하좌우 우선순위
    visited=[[0]*N for _ in range(N)]
    q=deque([(sr,sc)])
    visited[sr][sc]=1
    while q:
        r,c=q.popleft()
        for dx,dy in zip(dxs,dys):
            nr,nc=r+dx,c+dy
            if in_range(nr,nc) and grid[nr][nc]==0 and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc]=(r,c)
    if visited[er][ec]==0:
        return -1
    else:
        path=[]
        r,c=er,ec
        while visited[r][c]!=1:
            nr,nc=visited[r][c]
            path.append((nr,nc))
            r,c=nr,nc
        path=path[:-1]
        result=deque([])
        for i in path[::-1]:
            result.append(i)
        result.append((er,ec))
        return result


def vieww_updown(idx,dx):
    p_stop=[]
    R = sr + dx
    ER= -1 if idx==0 else N
    visited = [[0] * N for _ in range(N)]
    temp = 0
    # 정면
    for i in range(R,ER ,dx):
        if in_range(i, sc):
            visited[i][sc] = 1
            if p_grid[i][sc] != []:
                for p in p_grid[i][sc]:
                    p_stop.append(p)
                    temp += 1
                break
    # 왼쪽+오른쪽
    minus = True
    for _ in range(2):
        c = 2
        for i in range(R, ER,dx):
            for cc in range(1, c):
                j = sc - cc if minus else sc + cc
                if in_range(i, j) and visited[i][j] != -1:
                    visited[i][j] = 1
                    if p_grid[i][j] != []:
                        for p in p_grid[i][j]:
                            p_stop.append(p)
                            temp += 1
                        for a in range(i + dx, ER,dx):
                            b = 2
                            visited[a][j]=-1
                            for bb in range(1, b):
                                tj = j - bb if minus else j + bb
                                if in_range(a, tj):
                                    visited[a][tj] = -1
            c += 1
        minus = False
    return temp, idx, p_stop, visited
def view_leftright(idx,dy):
    p_stop = []
    C=sc+dy
    EC= -1 if idx==2 else N
    visited = [[0] * N for _ in range(N)]
    temp = 0
    # 정면
    for i in range(C, EC, dy):
        if in_range(sr, i):
            visited[sr][i] = 1
            if p_grid[sr][i] != []:
                for p in p_grid[sr][i]:
                    p_stop.append(p)
                    temp += 1
                break
    # 왼오
    minus = True
    for _ in range(2):
        c = 2
        for i in range(C, EC, dy):
            for cc in range(1, c):
                j = sr - cc if minus else sr + cc
                if in_range(j,i) and visited[j][i] != -1:
                    visited[j][i] = 1
                    if p_grid[j][i] != []:
                        for p in p_grid[j][i]:
                            p_stop.append(p)
                            temp += 1
                        for a in range(i + dy,EC,dy):
                            b = 2
                            visited[j][a] = -1
                            for bb in range(1, b):
                                tj = j - bb if minus else j + bb
                                if in_range(tj,a):
                                    visited[tj][a] = -1
            c += 1
        minus = False
    return temp, idx, p_stop, visited
def me_eye():
    global stone
    ##상하좌우 중 전사를 가장 많이 볼 수 있는 방향으로 바라봄 =>heapq
    ## 90도 시야각 가지며 시야각 범위 안에 전사들을 볼 수 있음
    ##시야각 안에 들어있지만 다른 전사에게 가려진 전사의 경우 메두사에게 보이지 않음
    ## 메두사가 본 전사들은 돌로 변해 현재턴에는 움직일 수 없음
    ## 두명 이상 같은 위치에 있다면 해당칸의 전사 모두 돌로 변함
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    q=[]
    #상
    if sr>0:
        temp, idx, _,_=vieww_updown(0, -1)
        heapq.heappush(q, (-temp, idx))
    #하
    if sr<N-1:
        temp, idx, _ ,_= vieww_updown(1, 1)
        heapq.heappush(q, (-temp, idx))
    #좌
    if sc>0:
        temp, idx, _,_ = view_leftright(2, -1)
        heapq.heappush(q, (-temp, idx))
    #우
    if sc<N-1:
        temp, idx, _,_ = view_leftright(3, 1)
        heapq.heappush(q, (-temp, idx))

    _,idx=heapq.heappop(q)
    if idx<=1:
        _,_,p_stop,view=vieww_updown(idx, dxs[idx])
    else:
        _,_,p_stop,view=view_leftright(idx, dys[idx])
    for i in p_stop:
        if stop[i]==turn:
            stone += 1
        stop[i]=turn+1
    return view

def distance(x,y,x1,y1):
    return abs(x-x1)+abs(y-y1)
me_path=me_move()
if me_path==-1:#메두사의 집으로부터 공원까지 이어지는 도로가 존재하지 않는다면 -1 출력
    print(-1)
else:
    turn=0
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    while True:
        dist, stone, die = 0, 0, 0  # 전사 이동거리 합, 돌이된 전사수, 메두사가 공격한 전사수
    #1 메두사 이동
        sr,sc=me_path.popleft() # 도로를 따라 한칸 이동하며 공원까지 최단경로를 따름
        if (sr,sc)==(er,ec): #메두사가 공원 도착하는 턴에는 0을 출력
            break
        if p_grid[sr][sc]!=[]:# 메두사 이동칸에 전사가 있을경우 전사는 메두사에게 공격받고 사라짐
            for i in p_grid[sr][sc]:
                people.pop(i)
                p_grid[sr][sc].remove(i)

    #2 메두사 시선 =>함수화 (메두사위치, 바라보는 방향)
        view=me_eye()

    #3 전사들 이동
        ##메두사를 향해 최대 두칸 이동,메두사의 시야에 들어오는 곳으로 이동 불가
        ##3-1 메두사와의 거리를 줄일 수 있는 방향으로 이동 상하좌우 우선순위
        ##3-2메두사와의 거리를 줄일 수 있는 방향으로 이동 좌우상하 우선순위
        rm=[]
        for i in people:
            if stop[i]==turn:
                r,c=people[i]
                p_grid[r][c].remove(i)
                for m in range(2):
                    moved=False
                    if m==0:
                        li=[0,1,2,3]
                    else:
                        li=[2,3,0,1]
                    original_dist = distance(sr, sc, r, c)
                    q=[]
                    for idx in li:
                        nr,nc=r+dxs[idx],c+dys[idx]
                        new_dist=distance(sr,sc,nr,nc)
                        if in_range(nr,nc) and view[nr][nc]!=1 and original_dist>new_dist:
                            heapq.heappush(q,(new_dist,idx))
                    if q:
                        _,idx=heapq.heappop(q)
                        moved=True
                        dist+=1
                        r,c=r+dxs[idx],c+dys[idx]
                        if (r,c)==(sr,sc):

                            break
                    if not moved:
                        break
                if (r,c)==(sr,sc):
                    die+=1
                    rm.append(i)
                else:# (r,c)!=(sr,sc):
                    people[i]=(r,c)
                    p_grid[r][c].append(i)
        # 4 전사의 공격
        ##메두사와 같은칸에 도달한 전사는 메두사 공격하지만 져서 사라짐
        for i in rm:
            people.pop(i)
    #5 종료
    ## 메두사가 도달할때까지 매턴마다 모든 전사가 이동한 거리의 합, 메두사로 인해 돌이된 전사 수, 작성
        print(dist,stone,die)
        for i in people:
            if stop[i]<=turn:
                stop[i]=turn+1
        turn+=1
print(0)