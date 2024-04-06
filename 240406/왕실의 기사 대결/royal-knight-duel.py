l,n,q=map(int,input().split())
#1:함정, 2:벽
grid=[list(map(int,input().split())) for _ in range(l)]

# (r,c,h,w,k)/r,c:초기위치/hw세로가로/k체력
people=[(-1,-1,-1,-1,-1)]
for _ in range(n):
    people.append(list(map(int,input().split())))

people_grid=[[0]*l for _ in range(l)]

for n,(r,c,h,w,k) in enumerate(people[1:]):
    people[n+1][0]-=1
    people[n+1][1]-=1
    for i in range(r-1,r-1+h):
        for j in range(c-1,c-1+w):
            people_grid[i][j]=n+1

#i:기사 번호, d:방향으로 1칸이동
#d 0:위,1:오른,2:아래,3:왼
king=[list(map(int,input().split())) for _ in range(q)]
DX,DY=[-1,0,1,0],[0,1,0,-1]

def in_range(x,y):
    return 0<=x and x<l and 0<=y and y<l and grid[x][y]!=2

def surround(n,d):
    global other,ok
    x,y,h,w,_=people[n]
    for i in range(h):
        for j in range(w):
            new_x=x+i+DX[d]
            new_y=y+j+DY[d]
            if not in_range(new_x,new_y):
                ok=True
                return 
            else:
                if people_grid[new_x][new_y]==n or people_grid[new_x][new_y]==0:
                    continue
                other.add(people_grid[new_x][new_y])
                surround(people_grid[new_x][new_y],d)
def damage(i):
    dmg=0
    r,c,_,_,k=people[i]
    if grid[r][c]==1:
        people[i][4]-=1
        dmg+=1
    return dmg,people[i][4]

def move(i,d):
    r,c,h,w,k=people[i]
    for i in range(h):
        for j in range(w):
            people_grid[r+i][c+j]=0
            people_grid[r+i+DX[d]][c+j+DY[d]]=i

    people[i]=[r+DX[d],c+DY[d],h,w,k]

def remove(i):
    r,c,h,w,k=people[i]
    for i in range(h):
        for j in range(w):
            people_grid[r+i][c+j]=0

answer=0
rm_list=[]
for i,d in king:
    if i in rm_list:
        continue
    other=set([i])
    ok=False
    surround(i,d)

    if ok:
        continue
    for n in list(other)[::-1]:
        move(n,d)
        d,temp=damage(n)
        answer+=d
        if temp==0:
            remove(i)

print(answer)