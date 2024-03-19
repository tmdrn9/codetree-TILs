n,k=map(int,input().split())

li=[]
d=dict()
person=list(range(1,n+1))

for i in range(n):
    d[i+1]={person[i]}
for i in range(k):
    li.append(list(map(int,input().split())))

for i in range(3*k):
    change=li[i%k]
    temp=person[change[0]-1]
    person[change[0]-1]=person[change[1]-1]
    person[change[1]-1]=temp
    if person==list(range(1,n+1)):
        break
    d[person[change[0]-1]].add(change[0])
    d[person[change[1]-1]].add(change[1])
    # print(d)

for i in d.values():
    print(len(i))