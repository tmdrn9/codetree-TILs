n,k=map(int,input().split())
pixed_sum=[0]*n
li=list(map(int,input().split()))
pixed_sum[0]=li[0]
m=0
for i in range(n-1):
    pixed_sum[i]=pixed_sum[i-1]+li[i]
for i in range(k-1,n):
    if i-k+1==0:
        if pixed_sum[i]>m:
            m=pixed_sum[i]
    else:
        temp=pixed_sum[i]-pixed_sum[i-k]
        if temp>m:
            m=temp
print(m)