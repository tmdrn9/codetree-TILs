def in_range(x,y):
    return 0<=x<n and 0<=y<n

def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def hello_runner(d):
    global score
    answer=[]
    check=[(x,y),(x+MX[d],y+MY[d]),(x+MX[d]*2,y+MY[d]*2)]

    for i, r in enumerate(runner):
        if r in check and grid[r[0]][r[1]]==0:
            score+=t
            p_grid[r[0]][r[1]] = 0
            answer.append(r)
    return answer



MX,MY=[-1,0,1,0],[0,1,0,-1] #슐래 토네이도
DX,DY=[0,0,1,-1],[-1,1,0,0] #좌오하상 #러너꺼

score=0
n, m, h, k=map(int, input().split())
grid=[[0]*n for _ in range(n)]
p_grid = [[0] * n for _ in range(n)]
runner=[]
runner_d=[]
for _ in range(m):
    x,y,d=map(int, input().split())
    runner.append((x-1,y-1))
    p_grid[x-1][y-1]+=1
    runner_d.append(d)
for _ in range(h):
    x, y = map(int, input().split())
    grid[x-1][y-1]=-1 #나무는 -1로 표시

x,y=n//2,n//2 # 술래 위치
dist = 1
idx = 0
inout=0
t = 0
total = 0
t_dist = 0
visited=[[False]*n for _ in range(n)]
visited[0][0] =True
rm=set([])
# k번 반복
for turn in range(1,k+1):

    cp=[x[:] for x in p_grid]
    for i in range(len(runner)):
        # 1. 도망자 움직임 단, 거리가 3 이하인 도망자만 동시에 움직임
        if i in rm:
            continue
        rx,ry=runner[i]
        rd=runner_d[i]
        if distance(x,y,rx,ry)<=3:
            # 바라보고 있는 방향으로 한칸씩 이동
            nx,ny= rx+DX[rd],ry+DY[rd]
            # 움직이려는 칸에 술래가 있는 경우엔 움직이지 않음
            if (nx,ny)==(x,y):
                continue
            # 격자를 벗어나는 경우 방향을 틀고, 술래가 없을때만 1칸 이동
            if not in_range(nx,ny):
                if rd==1:
                    runner_d[i],rd=0,0
                elif rd==0:
                    runner_d[i],rd = 1,1
                elif rd==2:
                    runner_d[i],rd = 3,3
                else:
                    runner_d[i],rd = 2,2
                nx,ny= rx+DX[rd],ry+DY[rd]
                if (nx, ny) == (x, y):
                    continue
                else:
                    cp[rx][ry] -= 1
                    cp[nx][ny] += 1
                    runner[i]=(nx,ny)
            else:
                cp[rx][ry] -= 1
                cp[nx][ny] += 1
                runner[i] = (nx, ny)

        else:
            continue
    p_grid=cp

    #t_dist,dist,idx,inout,t,total
    if inout==0:
        x, y = x + MX[idx], y + MY[idx]
        t+=1
        t_dist+=1
        if (x, y) == (0, 0):
            inout=1
            t_dist,total,dist,t,idx=0,0,1,0,2
        else:
            if t_dist==dist:
                idx = (idx + 1) % 4
                t_dist=0
            if t==total+dist*2:
                total+=t
                dist+=1
    #밖에서 안으로
    else:
        x, y = x + MX[idx], y + MY[idx]
        visited[x][y]=True
        if (x, y) == (n//2, n//2):
            visited = [[False] * n for _ in range(n)]
            visited[0][0]=True
            idx=0
            inout=0
        else:
            if in_range(x + MX[idx], y + MY[idx])==False or visited[x + MX[idx]][y + MY[idx]]:
                idx=(idx-1)%4

    rm_li=hello_runner(idx)
    for i in range(len(runner)):
        if runner[i] in rm_li:
            rm.add(i)
    if len(rm)==m:
        break
print(score)