n,k=map(int,input().split())

li=[]
possible=[]

person=list(range(1,n+1))
possible.append(tuple(person))
for i in range(k):
    li.append(list(map(int,input().split())))

for i in range(3*k):
    change=li[i%k]
    temp=person[change[0]-1]
    person[change[0]-1]=person[change[1]-1]
    person[change[1]-1]=temp
    possible.append(tuple(person))

possible=list(set(possible))

answer=[]
for i in zip(*possible):
    answer.extend(list(set(i)))
for i in range(n):
    print(answer.count(i+1))