def mov(li,n):
    for i in range(1,n+1):
        d,t=input().split()
        if d=='R':
            li.extend(list(range(li[len(li)-1]+1,li[len(li)-1]+int(t)+1)))
        else:
            li.extend(list(range(li[len(li)-1]-1,li[len(li)-1]-int(t)-1,-1)))

n,m=map(int,input().split())
a=[0]
b=[0]
mov(a,n)
mov(b,m)
ans=-1
for i in range(1,min(len(a),len(b))):
    if a[i]==b[i]:
        ans=i
        break
print(ans)