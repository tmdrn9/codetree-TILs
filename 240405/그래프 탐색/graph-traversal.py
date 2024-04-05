n,m=map(int,input().split())
edges=[]
for _ in range(m):
    edges.append(tuple(map(int,input().split())))

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for x,y in edges:
    graph[x].append(y) 
    graph[y].append(x)    
cnt=0
def dfs(n):
    global cnt
    for curr in graph[n]:
        if not visited[curr]:
            cnt+=1
            visited[curr]=True
            dfs(curr)
    return cnt
visited[1]=True

print(dfs(1))