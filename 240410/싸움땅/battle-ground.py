DX, DY = [-1, 0, 1, 0], [0, 1, 0, -1]
def in_range(x,y):
    return 0<=x<N and 0<=y<N
# 이동 함수, 대결함수
def move_player(i):
    x, y=player[i]
    d=player_go[i]
    nx,ny=x+DX[d],y+DY[d]
    # 해당 방향으로 나갈 때 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼 이동
    if not in_range(nx,ny):
        new_d=(d+2)%4
        player_go[i]=new_d
        nx, ny = x+DX[new_d],y+DY[new_d]
    player[i] = [nx, ny]
    return nx,ny

def fight(i,j,nx,ny):
    i_power=player_init[i]+player_gun[i]
    j_power=player_init[j]+player_gun[j]
    score=abs(i_power-j_power)
    if i_power>j_power:
        winner=i
        loser=j
    elif i_power==j_power:
    ## 만일 이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리
        winner= i if player_init[i]>player_init[j] else j
        loser= j if winner==i else i
    else:
        winner = j
        loser = i
    ### 이긴플레이어:각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득
    player_score[winner]+=score
    ### 진 플레이어: 본인이 가지고 있는 총을 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동
    grid[nx][ny]=player_gun[loser]
    player_gun[loser]=0
    move_player(loser)
    ### 이긴 플레이어: 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓습니다.
    change_gun(winner,nx,ny)


def change_gun(i,nx,ny):
    if player_gun[i] < grid[nx][ny]:
        player_gun[i], grid[nx][ny] = grid[nx][ny], player_gun[i]


N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
player = [[-1, -1] for _ in range(M + 1)]  # 4는 총 공격력
player_go = [-1] * (M + 1)
player_init = [-1] * (M + 1)
player_gun = [0] * (M + 1)
player_score = [0] * (M + 1)
for i in range(1, M + 1):
    x, y, d, s = map(int, input().split())
    player[i] = [x-1, y-1]
    player_go[i] = d
    player_init[i] = s
#################################
for turn in range(1,K+1):
    # 1-1 첫 번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동
    for i in range(1,M+1):
        nx,ny=move_player(i)
        ##총이 있는 경우, 해당 플레이어는 총을 획득합니다.
        ###플레이어가 이미 총을 가지고 있는 경우에는 놓여있는 총들과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둡니다.
        if grid[nx][ny]>0:
            #더 쎈 총을 획득하거나 그대로 있거나
            change_gun(i,nx,ny)
        elif [nx,ny] in player:
            hi=player.index([nx,ny])
            fight(i,hi,nx,ny)
for i in range(1, M + 1):
    print(player_score[i],end=' ')