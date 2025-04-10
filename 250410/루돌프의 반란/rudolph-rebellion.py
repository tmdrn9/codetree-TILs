#시작 3:00
#설계 끝 3:18
#코딩 끝 5:06
import heapq
from collections import deque
def distance(x,y,x1,y1):
    return (x-x1)**2+(y-y1)**2

N,M,P,C,D=map(int,input().split())
Rr,Rc=map(lambda x:int(x)-1 ,input().split())
santa=[(-1,-1) for _ in range(P+1)]
grid=[[0]*N for _ in range(N)]

for _ in range(P):
    n,sr,sc=map(int,input().split())
    santa[n]=(sr-1,sc-1)
    grid[sr-1][sc-1]=n
santa_score=[0]*(P+1)
santa_die=[1]+([0]*(P))
santa_kigul=[0]*(P+1)

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def move_r():
    global Rr,Rc
    q=[]
    ## 탈락하지 않은 산타 중 가장 가까운 산타를 향해 돌진 (r 큰거>c큰거)
    for i in range(1,P+1):
        if not santa_die[i]:
            sr,sc=santa[i][0], santa[i][1]
            heapq.heappush(q,(distance(Rr,Rc, sr,sc),-sr,-sc))
    d,sr,sc=heapq.heappop(q)
    sr=-sr
    sc=-sc
    i = santa.index((sr,sc))
    dx,dy=0,0
    if sr>Rr:
        Rr+=1
        dx=1
    elif sr<Rr:
        Rr-=1
        dx=-1
    if sc>Rc:
        Rc+=1
        dy=1
    elif sc<Rc:
        Rc-=1
        dy=-1
    if (Rr,Rc)==(sr,sc):
        # 루돌프가 움직여서 충돌 일어난 경우
        # 산타는 c만큼의 점수 획득+루돌프가 이동해온 방향으로 c만큼 밀려나기
        santa_score[i]+=C
        santa_kigul[i] += 2
        get_score(i,Rr,Rc,dx,dy,C)

def get_score(i,r,c,dx,dy,jump):
    nr,nc= r+(dx*jump),c+(dy*jump)
    santa[i]=(nr,nc)
    if not in_range(nr,nc):
        santa_die[i]=1

    elif grid[nr][nc]!=0:
        get_score(grid[nr][nc], nr, nc, dx, dy, 1)
        grid[nr][nc] = i
    else:
        grid[nr][nc]=i
    grid[r][c] = 0
## 산타와 루돌프 같은 칸에 있으면 발생
    ## 루돌프가 움직여서 충돌 일어난 경우, 산타는 c만큼의 점수 획득+루돌프가 이동해온 방향으로 c만큼 밀려나기
    ##밀려난 위치가 게임밖이라면 산타는 탈락
    ##밀려난 칸에 다른산타가 있는 경우, 그 산타는 1칸 해당방향으로 밀려나게 됨


s_dxs,s_dys=[-1,0,1,0],[0,1,0,-1]
for turn in range(M):

    #1루돌프 움직임
    move_r()
    if all(santa_die):
        break
    #2산타 순서대로 움직임
    for i in range(1,P+1):
        ##기절해있거나 격자밖으로 빠져나가 탈락한 산타는 움직일 수 없음
        if not santa_die[i] and santa_kigul[i]==turn:
            sx,sy=santa[i]
            original_dist = distance(Rr, Rc,sx,sy)
            q=[]
            for ii,(dx,dy) in enumerate(zip(s_dxs,s_dys)):
                nsx,nsy=sx+dx,sy+dy
                new_dist=distance(nsx,nsy,Rr,Rc)
                ##루돌프와 가까워지는 방향으로 이동
                ##다른산타가 있는 칸이나 게임판 밖으로 못움직임=>움직일수있는칸 없다면 움직이지않음
                ##움직일 수 있어도 가까워지는 방향이아니면 움직이지않음
                if in_range(nsx,nsy) and grid[nsx][nsy]==0 and original_dist>new_dist:
                    heapq.heappush(q,(new_dist,ii))
            if q:
                _,idx=heapq.heappop(q)
                grid[sx][sy]=0
                nsx, nsy=sx+s_dxs[idx],sy+s_dys[idx]
                grid[nsx][nsy] = i
                santa[i]=(nsx,nsy)
                if (Rr,Rc)==(nsx,nsy):
                    # 산타가 움직여서 충돌 일어난 경우, 산타는 d만큼의 점수 획득
                    # 자신이 이동해온 반대방향으로 d만큼 밀려남
                    santa_score[i] += D
                    santa_kigul[i] += 2
                    get_score(i,nsx,nsy,-s_dxs[idx],-s_dys[idx],D)

    #충돌
    ## 산타와 루돌프 같은 칸에 있으면 발생
    ## 루돌프가 움직여서 충돌 일어난 경우, 산타는 c만큼의 점수 획득+루돌프가 이동해온 방향으로 c만큼 밀려나기
    ##밀려난 위치가 게임밖이라면 산타는 탈락
    ##밀려난 칸에 다른산타가 있는 경우, 그 산타는 1칸 해당방향으로 밀려나게 됨

    #기절
    #루돌프와 충돌한 산타는 기절. 2턴 후부터 정상상태
    #기절해도 밀려날 수 있음
    #루돌프는 기절한 산타를 돌진대상으로 선택가능

    #게임종료
    # 모든 산타가 탈락하게되면 즉시 게임종료
    if all(santa_die):
        break

    # 매 턴 이후 탈락하지 않은 산타들은 +1점
    for i in range(1,P+1):
        if not santa_die[i]:
            if santa_kigul[i]<=turn:
                santa_kigul[i] += 1
            santa_score[i]+=1

#출력
for i in santa_score[1:]:
    print(i, end=' ')