from collections import deque

dxs,dys=[-1,0,1,0],[0,1,0,-1]

L, N, Q=map(int,input().split())
grid=[[2]*(L+2)]+[[2]+list(map(int,input().split()))+[2] for _ in range(L)]+[[2]*(L+2)]
unit={}
init_k=[0]*(N+1)

for i in range(1,N+1):
    unit[i]=list(map(int,input().split()))
    init_k[i]=unit[i][4]

def fight(start,d):
    q=deque()
    d_set=set()
    damage=[0]*(N+1)

    q.append(start)
    d_set.add(start)

    while q:
        cur=q.popleft()
        si,sj,sh,sw,_=unit[cur]
        ni,nj=si+dxs[d],sj+dys[d]
        for i in range(ni,ni+sh):
            for j in range(nj,nj+sw):
                if grid[i][j]==2:
                    return
                if grid[i][j]==1:
                    damage[cur]+=1
        
        for idx in unit:
            if idx in d_set:
                continue

            ti,tj,th,tw,_=unit[idx]
            if ni<=ti+th-1 and ti<=ni+sh-1 and nj<=tj+tw-1 and tj<=nj+sw-1:
                d_set.add(idx)
                q.append(idx)
        
    damage[start]=0
    for idx in d_set:
        if unit[idx][4]-damage[idx]<=0:
            unit[idx].pop()
            continue
        unit[idx][4]-=damage[idx]

for _ in range(Q):
    i,d=map(int,input().split())
    if i in unit:
        fight(i,d)


result=0
for idx in unit:
    result+=init_k[idx]-unit[idx][4]
print(result)