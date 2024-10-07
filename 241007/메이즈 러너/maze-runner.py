import heapq
from collections import deque

dxs,dys=[-1,1,0,0],[0,0,-1,1] #상하좌우

def can_go(x,y):
    return 0<=x and x<N and 0<=y and y<N and grid[x][y]<=0

def dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

#입력받기

N, M, K= map(int,input().split())
bye=M
grid=[list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    r,c=map(lambda x:int(x)-1, input().split())
    grid[r][c]-=1
er,ec=map(lambda x:int(x)-1, input().split())
grid[er][ec]=-11
ans=0

def move_unit():
    global grid,bye,ans
    temp=[row[:] for row in grid]
    for i in range(N):
        for j in range(N):
            if -11<grid[i][j]<0:
                mn=dist(er,ec,i,j)
                for dx,dy in zip(dxs,dys):
                    ni,nj=i+dx,j+dy
                    if can_go(ni,nj) and dist(er,ec,ni,nj)<mn:
                        ans+=1
                        if (ni,nj)!=(er,ec):
                            temp[ni][nj] += grid[i][j]
                            temp[i][j] -= grid[i][j]
                            break
                        else:
                            bye-=1
                            temp[i][j] -= grid[i][j]
                            break

    grid=temp


def find_square():
    mn=N
    for i in range(N):
        for j in range(N):
            if -11<grid[i][j]<0:
                mn=min(mn,max(abs(er-i),abs(ec-j)))

    for i in range(N-mn):
        for j in range(N-mn):
            if i<=er<=i+mn and j<=ec<=j+mn:
                for h in range(i,i+mn+1):
                    for w in range(j,j+mn+1):
                        if -11<grid[h][w]<0:
                            return mn+1,i,j

def rotate90(size, r,c):
    global grid,er,ec
    result=[row[:] for row in grid]
    for i in range(size):
        for j in range(size):
            result[r+j][c+size-i-1]=grid[r+i][c+j]-1 if grid[r+i][c+j]>0 else grid[r+i][c+j]
            if grid[r+i][c+j]==-11:
                er,ec=r+j,c+size-i-1
    grid=result


#main
for turn in range(1,K+1):
    #참가자 움직임(동시)
    move_unit()
    #회전 네모 찾기
    size, r, c=find_square()
    #회전
    rotate90(size, r, c)

    if bye==0:
        break


#출력
print(ans)
print(f'{er+1} {ec+1}')