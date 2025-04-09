#시작 1:00
#설계 끝 1:14
#코딩 끝 2:24

# import sys
# sys.stdin=open('input.txt')
# input=sys.stdin.readline

import heapq
N,M,K=map(int,input().split())
people=[]
grid=[list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    r,c=map(int,input().split())
    r-=1
    c-=1
    grid[r][c]-=1
    people.append((r,c))
exit_r, exit_c = map(int,input().split())
exit_r-=1
exit_c-=1
grid[exit_r][exit_c]=10

def distance(x,y,x1,y1):
    return abs(x-x1)+abs(y-y1)

move_count=0

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def move_people():
    global move_count,grid, people
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    ## 움직이는칸은 현재 머물러있던 칸보다 출구까지의 거리가 가까워야함
    ## 움직일 수 없으면 움직이지 않음
    ## 한 칸에 두명 이상의 참가자가 있을 수 있음
    ## 참가자가 출구에 도달하면 즉시 탈출
    temp_people=[]
    temp=[row[:] for row in grid]
    for r,c in people:
        move=False
        n_people=grid[r][c]
        if distance(exit_r, exit_c,r,c)==1:
            move = True
            move_count -= n_people
            temp[r][c] -= n_people
        else:
            for dx,dy in zip(dxs,dys):
                nr,nc=r+dx,c+dy
                if (0<=nr<N and 0<=nc<N and grid[nr][nc]<=0) and distance(nr,nc,exit_r, exit_c)<distance(r,c,exit_r, exit_c):
                    move=True
                    move_count-=n_people
                    temp[r][c]-=n_people
                    temp[nr][nc]+=n_people
                    temp_people.append((nr, nc))
                    break
        if not move:
            temp_people.append((r,c))
    people=temp_people
    grid=temp

def find_box():
    ### 2개 이상이면 r작은것>c작은것
    q=[]
    for r,c in people:
        rr=abs(r-exit_r)
        cc=abs(c-exit_c)
        box_size=max(rr,cc)
        if box_size==rr:
            br= r if r<exit_r else exit_r
            if c<=exit_c:
                bc=0 if exit_c-box_size<=0 else exit_c-box_size
            else:
                bc =0 if c-box_size<=0 else c-box_size

        else:
            bc= c if c<exit_c else exit_c
            if r<=exit_r:
                br =0 if exit_r-box_size<=0 else exit_r-box_size
            else:
                br = 0 if r - box_size <= 0 else r - box_size

        heapq.heappush(q,(box_size,br,bc))

    return heapq.heappop(q)

def rotate90(size,r,c):

    global grid,exit_r, exit_c
    result=[row[:] for row in grid]
    for i in range(size):
        for j in range(size):
            if 1<=grid[r+i][c+j]<=9:
                result[r+j][c+size-i-1]=grid[r+i][c+j]-1
            else:
                result[r + j][c + size - i - 1] = grid[r + i][c + j]
                if grid[r + i][c + j] == 10:
                    exit_r, exit_c =r + j,c + size - i - 1
                elif grid[r + i][c + j] <0:
                    people.remove((r+i,c+j))
                    people.append((r+j,c+size-i-1))
    grid=result

for turn in range(K):
    #1. 모든 참가지는 동시에 한칸씩 움직임 =>함수
    move_people()

    if len(people)<=0: #모든 참가자 탈출
        break

    #2. 미로회전
    ##한명 이상의 참가자와 출구를 포함한 가장작은 정사각형 선택 =>함수화
    box_size,br,bc=find_box()
    ##90도 회전+내구도 1씩 깍임 =>함수화
    rotate90(box_size+1,br,bc)

#모든 참가자들의 이동거리 합과 출구 좌표 출력
print(move_count)
print(exit_r+1,exit_c+1)
