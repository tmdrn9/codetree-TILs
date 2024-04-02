n,m=map(int,input().split())
li=list(map(int,input().split()))

def lower_bound(target): #target이 처음으로 나오는 위치
    left,right=0,n-1
    minIdx=n
    while left<=right:
        mid=(left+right)//2
        if li[mid]>=target:
            minIdx=min(minIdx,mid)
            right=mid-1
        else:
            left=mid+1
    return minIdx

def upper_bound(target): #target을 초과하는 값이 처음으로 나오는 위치
    left,right=0,n-1
    minIdx=n
    while left<=right:
        mid=(left+right)//2
        if li[mid]>target:
            minIdx=min(minIdx,mid)
            right=mid-1
        else:
            left=mid+1
    return minIdx


for _ in range(m):
    t=int(input())
    c=upper_bound(t)-lower_bound(t)
    print(c)