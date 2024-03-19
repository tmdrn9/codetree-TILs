n,k=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(k)]

d=dict()
person=list(range(1,n+1))

for i in range(1,n+1):
    d[i]={i}
# s = [set() for _ in range(n + 1)]


for i in range(3*k):
    change=li[i%k]
    person[change[0]-1], person[change[1]-1] = person[change[1]-1], person[change[0]-1]
    # s[]
    d[person[change[0]-1]].add(change[0])
    d[person[change[1]-1]].add(change[1])

for i in d.values():
    print(len(i))