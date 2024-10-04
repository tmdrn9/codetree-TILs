from collections import deque
import heapq

#0, 1, 2, 3 중에 하나이며 각각 위쪽, 오른쪽, 아래쪽, 왼쪽
dxs,dys=[-1,0,1,0],[0,1,0,-1]

def in_range(x,y):
    return 0<=x and x<L and 0<=y and y<L

def damege(d_li):
    for i in d_li:
        r,c,h,w,k=p[i]
        for hh in range(h):
            if grid[r+hh][c]==1 and p[i][4]>0:
                p[i][4]-=1
                p_d[i]+=1
        for ww in range(w):
            if grid[r][c+ww]==1 and p[i][4]>0:
                p[i][4]-=1
                p_d[i]+=1
        if p[i][4]<0:
            for row in p_grid[r:r + h]:
                row[c:c + w] = [0] * w

def bfs(i,d):
    q=deque([])
    def add_i(i):
        r,c,h,w,k=p[i]
        for hh in range(h):
            q.append((r+hh,c))
        for ww in range(1,w):
            q.append((r,c+ww))

    m_i=set([])
    add_i(i)
    visited=[[0]*L for _ in range(L)]
    while q:
        r,c=q.popleft()
        newr,newc=r+dxs[d],c+dys[d]
        if not in_range(newr,newc) or grid[newr][newc]==2:
            return 0
        else:
            if not visited[newr][newc] and p_grid[newr][newc]!=0:
                visited[newr][newc]=1
                add_i(p_grid[newr][newc])
                m_i.add(p_grid[newr][newc])

    for m in list(m_i)[::-1]+[i]:
        r,c,h,w,k=p[m]
        for row in p_grid[r:r+h]:
            row[c:c+w]=[0]*w
        pr,pc=r+dxs[d],c+dys[d]
        for row in p_grid[pr:pr+h]:
            row[pc:pc+w]=[m]*w
        p[m]=[pr,pc,h,w,k]
    return m_i





#체스판크기, 초기 기사 정보, 왕의 명령
L, N, Q = map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(L)]
p_grid=[[0]*L for _ in range(L)]
p=[[0,0,0,0,0]]
for i in range(N):
    r,c,h,w,k=map(int,input().split())
    p.append([r-1,c-1,h,w,k])
    for row in p_grid[r-1:r -1 + h]:
        row[c-1 :c -1 + w] = [i+1]*w


k=[list(map(int,input().split())) for _ in range(Q)]
p_d=[0]*(len(p)+1)

for i,d in k:
    #print(p_grid)
    # i번 기사에게 방향 d로 한 칸 이동하라는 명령
    #체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 됩니다.
    if p[i][4]<=0:
        continue

    # 명령 실행
    d_li=bfs(i,d)

    #데미지
    if d_li !=0:
        damege(d_li)

    #print(p_grid)
answer=0
for n in range(1,N+1):
    if p[n][4]>0:
        answer+=p_d[n]
print(answer)