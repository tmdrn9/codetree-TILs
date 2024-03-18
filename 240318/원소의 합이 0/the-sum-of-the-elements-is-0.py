n=int(input())
li=[]
for i in range(4):
    li.append(list(map(int, input().split())))
li2=[]
for i in zip(*li):
    li2.append(list(i))

d1=dict()
d2=dict()
d3=dict()
d4=dict()

for j in li2:
    d1[j[0]]=1 if j[0] not in d1 else d1[j[0]]+1
    d2[j[1]]=1 if j[1] not in d2 else d2[j[1]]+1
    d3[j[2]]=1 if j[1] not in d3 else d3[j[0]]+1
    d4[j[3]]=1 if j[2] not in d4 else d4[j[0]]+1


answer=0
for i in d1:
    for j in d2:
        for k in d3:
            s=i+j+k
            if -s in d4:
                answer+=(d1[i]*d2[j]*d3[k]*d4[-s])
print(answer)