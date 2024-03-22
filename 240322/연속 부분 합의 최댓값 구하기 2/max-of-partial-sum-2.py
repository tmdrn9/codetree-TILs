n=int(input())
li=list(map(int,input().split()))
pixed_sum=[0]*len(li)
pixed_sum[0]=li[0]
m=li[0]
if all([i<0 for i in li]):
    print(max(li))
else:
    for i,c in enumerate(li[1:]):
        pixed_sum[i]=pixed_sum[i-1]+c
        if m<pixed_sum[i]:
            m=pixed_sum[i]
        if pixed_sum[i]<0:
            pixed_sum[i]=0
    print(m)