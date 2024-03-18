n=int(input())
li=[]
for i in range(4):
    li.append(list(map(int, input().split())))

d1=dict()
for j in li[0]:
    if j in d1:
        d1[j]+=1
    else:
        d1[j]=1

d2=dict()
for j in li[1]:
    if j in d2:
        d2[j]+=1
    else:
        d2[j]=1

d3=dict()
for j in li[2]:
    if j in d3:
        d3[j]+=1
    else:
        d3[j]=1
d4=dict()
for j in li[3]:
    if j in d4:
        d4[j]+=1
    else:
        d4[j]=1

answer=0
for i in d1:
    for j in d2:
        for k in d3:
            s=i+j+k
            if -s in d4:
                
                answer+=(d1[i]*d2[j]*d3[k]*d4[-s])
print(answer)