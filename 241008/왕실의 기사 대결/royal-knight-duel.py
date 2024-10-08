from collections import deque

dxs,dys=[-1,0,1,0],[0,1,0,-1]

#입력
L, N, Q=map(int,input().split())

grid=[[2]*(L+2)]+[[2]+list(map(int,input().split()))+[2] for _ in range(L)]+[[2]*(L+2)]
init_k=[0]*(N+1)
unit={}
for i in range(1,N+1):
    unit[i]=list(map(int,input().split()))
    init_k[i]=unit[i][4]
def bfs(i,d):
    damage=[0]*(N+1)
    damage_unit=set()
    q=deque([])
    q.append(i)
    damage_unit.add(i)

    while q:
        cur=q.popleft()
        r,c,h,w,k=unit[cur]
        nr, nc = r + dxs[d], c + dys[d]
        for ii in range(h):
            for jj in range(w):
                if grid[nr+ii][nc+jj]==2:
                    return
                if grid[nr+ii][nc+jj]==1:
                    damage[cur]+=1

        for idx in unit:
            if idx in damage_unit:
                continue
            sr,sc,sh,sw,sk=unit[idx]
            if nr<=sr+sh-1 and sr<=nr+h-1 and nc<=sc+sw-1 and sc<=nc+h-1: #그 위치에 다른 기사있으면 연쇄적으로 이동
                q.append(idx)
                damage_unit.add(idx)

    damage[i]=0 #명령받은 기사는 피해입지 않음
    for idx in damage_unit: #기사들이 모두 밀린 후에 일괄적으로 대미지
        r,c,h,w,k=unit[idx]
        if k-damage[idx]<=0:
            unit.pop(idx)
        else:
            unit[idx]=[r+ dxs[d],c+ dys[d],h,w,k-damage[idx]]




#main
for turn in range(Q):
    i,d=map(int,input().split())
    # 체스판에 사라진 기사에게 명령을 내리면 반응x
    if i in unit:
        ##명령받은대로 이동
        bfs(i,d)

#기사이동
##그 위치에 다른 기사있으면 연쇄적으로 이동

#대결 대미지
##밀려난 기사들을 함정수만큼 피해입음



#출력: 생존 기사들의 대미지 합
ans=0
for idx in unit:
    ans+=init_k[idx]-unit[idx][4]
print(ans)