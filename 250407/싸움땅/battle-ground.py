#시작 8:44
#설계끝 8:56
#코딩끝
# import sys
# sys.stdin=open('input.txt')
# input=sys.stdin.readline

dxs,dys=[-1,0,1,0],[0,1,0,-1]
N,M,K= map(int,input().split())

grid=[[]*N for _ in range(N)]
for i in range(N):
    row=map(int,input().split())
    for j,g in enumerate(row):
        if g!=0:
            grid[i].append([g])
        else:
            grid[i].append([])

player=[]
player_d=[0]*M
player_init=[0]*M
player_gun=[0]*M
player_point=[0]*M
for i in range(M):
    x,y,d,s=map(int,input().split())
    player.append((x-1,y-1))
    player_d[i]=d
    player_init[i]=s

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def check_gun(x,y,i):
    ## 있는 경우 플레이어가 총이 없다면 총 획득, 있다면 공격력이 쎈 총 획득하고 나머지 총들은 내려놓기

    if grid[x][y]: #총이 그자리에 있다면
        new_gun = max(grid[x][y])
        if player_gun[i]==0:
            player_gun[i]=new_gun
            grid[x][y].remove(new_gun)
        else:
            if new_gun>player_gun[i]:
                grid[x][y].remove(new_gun)
                grid[x][y].append(player_gun[i])
                player_gun[i]=new_gun

def fight(i,j):
    scorei = player_init[i]+player_gun[i]
    scorej = player_init[j] + player_gun[j]
    ##플레이어의 초기 능력치와 가지고있는 총의 공격력의 합을 비교해서 더 큰 플레이어 승리
    if scorei>scorej:
        winner, loser=i,j
    elif scorej>scorei:
        winner, loser = j,i
    else:##만일 수치가 같은경우 초기능력치가 높은 플레이어 승리
        if player_init[i]>player_init[j]:
            winner, loser = i, j
        else:
            winner, loser = j, i
    ##이긴 플레이어는 각플레이어의 초기능력치와 가지고있는 공격력의 합 차이만큼 포인트 획득
    player_point[winner]+=abs(scorei-scorej)
    return winner,loser

for turn in range(K):
    #1-1 모든 플레이어가 순차적으로 향하고있는방향대로 한칸씩 이동
    for i in range(M):
        x,y=player[i]
        d = player_d[i]
        nx,ny=x+dxs[d],y+dys[d]
        if not in_range(nx,ny): ## 격자에서 벗어나는경우 정반대 방향으로 방향을 바꾸어서 1만큼
            d=(d+2)%4
            player_d[i]=d
            nx, ny = x + dxs[d], y + dys[d]
        player[i] = (nx, ny)
        #2-1 이동한 방향에 플레이어가 없다면 총이 있는지 확인 =>함수화
        if len(set(player))==len(player):
            check_gun(nx,ny,i)
        else:
            for j in range(M):
                if i==j: continue
                if (nx,ny)== player[j]:
                    # 2-2-1 이동한 방향에 플레이어가 있다면 싸움 =>함수
                    winner,loser=fight(i,j)
                    # 2-2-2진 플레이어는 총을 해당 격자에 내려놓고, 원래 방향으로 한칸 이동
                    if player_gun[loser]>0:
                        grid[nx][ny].append(player_gun[loser])
                        player_gun[loser]=0
                    lx,ly=player[loser]
                    ld=player_d[loser]
                    ## 만약 이동하려는 칸에 플레이어가 있거나 격자밖인 경우에는 오른쪽으로 회전하며 빈칸이 보이는 순간 이동
                    for r in range(0,5):
                        nld = (ld + r) % 4
                        nlx, nly = lx + dxs[nld], ly + dys[nld]
                        if in_range(nlx,nly) and (nlx,nly) not in player:
                            player[loser]=(nlx, nly)
                            player_d[loser]=nld
                            ## 만약 이동칸에 총이 있다면 공격력 높은 총을 획득하고 나머지 총들은 내려놓음
                            check_gun(nlx, nly,loser)
                            break
                    # 2-2-3
                    ##이긴 플레이어는 승리한칸에 떨어져있는 총들과 원래 들고있는 총중 가장 공격력이 높은 총을 획득하고 , 나머지 총은 내려놓기
                    check_gun(nx,ny, winner)
                    break

for i in player_point:
    print(i, end=' ')