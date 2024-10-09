dxs,dys=[-1,0,1,0],[0,1,0,-1]
#입력
n, m, h, k=map(int,input().split())

#술래 특) 격자 정중앙에서 시작
mx,my,md=n//2,n//2,0

unit_grid=[[[] for _ in range(n)] for _ in range(n)]

unit={}
unit_k={}
for i in range(1,m+1):
    x,y,d=map(int, input().split())
    # 좌우로 움직이는 사람은 항상 오른쪽을 보고 시작
    # 상하로 움직이는 사람은 항상 아래쪽을 보고 시작
    unit[i]=(x-1,y-1)
    unit_k[i]=d
    unit_grid[x-1][y-1].append(i)

grid=[[0]*n for _ in range(n)]
for i in range(h):
    x, y = map(int, input().split())
    grid[x-1][y-1]=1

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

od={0:2,1:3,2:0,3:1}
point=0
def dist(x,y,x1,y1):
    return abs(x-x1)+abs(y-y1)

mdist=1
move_count=0
tdist=0
tonado=True
#main
for turn in range(1,k+1):
    #1도망자 움직임
    temp=[row[:] for row in unit_grid]

    for idx in unit:
        ux,uy=unit[idx]
        ud=unit_k[idx]
        ##술래와의 거리가 3 이하인 도망자만 움직임
        if dist(mx,my,ux,uy)<=3:
            ##바라보고있는 방향으로 움직임
            nx,ny=ux+dxs[ud],uy+dys[ud]
            if not in_range(nx,ny) and (nx,ny)!=(mx,my):
                ###격자 벗어나면)방향틀어주고 한칸이동 단, 술래없는 경우
                ud=od[ud]
                temp[ux][uy].remove(idx)
                nx, ny = ux + dxs[ud], uy + dys[ud]
                temp[nx][ny].append(idx)
                unit[idx]=(nx, ny)
                unit_k[idx]=ud
            else:
                ###안벗어나면)술래가 있는 없다면 이동(나무 유무 상관 없음)
                if (nx,ny)!=(mx,my):
                    temp[ux][uy].remove(idx)
                    temp[nx][ny].append(idx)
                    unit[idx] = (nx, ny)

    unit_grid=temp

    #2 술래 움직임
    ##2-1달팽이 모양으로 움직임
    if tonado:
        mx, my = mx + dxs[md], my + dys[md]
        tdist+=1

        if tdist==mdist:
            tdist=0
            md = (md + 1) % 4
            move_count += 1
            if move_count==2:
                mdist+=1
                move_count=0
        if (mx,my)==(0,0):
            tonado=False
            md=2
            tdist=1
            move_count=1
    else: #상우하좌 하우상좌
        mx, my = mx + dxs[md], my + dys[md]
        tdist += 1
        if tdist==mdist:
            tdist = 0
            md = (md + 3) % 4
            move_count += 1
            if move_count==2:
                mdist-=1
                move_count=0
        if (mx,my)==(n//2,n//2):
            tonado = True
            md = 0
            tdist = 0
            move_count = 0
            mdist=1
    #2-2 바라보고 있는 방향을 기준으로 현재칸을 포함해 3칸내에 있는 도망자 잡음.
    t_point=0
    for c in range(3):
        tx,ty=mx+(dxs[md]*c),my+(dys[md]*c)
        ##나무가 있는 칸의 도망자는 못잡음
        if in_range(tx,ty) and grid[tx][ty]==0:
            n_unit=len(unit_grid[tx][ty])
            if n_unit>0:
                t_point+=n_unit
                units=unit_grid[tx][ty]
                while units:
                    u_idx=units.pop(0)
                    unit.pop(u_idx)
                    unit_k.pop(u_idx)
    ##턴*잡은 도망자수만큼 점수 획득
    point+=(t_point*turn)


#출력
print(point)