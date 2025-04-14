import heapq
from collections import deque
# import sys
# sys.stdin=open('input.txt')
# input=sys.stdin.readline

dxs,dys=[-1,1,0,0],[0,0,-1,1]
def find_seperate(k):
    global grid
    visited=[[0]*N for _ in range(N)]
    temp=[row[:] for row in grid]
    cnt=0

    for i in range(N):
        for j in range(N):
            if grid[i][j]==k and not visited[i][j]:
                cnt+=1
                q=deque([(i,j)])
                visited[i][j]=1
                temp[i][j]=0
                while q:
                    r,c=q.popleft()
                    for dx,dy in zip(dxs,dys):
                        nr,nc=r+dx,c+dy
                        if 0<=nr<N and 0<=nc<N and grid[nr][nc]==k and not visited[nr][nc]:
                            q.append((nr,nc))
                            visited[nr][nc]=1
                            temp[nr][nc]=0

    if cnt>=2:
        grid=temp

def check_paper():
    paper={}
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j]!=0 and not visited[i][j]:
                n=grid[i][j]
                q=deque([(i,j)])
                visited[i][j]=1
                paper[n]=[(0,0)]

                while q:
                    r,c=q.popleft()
                    for dx,dy in zip(dxs,dys):
                        nr,nc=r+dx,c+dy
                        if 0<=nr<N and 0<=nc<N and grid[nr][nc]==n and not visited[nr][nc]:
                            q.append((nr,nc))
                            visited[nr][nc]=1
                            paper[n].append((nr-i,nc-j))
    return paper

N,K=map(int,input().split())
grid=[[0]*N for _ in range(N)]
answer=[0]*K
for k in range(1, K+1):
    #추가
    r1,c1,r2,c2=map(int,input().split())
    other=set()
    for i in range(r1,r2):
        for j in range(c1,c2):
            if grid[i][j]!=0:
                other.add(grid[i][j])
            grid[i][j]=k

    for o in other:
        find_seperate(o)

    #재배치
    paper=check_paper()
    hq=[]
    for i in paper:
        heapq.heappush(hq,(-len(paper[i]),i))

    grid = [[0] * N for _ in range(N)]
    while hq:
        _,kk =heapq.heappop(hq)
        for i in range(N):
            for j in range(N):
                cnt = 0
                temp = [row[:] for row in grid]
                for r,c in paper[kk]:
                    r,c=r+i,c+j
                    if 0 <= r < N and 0 <= c < N and grid[r][c]==0:
                        temp[r][c]=kk
                        cnt +=1
                    else:
                        break
                if len(paper[kk])==cnt:
                    break
            if len(paper[kk]) == cnt:
                break
        if len(paper[kk]) == cnt:
            grid=temp

    #시너지 계산
    good=set()
    visited = [[0] * N for _ in range(N)]
    visited_paper=[]
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0 and grid[i][j] not in visited_paper:
                n=grid[i][j]
                visited_paper.append(n)
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    r, c = q.popleft()
                    for dx, dy in zip(dxs, dys):
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] !=0 and not visited[nr][nc]:
                            if n==grid[nr][nc]:
                                q.append((nr, nc))
                                visited[nr][nc] = 1
                            else:
                                good.add((grid[nr][nc],n)) if grid[nr][nc]>=n else good.add((n,grid[nr][nc]))
    hap=0
    for i,j in good:
        hap+=len(paper[i])*len(paper[j])
    answer[k-1]=hap
for a in answer:
    print(a)
