import heapq
n=int(input())
grid=[]
visited=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    grid.append(temp)
    visited.append(list(map(lambda x: False if x else True,temp)))

people=[]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def dfs(x,y):
    global cnt
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    for i,j in zip(dx,dy):
        new_x,new_y=x+i,y+j
        if in_range(new_x,new_y) and not visited[new_x][new_y]:
            visited[new_x][new_y]=True
            dfs(new_x,new_y)
            cnt+=1


for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        visited[i][j]=True
        cnt=1
        dfs(i,j)
        heapq.heappush(people,cnt)

print(len(people))
while people:
    print(heapq.heappop(people))