import heapq,math

DX,DY=[-1,1,0,0],[0,0,-1,1]

def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def rotate90(arr):
    n,m=len(arr[0]),len(arr)
    new_arr=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if 1<=arr[i][j]<=9:
                new_arr[j][m-i-1]=arr[i][j]-1
            else:
                new_arr[j][m - i - 1] = arr[i][j]
    return new_arr
def move(r,c):
    for dx,dy in zip(DX,DY):
        nr,nc=r+dx,c+dy
        if in_range(nr,nc) and not 1<=grid[nr][nc]<=9 and distance(r,c,exitr,exitc)>distance(nr,nc,exitr,exitc):
            return (nr,nc)
    return -1

def select_box():
    mdist = math.inf
    # 가장 가까운 사람찾기
    mp = []
    for pr, pc in location:
        p_dist = distance(pr, pc, exitr, exitc)
        heapq.heappush(mp, (p_dist, pr, pc))
        if p_dist < mdist:
            mdist = p_dist
    fp = [(i[1], i[2]) for i in mp if i[0] == mdist]

    fb = []
    for cr, cc in fp:
        width = max(abs(cc - exitc), abs(cr - exitr))
        if cr<=exitr:
            cr= 0 if exitr-width<=0 else exitr-width
        elif cr>exitr:
            cr=exitr
        if cc<=exitc:
            cc=0 if exitc-width<=0 else exitr-width
        elif cc>exitc:
            cc=exitc
        heapq.heappush(fb,(cr, cc))
    bx,by=heapq.heappop(fb)

    return width+1,bx,by



cnt=0
N, M, K=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
location=[]
for _ in range(M):
    x,y=map(lambda x:int(x)-1,input().split())
    grid[x][y]=-1
    location.append((x,y))
exitr,exitc=map(lambda x:int(x)-1,input().split())
grid[exitr][exitc] = 1000
arrive=0
for turn in range(1,K+1):

    # 사람 한명씩 다 움직이기(벽 없는 곳으로), 움직일 수 없으면 안움직임
    # 여러명 함께 가능
    add_=[]
    rm=[]
    for pr,pc in location:
        new=move(pr,pc)
        if new==-1:
            continue
        else:
            cnt +=1
            rm.append((pr,pc))
            add_.append(new)
            s=grid[pr][pc]
            grid[pr][pc]=0
            grid[new[0]][new[1]]+=s
    for i in range(len(add_)):
        location.append(add_[i])
    for i in range(len(rm)):
        location.remove(rm[i])

    location = list(set(location))
    if (exitr,exitc) in location:
        location.remove((exitr,exitc))

    # 출구와 한명이상 포함하는 가장작은 정사각형 잡기
    width, bx, by=select_box()
    temp=[[0]*width for _ in range(width)]
    for i in range(width):
        for j in range(width):
            temp[i][j]=grid[bx+i][by+j]
            if temp[i][j]<0:
                location.remove((bx+i,by+j))

    #90도 회전
    new_arr=rotate90(temp)
    for i in range(width):
        for j in range(width):
            grid[bx+i][by+j]=new_arr[i][j]
            if new_arr[i][j]<0:
                location.append((bx+i,by+j))
            if new_arr[i][j]>9:
                exitr,exitc=bx+i,by+j

    #모든 참가자가 도착했는지 확인해서 다 도착하면 끛
    if location==[]:
        break

# 모든 참가자들의 이동거리 합과 출구 좌표를 출력
print(cnt)
print(exitr+1, exitc+1)