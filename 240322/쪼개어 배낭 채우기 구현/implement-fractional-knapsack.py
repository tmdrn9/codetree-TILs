n,m=map(int,input().split())
li=sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda x:x[1]/x[0],reverse=True)
answer=0
remain=m
for i in li:
    if i[0]>=remain:
        answer+=(i[1]/i[0])*remain
        break
    else:
        answer+=i[1]
        remain-=i[0]


print(f'{round(answer,4):.3f}')