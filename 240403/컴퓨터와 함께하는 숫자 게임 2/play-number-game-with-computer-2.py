import math
m=int(input())
a,b=map(int,input().split())

max_cnt=-1
min_cnt=math.inf
for target in range(a,b+1):
    cnt=0
    left,right=1,m
    while left<=right:
        cnt+=1
        mid=(left+right)//2
        if mid==target:
            break
        elif mid>target:
            right=mid-1
        else:
            left=mid+1
    max_cnt=max(max_cnt,cnt)
    min_cnt=min(min_cnt,cnt)
print(min_cnt, max_cnt)