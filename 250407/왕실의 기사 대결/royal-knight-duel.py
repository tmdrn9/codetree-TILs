#시작12:18
#코딩시작 12:30
from collections import deque
# import sys
# sys.stdin=open('input.txt')
# input=sys.stdin.readline
dxs,dys=[-1,0,1,0],[0,1,0,-1]

L,N,Q=map(int,input().split())

grid=[[2]*(L+2) for _ in range(L+2)]
p_grid=[[0]*(L+2) for _ in range(L+2)] #기사들 두는 그리드
for i in range(1,L+1):
    grid[i]=[2]+list(map(int,input().split()))+[2]
person=[[0,0,0,0,0] for _ in range(N+1)]
original_k=[0]*(N+1)
#기사위치 표시
for i in range(1,N+1):
    # 기사초기위치 rc, 직사각형형태hw, 체력k
    r,c,h,w,k=map(int,input().split())
    original_k[i]=k
    person[i]=[r,c,h,w,k]
    for ii in range(r,r+h):
        for jj in range(c,c+w):
            p_grid[ii][jj]=i

def move_person(I,D):
    global p_grid
    damage = [0] * (N + 1)
    p_temp_grid=[[0]*(L+2) for _ in range(L+2)]
    visited=[[0]*(L+2) for _ in range(L+2)]
    p_move=[I]
    r, c, h, w, k =person[I]
    pq=deque([])
    for i in range(r, r + h):
        for j in range(c, c + w):
            pq.append((i,j))
            visited[i][j]=1
    while pq:
        x,y=pq.popleft()
        nx,ny=x+dxs[D],y+dys[D]
        p_temp_grid[nx][ny] = p_grid[x][y]
        if grid[nx][ny]==1:
            damage[p_grid[x][y]]+=1
        if grid[nx][ny]==2:
            return
        else:
            if p_grid[nx][ny]>0 and not visited[nx][ny]:
                if p_grid[x][y] != p_grid[nx][ny]:
                    p_move.append(p_grid[nx][ny])
                    r, c, h, w, _ = person[p_grid[nx][ny]]
                    for i in range(r, r + h):
                        for j in range(c, c + w):
                            pq.append((i, j))
                            visited[i][j] = 1
                else:
                    visited[i][j]=1
                    pq.append((nx,ny))

    #만약 다 이동가능하다면 마지막에 있던애부터 이동 시작
    for i in p_move[::-1]:
        r, c, h, w, k = person[i]
        person[i]=[r+dxs[D], c+dys[D], h, w, k]

    #대미지 적용
    for i,dd in enumerate(damage):
        if i==I:
            continue
        person[i][4]-=dd
        if person[i][4]<0:
            r, c, h, w, _ = person[i]
            for ii in range(r, r + h):
                for jj in range(c, c + w):
                    p_temp_grid[ii][jj]=0
    p_grid=p_temp_grid
    return

# 2. 대결대미지
##명령받은 기사가 다른기사 밀치면 밀려난 기사들, 이동한곳에 함정수 만큼 피해
##현재 체력 이상의 대미지받으면 체스판에서 사라짐
##기사들이 모두 밀린 후 피해 입음


for turn in range(Q):
    ##기사 명령 받기/ 체스판에 사라진 기사에게 명령 내리면 반엉 x
    i,d=map(int, input().split())
    if person[i][4]<=0:
        continue
    move_person(i,d)

result=0
for i in range(1,N+1):
    if person[i][4]>0:
        result+=original_k[i]-person[i][4]
print(result)