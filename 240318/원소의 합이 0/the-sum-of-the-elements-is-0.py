n=int(input())
li=[]
for i in range(4):
    li.append(list(map(int, input().split())))

d1=dict()
for j in list(set(li[0])):
    d1[j]=1

d2=dict()
for j in list(set(li[1])):
    d2[j]=1

d3=dict()
for j in list(set(li[2])):
    d3[j]=1
d4=dict()
for j in list(set(li[3])):
    d4[j]=1

answer=0
for i in d1:
    for j in d2:
        for k in d3:
            s=i+j+k
            if -s in d4:
                answer+=1
print(answer)