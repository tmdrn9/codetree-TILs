n,m=map(int,input().split())
d=dict()
n_li=list(map(int,input().split()))

for i in n_li:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

m_li=list(map(int,input().split()))
answer=[]
for a in m_li:
    if a in d:
        answer.append(str(d[a]))
    else:
        answer.append('0')
print(' '.join(answer))