dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
gun = {}
for i in range(n):
    for j in range(n):
        if grid[i][j] > 0:
            gun[(i, j)] = [0, grid[i][j]]
        else:
            gun[(i, j)] = [0]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


player = [[0, 0] for _ in range(m)]
player_d = [0] * m
player_s = [0] * m
player_g = [0] * m
for i in range(m):
    x, y, d, s = map(int, input().split())
    player[i] = [x - 1, y - 1]
    player_d[i] = d
    player_s[i] = s

get_point = [0] * m


def change_gun(p, nx, ny):
    gg = gun[(nx, ny)]
    tg = max(gg)
    if player_g[p] == 0:
        player_g[p] = tg
        gg.remove(tg)
        gun[(nx, ny)] = gg
    else:
        if player_g[p] < tg:
            gg.append(player_g[p])
            player_g[p] = tg
            gg.remove(tg)
            gun[(nx, ny)] = gg


def after_fight(winner, loser, point, x, y):
    ###이긴사람:각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득
    ###승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓습니다.
    get_point[winner] += point
    if len(gun[(x, y)]) > 1:
        change_gun(winner, x, y)

    ###진 사람: 본인이 가지고 있는 총을 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동
    if player_g[loser] != 0:
        gs = gun[(x, y)]
        gs.append(player_g[loser])
        gun[(x, y)] = gs
        player_g[loser] = 0

    lx, ly = player[loser][0], player[loser][1]
    ld = player_d[loser]
    nlx, nly = lx + dxs[ld], ly + dys[ld]
    ###이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동
    if not in_range(nlx, nly) or [nlx, nly] in player:
        for _ in range(4):
            ld = (ld + 1) % 4
            player_d[loser] = ld
            nlx, nly = lx + dxs[ld], ly + dys[ld]
            if in_range(nlx, nly) and [nlx, nly] not in player:
                break
    ###해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려 놓습니다.
    if len(gun[(lx, ly)]) > 1:
        change_gun(loser, nlx, nly)
    player[loser] = [nlx, nly]


for turn in range(k):
    # 1
    ##첫 번째 플레이어부터 순차적으로 본인이 방향대로 한 칸 이동
    ##격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼 이동
    for p in range(m):
        x, y = player[p][0], player[p][1]
        d = player_d[p]
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny):
            if d == 0:
                d = 2
            elif d == 1:
                d = 3
            elif d == 2:
                d = 0
            else:
                d = 1
            player_d[p] = d
            nx, ny = x + dxs[d], y + dys[d]

        # 이동한 곳에 플레이어 있는지 확인
        if [nx, ny] in player:
            p_power = player_s[p] + player_g[p]
            p2 = player.index([nx, ny])
            p2_power = player_s[p2] + player_g[p2]
            player[p] = [nx, ny]

            ###플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교(같은경우 초기 능력치 큰사람 이김)
            #이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓습니다.

            if p_power > p2_power:
                after_fight(p, p2, abs(p_power - p2_power), nx, ny)
                if len(gun[(nx, ny)]) > 1:
                    change_gun(p, nx, ny)
            elif p_power < p2_power:
                after_fight(p2, p, abs(p_power - p2_power), nx, ny)
                if len(gun[(nx, ny)]) > 1:
                    change_gun(p2, nx, ny)
            else:
                if player_s[p] > player_s[p2]:
                    after_fight(p, p2, 0, nx, ny)
                    if len(gun[(nx, ny)]) > 1:
                        change_gun(p, nx, ny)
                else:
                    after_fight(p2, p, 0, nx, ny)
                    if len(gun[(nx, ny)]) > 1:
                        change_gun(p2, nx, ny)
            

        else:
            ##해당 칸에 총이 있으면 가지고있는 총과 비교해서 공격력 센 총 획득 후 남은건 자리에 놓기
            if len(gun[(nx, ny)]) > 1:
                change_gun(p, nx, ny)
            player[p] = [nx, ny]

# 출력
for i in get_point:
    print(i, end=' ')