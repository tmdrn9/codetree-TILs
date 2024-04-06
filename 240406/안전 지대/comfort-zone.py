import heapq

n,m=map(int,input().split())
homes=[list(map(int,input().split())) for _ in range(n)]
pq=[]
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

def dfs(x,y):
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    for i,j in zip(dx,dy):
        new_x,new_y=x+i, y+j
        if in_range(new_x,new_y) and not visited[new_x][new_y]:
            visited[new_x][new_y]=True
            dfs(new_x,new_y)

max_k= max(max(homes)) if len(homes)>1 else max(homes)
if max_k==1:
    print(1,0)
else:
    for k in range(1,max_k-1):
        visited=[]
        for i in homes:
            visited.append(list(map(lambda x: True if x<=k else False ,i)))
        cnt=0
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                dfs(i,j)
                cnt+=1
        heapq.heappush(pq,(-cnt,k))
    max_,k=heapq.heappop(pq)
    print(k,-max_)