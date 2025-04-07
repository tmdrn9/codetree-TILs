#시작12:18
#코딩시작 12:30
from collections import deque

dxs,dys=[-1,0,1,0],[0,1,0,-1]

L,N,Q=map(int,input().split())

grid=[[2]*(L+2) for _ in range(L+2)]
for ii in range(1,L+1):
    grid[ii]=[2]+list(map(int,input().split()))+[2]

person={}
original_k={}
for i in range(1,N+1):
    r, c, h, w, k =map(int,input().split())
    person[i]=(r, c, h, w, k)
    original_k[i]=k

def move_person(I,D):
    damage = [0] * (N + 1)
    pq=deque([I])
    p_move=set()
    p_move.add(I)
    while pq:
        n=pq.popleft()
        r, c, h, w, k = person[n]
        nr,nc=r+dxs[D],c+dys[D]
        for i in range(nr, nr + h):
            for j in range(nc, nc + w):
                if grid[i][j]==2:
                    return
                elif grid[i][j]==1:
                    damage[n]+=1
        for idx in person:
            if idx in p_move:
                continue
            ti,tj,th,tw,tk=person[idx]
            if nr+h-1>=ti and nr<=ti+th-1 and tj<=nc+w-1 and nc<=tj+tw-1:
                p_move.add(idx)
                pq.append(idx)

    damage[I]=0
    for idx in p_move:
        r, c, h, w, k = person[idx]
        if k<=damage[idx]:
            person.pop(idx)
            continue
        person[idx]=(r+dxs[D],c+dys[D], h, w, k-damage[idx])
    return

# 2. 대결대미지
##명령받은 기사가 다른기사 밀치면 밀려난 기사들, 이동한곳에 함정수 만큼 피해
##현재 체력 이상의 대미지받으면 체스판에서 사라짐
##기사들이 모두 밀린 후 피해 입음


for turn in range(Q):
    ##기사 명령 받기/ 체스판에 사라진 기사에게 명령 내리면 반엉 x
    i,d=map(int, input().split())
    if i in person:
        move_person(i,d)

result=0
for idx in person:
    result+=original_k[idx]-person[idx][4]
print(result)