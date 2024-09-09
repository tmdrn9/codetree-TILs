n,m=map(int,input().split())
a=[0]*(1000000)
b=[0]*(1000000)

def mov(n,ab):
    now=1
    for _ in range(1,n+1):
        t,d=input().split()
        if d =='R':
            for j in range(int(t)):
                ab[now]=ab[now-1]+1
                now+=1
        else:
            for j in range(int(t)):
                ab[now]=ab[now-1]-1
                now+=1
    ab[now]=1000001

mov(n,a)
mov(m,b)

a_end=a.index(1000001)
b_end=b.index(1000001)

end=-1
if a_end>b_end:
    end=a_end
    b[b_end:a_end]=[b[b_end-1]]*(a_end-b_end)
elif b_end>a_end:
    end=b_end
    a[a_end:b_end]=[a[a_end-1]]*(b_end-a_end)
else:
    end=a_end

ans=0
for i in range(1,end):
    if a[i]==b[i] and a[i-1]!=b[i-1]:
        ans+=1

print(ans)