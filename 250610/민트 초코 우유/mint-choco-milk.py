import heapq
from collections import deque

dxs,dys=[-1,1,0,0],[0,0,-1,1]

N,T= map(int,input().split())
food=[list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if food[i][j]=='T':
            food[i][j] =0b100
        elif food[i][j]=='C':
            food[i][j] =0b010
        else:
            food[i][j] =0b001

trust=[list(map(int,input().split())) for _ in range(N)]

def sum_trust():
    result=[0]*7
    for i in range(N):
        for j in range(N):
            t_food=food[i][j]
            if t_food==0b111:
                result[0]+=trust[i][j]
            elif t_food==0b110:
                result[1] += trust[i][j]
            elif t_food==0b101:
                result[2] += trust[i][j]
            elif t_food==0b011:
                result[3] += trust[i][j]
            elif t_food==0b001:
                result[4] += trust[i][j]
            elif t_food==0b010:
                result[5] += trust[i][j]
            else:
                result[6] += trust[i][j]
    return result

def gruop():
    global food, trust
    ##인접한 학생들과 신봉음식이 완전히 같은 경우, 그룹형성
    ##그룹 내 대표자 선정: 신앙심>r작은사람>c작은사람
    ##대표자의 신앙심은 +(그룹원수-1)/나머지 그룹원 신앙심 -1
    li_group=[]
    visited=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                temp_group=[]
                q=deque([(i,j)])
                visited[i][j]=1
                trustfood=food[i][j]
                heapq.heappush(temp_group, (-trust[i][j], i, j))
                while q:
                    r,c=q.popleft()
                    for dx,dy in zip(dxs,dys):
                        nr,nc=r+dx,c+dy
                        if (0<=nr and nr<N and 0<=nc and nc<N) and not visited[nr][nc] and trustfood==food[nr][nc]:
                            visited[nr][nc] = 1
                            q.append((nr,nc))
                            heapq.heappush(temp_group,(-trust[nr][nc],nr,nc))
                li_group.append(temp_group)
    leaders = []
    for g in li_group:
        n_p=len(g)
        if n_p==1:
            leaders.append(g[0])
        else:
            for n,p in enumerate(g):
                if n==0:
                    trust[p[1]][p[2]]+=n_p-1
                    leaders.append((-trust[p[1]][p[2]],p[1],p[2]))
                else:
                    trust[p[1]][p[2]] -= 1
    return leaders

def move_trust(leaders):
    global food, trust
    defence = [[0] * N for _ in range(N)]

    re_leader=[]
    for l in leaders:
        t_food=food[l[1]][l[2]]
        n_one=bin(t_food).count('1')#1의 갯수
        heapq.heappush(re_leader,(n_one,l[0],l[1],l[2]))

    while re_leader:
        leader=heapq.heappop(re_leader)
        leader_r, leader_c = leader[2], leader[3]
        leader_trust=trust[leader_r][leader_c]
        ### 전파를 이미 당한 학생이라면 당일에는 전파하지않음,추가 전파 받는 것은 가능
        if defence[leader_r][leader_c] !=1:
            trust[leader_r][leader_c] = 1
            leader_x=leader_trust-1
            leader_food=food[leader_r][leader_c]
            ##대표자 신앙심을 4로 나눈 나머지에 따라 해당 방향으로 전파
            d=leader_trust%4

            if leader_x<=0:
                continue
            r, c = leader_r, leader_c

            ##전파 방향으로 이동하면서 전파시도
            while leader_x>0:
                nr,nc=r+dxs[d],c+dys[d]
                ##전파대상이 전파자와 신봉음식이 다른경우에만 전파 진행(간절함 = 전파자 신앙심-1)
                if 0<=nr and nr<N and 0<=nc and nc<N:
                    if leader_food!=food[nr][nc]:
                        if leader_x>trust[nr][nc]: ### 간절함>전파대상 신앙심 => 강한 전파성공
                            #### 전파 대상은 전파자의 사상과 완전히 동화/전파자 간절함이 전파대상+1만큼 깍임/전파대상의 신앙심 +1
                            food[nr][nc]=leader_food
                            leader_x-= (trust[nr][nc])+1
                            trust[nr][nc] += 1
                            # leader_x-=trust[nr][nc]
                        #### 전파자의 간절함이 0이되면 전파 종료

                        else: ### 간절함<=전파대상 신앙심 => 약한 전파성공
                            #### 전파 대상은 기존에 관심가지고있던 기본음식들과 전파자의 기본음식을 보두합친 음식을 신봉
                            # new=list(food[nr][nc])[:]
                            # for i,ii in enumerate(list(leader_food)):
                            #     if ii=='1':
                            #         new[i]='1'
                            food[nr][nc] |= leader_food
                            #### 전파 대상 신앙심 +간절함/전파자 간절함 0=> 전파 종료
                            trust[nr][nc] += leader_x
                            leader_x=0
                        defence[nr][nc]=1
                    r,c=nr,nc

                ### 격자밖으로 나가거나 간절함이 0이되면 전파 종료
                else:
                    break

for day in range(T):
    #아침
    ##모든 학생 신앙심+1
    for i in range(N):
        for j in range(N):
            trust[i][j]+=1

    #점심
    li_group=gruop()

    #저녁
    ##대표자들이 신앙 전파 =>전파자
    move_trust(li_group)

    #신앙심 총합 출력
    total_trust=sum_trust()
    for t in total_trust:
        print(t, end=' ')
    print()