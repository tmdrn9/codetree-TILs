n,k=map(int,input().split())

li=[]
d=dict()
person=list(range(1,n+1))
for i in range(n):
    d[i]={person[i]}
for i in range(k):
    li.append(list(map(int,input().split())))

for i in range(3*k):
    change=li[i%k]
    temp=person[change[0]-1]
    person[change[0]-1]=person[change[1]-1]
    person[change[1]-1]=temp
    if person==list(range(1,n+1)):
        break
    d[change[0]-1].add(person[change[0]-1])
    d[change[1]-1].add(person[change[1]-1])

answer=[]
for i in d.values():
    answer.extend(list(i))
for i in range(n):
    print(answer.count(i+1))