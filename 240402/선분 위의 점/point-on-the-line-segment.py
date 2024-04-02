n,m=map(int,input().split())
li=list(map(int,input().split()))
def twoFind(line,t):
    left,right=line[0],line[1]
    if t>right or t<left:
        return 0
    else:
        return 1
for _ in range(m):
    line=tuple(map(int,input().split()))
    answer=0
    for i in li:
        answer+=twoFind(line,i)
    print(answer)