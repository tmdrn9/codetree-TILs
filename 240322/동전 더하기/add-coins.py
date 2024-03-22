n,k=map(int,input().split())
li=[int(input()) for _ in range(n)]
answer=0
for i in range(len(li)-1,-1,-1):
    c=li[i]
    while c<=k:
        k-=c
        answer+=1
        if k==0:
            break
print(answer)