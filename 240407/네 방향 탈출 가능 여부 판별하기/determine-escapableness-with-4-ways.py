from collections import deque
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
visited=[list(map(lambda x: True if x==0 else False, graph[i])) for i in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m
pq=deque([])
visited[0][0]=True
pq.append((0,0))
def bfs():
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    while pq:
        x,y=pq.popleft()
        for dxx,dyy in zip(dx,dy):
            new_x,new_y=x+dxx,y+dyy
            if in_range(new_x,new_y) and not visited[new_x][new_y]:
                visited[new_x][new_y]=True
                pq.append((new_x,new_y))

bfs()
answer= 1 if visited[-1][-1] else 0
print(answer)