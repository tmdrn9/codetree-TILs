from collections import deque
import heapq
import copy

dxs,dys=[0,1,0,-1],[1,0,-1,0]
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

n,k,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
k_li=[tuple(map(lambda x:int(x)-1,input().split())) for _ in range(k)]

#돌맹이 위치확인
m_li=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            m_li.append((i,j))

#치울 돌맹이 조합
arr=[x for x in range(0,len(m_li))]
combi_arr=[]
def combinations(n,new_arr,c):
    if len(new_arr)==n:
        combi_arr.append(new_arr)
        return
    for i in range(c,len(arr)):
        combinations(n,new_arr+[arr[i]],i+1)
combinations(m,[],0)

result=0
for idx in combi_arr:
    visited=[[0]*n for _ in range(n)]
    #돌맹이 치우기
    temp=copy.deepcopy(grid)
    for v in idx:
        i,j=m_li[v]
        temp[i][j]=0
    #치운거에서 움직이기
    for rr,cc in k_li:
        q=deque([])
        q.append([rr,cc])
        visited[rr][cc]=1
        while q:
            r,c=q.popleft()
            for dx,dy in zip(dxs,dys):
                newr,newc=r+dx,c+dy
                if in_range(newr,newc) and temp[newr][newc]==0 and visited[newr][newc]==0:
                    q.append([newr,newc])
                    visited[newr][newc]=1
    cnt=0
    for vs in visited:
        for vv in vs:
            if vv==1:
                cnt+=1

    if result<cnt:
        result=cnt
print(result)