n,m=map(int,input().split())
maxx=1000000
a=[0]*(maxx+1)
b=[0]*(maxx+1)

def setting_ab(n,ab):
    ind=1
    for _ in range(n):
        v,t=map(int,input().split())
        for _ in range(t):
            ab[ind]=ab[ind-1]+v
            ind+=1
setting_ab(n,a)
setting_ab(m,b)

now, ans= 0,0 
time_=1
#a가 선두일때 now=1/ b가 선두일때 now=2
while a[time_]!=0:
    if a[time_]>b[time_]:
        if now==2:
            ans+=1
        now=1
    elif a[time_]<b[time_]:
        if now==1:
            ans+=1
        now=2
    time_+=1
print(ans)