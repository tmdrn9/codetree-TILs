import sys
from collections import deque
import heapq

#우상좌하
dxs,dys=[0,-1,0,1],[1,0,-1,0]
#입력
n,m,k=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
point=[0]*m
ball=0
team=[[] for _ in range(m)]
head=[[0,0] for _ in range(m)]
tail=[0]*m

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def find_group():
    q=deque([])
    visited=[[0]*n for _ in range(n)]
    cnt=-1
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j]==1:
                cnt+=1
                tcnt=1
                q.append((i,j))
                visited[i][j]=1
                head[cnt] = [i, j]
                while q:
                    tx,ty=q.popleft()
                    team[cnt].append((tx, ty))
                    temp=[]
                    for dx,dy in zip(dxs,dys):
                        nx,ny=tx+dx,ty+dy
                        if in_range(nx,ny) and not visited[nx][ny] and grid[nx][ny]>0:
                            heapq.heappush(temp,(grid[nx][ny],nx,ny))
                    if temp!=[]:
                        _,nx,ny=heapq.heappop(temp)
                        if 0<grid[nx][ny]<4:
                            tcnt+=1
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                tail[cnt]=tcnt

#맨 앞에 있는 사람을 머리사람, 맨 뒤에 있는 사람을 꼬리사람
#[0] 각팀 찾기
find_group()

for turn in range(k):

    #[1]각팀 머리사람따라 한칸 이동
    for idx in range(m):

        q=deque([])
        tt=team[idx]
        q.extend(tt)
        q.rotate(1)
        team[idx]=list(q)
        head[idx]=team[idx][0]

        for nn,(i,j) in enumerate(team[idx]):
            if nn==0:
                grid[i][j]=1
            elif 0<nn<tail[idx]-1:
                grid[i][j]=2
            elif nn==tail[idx]-1:
                grid[i][j]=3
            else:
                grid[i][j]=4

    #[2]공 던져짐
    #[2-1] 공굴러가기
    if ball==0:
        bx, by = turn%n,0
    elif ball==1:
        bx, by = n-1, turn % n
    elif ball==2:
        bx, by = turn%n, n-1
    else:
        bx, by = 0, n-(turn % n)
    # [2-2] 최초만나는사람 팀 공얻기
    # print(ball,bx,by)
    ok = False
    for i in range(n):
        #최초에 만나게 되는 사람만이 공을 얻게 되어 점수 얻음
        if 0<grid[bx][by]<4:
            # 머리사람을 시작으로 팀 내에서 k번째 사람이라면 k의 제곱만큼 점수를 얻음
            for tm in range(m):
                if (bx,by) in team[tm]:
                    p=team[tm].index((bx,by))
                    point[tm]+=(p+1)**2

                    # 공을 획득한 팀은 즉시 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
                    q = deque([])
                    tt = team[tm]
                    for xx,yy in tt[::-1]:
                        q.append((xx,yy))
                    q.rotate(-(len(tt)-tail[tm]))
                    team[tm] = list(q)
                    head[tm] = team[tm][0]
                    ok=True
                    break
            if ok:
                break
        bx,by=bx+dxs[ball],by+dys[ball]
    ball= ((turn+1)//(n))%4

#출력
print(sum(point))