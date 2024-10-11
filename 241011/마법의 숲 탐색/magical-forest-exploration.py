from collections import deque

#북 동 남 서
dxs,dys=[-1,0,1,0],[0,1,0,-1]
ans=0
#입력
R,C,K=map(int,input().split())
grid=[[0]*C for _ in range(R+3)]
unit_c=[[0,0] for _ in range(K+1)]
unit_d=[0]*(K+1)
def move_car(idx,c,d):
    global grid
    r=1
    while True:
        # [0]남쪽으로 내려갈수있는지 확인
        # [1]가능)남쪽으로 한칸 내려옴
        # [1-1]불가능) 서쪽방향으로 회전하며 이동해서 내려감+출구는 반시계방향으로 이동
        # [1-1-1]불가능) 동쪽방향으로 회전해 이동해 내려감+출구는 시계방향으로 이동
        bye=True
        if r==R+1:
            break
        if check(idx, r,c,2):
            grid[r-1][c],grid[r][c+1],grid[r][c-1]=0,0,0
            grid[r+1][c+1],grid[r+1][c-1],grid[r+2][c]=idx,idx,idx
            r+=1
            bye=False
        elif 2<=c and check(idx,r,c,3) and check(idx,r,c-1,2):
            grid[r-1][c],grid[r][c+1],grid[r+1][c]=0,0,0
            grid[r - 1][c - 1],grid[r][c - 2],grid[r + 1][c - 1]=idx,idx,idx
            c-=1
            grid[r - 1][c], grid[r][c + 1], grid[r][c - 1] = 0, 0, 0
            grid[r + 1][c + 1], grid[r + 1][c - 1], grid[r + 2][c] = idx, idx, idx
            r += 1
            d= (d+3)%4
            bye = False
        elif c<=C-3 and check(idx,r,c,1) and check(idx,r,c+1,2):
            grid[r - 1][c], grid[r][c - 1], grid[r + 1][c] = 0, 0, 0
            grid[r - 1][c + 1], grid[r][c + 2], grid[r + 1][c + 1] = idx, idx, idx
            c+=1
            grid[r - 1][c], grid[r][c + 1], grid[r][c - 1] = 0, 0, 0
            grid[r + 1][c + 1], grid[r + 1][c - 1], grid[r + 2][c] = idx, idx, idx
            r += 1
            d = (d + 1) % 4
            bye = False
        if bye:
            break
    return r,c,d



def move_unit(r,c,d):
    # [2]가장 남쪽에 도달해 더이상 이동할 수 없으면 정령은 골렘 내에서 상하좌우 인접한 칸으로 이동이 가능
    # [2-1]골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 다른 골렘으로 이동할 수 있음
    # [3]모든 칸 중 가장 남쪽의 칸으로 이동하고 이동을 완전히 종료
    result=0
    visited=[[0]*C for _ in range(R+3)]
    if r==R+1:
        return R+2
    else:
        if check(0,r,c,d):
            return r+1
        else:
            final=False
            q=deque([])
            er, ec = r + dxs[d], c + dys[d]
            q.append((er,ec))
            visited[er][ec]=1
            while q:
                tr,tc=q.popleft()
                for dx,dy in zip(dxs,dys):
                    nr,nc=tr+dx,tc+dy
                    if 0<=nc<C and 0<=nr<R+3 and grid[nr][nc]!=0 and grid[nr][nc]!=grid[er][ec]:
                        q.append((nr,nc))
                        visited[nr][nc]=1
                        if nr==8:
                            final=True
                            break
                if final:
                    break
    if final:
        return R+2
    else:
        for rr in range(R+2,-1,-1):
            if 1 in visited[rr]:
                result=rr
                break
        return max(result,r+1)


#남:2
def check(idx,x,y,d):
    if d==1:
        return (grid[x-1][y+1]==0 or grid[x-1][y+1]==idx)and (grid[x][y+2]==0 or grid[x][y+2]==idx) and (grid[x+1][y+1]==0 or grid[x+1][y+1]==idx)
    elif d==2:
        return (grid[x+1][y-1]==0 or grid[x+1][y-1]==idx) and (grid[x+1][y+1]==0 or grid[x+1][y+1]==idx) and (grid[x+2][y]==0 or grid[x+2][y]==idx)
    elif d==3:
        return (grid[x-1][y-1]==0 or grid[x-1][y-1]==idx) and (grid[x][y-2]==0 or grid[x][y-2]==idx) and (grid[x+1][y-1]==0 or grid[x+1][y-1]==idx)

for i in range(1,K+1):
    ci,di=map(int,input().split())
    ci-=1
    unit_c[i]=[1,ci]
    unit_d[i]=di

    grid[0][ci]=i
    grid[1][ci-1:ci+2]=[i]*3
    grid[2][ci]=i
    # 골렘탐색
    r,c,d=move_car(i,ci,di)

    # 정령이동
    if r<=2:
        grid = [[0] * C for _ in range(R + 3)]
        continue
    unit_c[i] = [r, c]
    unit_d[i] = d
    point=move_unit(r,c,d)
    ans+=(point-2)





#골렘의 중앙을 제외한 4칸 중 한 칸은 골렘의 출구
#정령은 어떤 방향에서든 골렘에 탑승할 수 있지만,내릴 때에는 출구를 통해서만 내릴 수 있습니다.


#i번째로 탐색하는 골렘은 가장 북쪽에서 시작해서 중앙이 c열인 위치에서 내려오고 초기의 출구는 d방향
#정령은 어떤 방향에서든 골렘에 탑승할 수 있지만 골렘에서 내릴 때에는 정해진 출구를 통해서만 내릴 수 있습니다.





#골렘이 최대한 남쪽으로 이동했지만 골렘의 몸 일부가 여전히 숲을 벗어난 상태라면, 해당 골렘을 포함해 숲에 위치한 모든 골렘들은 숲을 빠져나간 뒤 다음 골렘부터 새롭게 숲의 탐색을 시작합니다. 단, 이 경우에는 정령이 도달하는 최종 위치를 답에 포함시키지 않습니다.
##=>다 탈출시키고 초기화하고 다시시작


#출력
#정령의 최종 위치의 행 번호의 합을 구해야 하기에 각 정령이 도달하게 되는 최종 위치를 누적
#숲이 다시 텅 비게 돼도 행의 총합은 누적되는 것에 유의합니다.
print(ans)