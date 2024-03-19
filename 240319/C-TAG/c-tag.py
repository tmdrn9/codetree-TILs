from itertools import combinations

n,m=map(int,input().split())
a=[input() for _ in range(n)]
b=[input() for _ in range(n)]
answer=0
for i in combinations(list(range(m)),3):
    s1=set()
    s2=set()
    for j in range(n):
        s1.add(a[j][i[0]]+a[j][i[1]]+a[j][i[2]])
        s2.add(b[j][i[0]]+b[j][i[1]]+b[j][i[2]])
    if len(s1.intersection(s2))==0:
        answer+=1
print(answer)