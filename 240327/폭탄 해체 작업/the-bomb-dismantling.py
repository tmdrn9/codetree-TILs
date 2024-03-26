n=int(input())
boom=[tuple(map(int,input().split()))for _ in range(n)]
answer=0
now=0
boom=sorted(boom,reverse=True)
boom=sorted(boom,key=lambda x:x[1])
for i in boom:
    if now<i[1]:
        answer+=i[0]        
    now+=1
print(answer)