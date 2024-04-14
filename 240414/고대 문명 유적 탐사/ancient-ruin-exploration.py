import heapq
from collections import deque


def in_range(x,y):
    return 0<=x<5 and 0<=y<5

def rotate90(x,y):
    new=[x[:] for x in grid]
    for i in range(3):
        for j in range(3):
            new[x+j][y+2-i]=grid[x+i][y+j]
    return new

def rotate180(x,y):
    new=[x[:] for x in grid]
    for i in range(3):
        for j in range(3):
            new[x+2-i][y+2-j]=grid[x+i][y+j]
    return new

def rotate270(x,y):
    new=[x[:] for x in grid]
    for i in range(3):
        for j in range(3):
            new[x+2-j][y+i]=grid[x+i][y+j]
    return new

def findxy():
    q=[]
    for i in range(3):
        for j in range(3):
            for r in [90,180,270]:
                if r==90:
                    new=rotate90(i,j)
                elif r==180:
                    new=rotate180(i,j)
                else:
                    new=rotate270(i,j)
                loc=bfs(new)
                heapq.heappush(q,(-len(loc),r,j,i))
    return heapq.heappop(q)

DX,DY=[-1,1,0,0],[0,0,-1,1]

def bfs(new):
    loc=[]
    visited=[[False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp_loc=[(i,j)]
            visited[i][j]=True
            q=deque([(i,j)])
            nn=new[i][j]
            while q:
                x,y=q.popleft()
                for d in range(4):
                    X,Y=x+DX[d],y+DY[d]
                    if in_range(X,Y) and new[X][Y]==nn and not visited[X][Y]:
                        visited[X][Y]=True
                        temp_loc.append((X,Y))
                        q.append((X,Y))
            if len(temp_loc)>=3:
                loc.extend(temp_loc)
    return loc

def fillblock(li):
    global grid
    pq=[]
    for x,y in li:
        heapq.heappush(pq,(y,-x))
    while pq:
        j,i=heapq.heappop(pq)
        n=m_li.popleft()
        grid[-i][j]=n


K, _ = map(int, input().split())
answer = [0] * K
grid = [list(map(int, input().split())) for _ in range(5)]
m_li = deque(list(map(int, input().split())))

for turn in range(K):

    score, r, j, i = findxy()
    if score == 0:
        break

    if r == 90:
        grid = rotate90(i,j)
    elif r == 180:
        grid = rotate180(i,j)
    else:
        grid = rotate270(i,j)

    while True:
        answer[turn] -= score
        loc = bfs(grid)
        fillblock(loc)
        temp_score = bfs(grid)
        if len(temp_score) < 3:
            break
        score = -len(temp_score)

for i in answer:
    if i == 0: break
    print(i, end=' ')