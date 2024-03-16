n,m=map(int,input().split())
d=dict()
for i in range(n):
    t=input()
    d[t]=i+1
d_key=list(d.keys())
for j in range(m):
    g=input()
    if g.isdigit():
        print(d_key[int(g)-1])
    else:
        print(d[g])