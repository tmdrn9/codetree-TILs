from collections import deque

dxs,dys=[-1,0,1,0],[0,1,0,-1]


L, N, Q=map(int,input().split())
grid=[[2]*(L+2)]+[[2]+ list(map(int,input().split()))+[2] for _ in range(L) ]+[[2]*(L+2)]
p={}
init_k=[0]*(N+1)
for i in range(1,N+1):
    p[i]=list(map(int,input().split()))
    init_k[i]=p[i][4]

def fight(start,d):
    q=deque()
    q_set=set()
    damage=[0]*(N+1)
    q.append(start)
    q_set.add(start)
    while q:
        cur=q.popleft()
        si,sj,h,w,k=p[cur]
        ni,nj=si+dxs[d],sj+dys[d]
        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                if grid[i][j]==2:#not in_range(i,j):
                    return
                if grid[i][j]==1:
                    damage[cur]+=1
        for idx in p:
            if idx in q_set:
                continue
            ti,tj,th,tw,tk=p[idx]
            if ni<=ti+th-1 and ti<=ni+h-1 and nj<=tj+tw-1 and tj<=nj+w-1:
                q.append(idx)
                q_set.add(idx)

    damage[start]=0
    for idx in q_set:
        ci,cj,h,w,k=p[idx]
        if k<=damage[idx]:
            p.pop(idx)
        else:
            p[idx]=[ci+dxs[d],cj+dys[d],h,w,k-damage[idx]]
                
            
                


for _ in range(Q):
    i,d=map(int,input().split())
    if i in p:
        fight(i,d)

ans=0
for i in p:
    ans+=init_k[i]-p[i][4]

print(ans)