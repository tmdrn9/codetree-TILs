n,m=map(int,input().split())
li=list(map(int,input().split()))
q=list(map(int,input().split()))
def lower_bound(t):
    left,right=0,n-1
    minIdx=n
    while left<=right:
        mid=(left+right)//2
        if li[mid]>=t:
            minIdx=min(minIdx,mid)
            right=mid-1
        else:
            left=mid+1
    return minIdx
def upper_bound(t):
    left,right=0,n-1
    minIdx=n
    while left<=right:
        mid=(left+right)//2
        if li[mid]>t:
            minIdx=min(minIdx,mid)
            right=mid-1
        else:
            left=mid+1
    return minIdx

for i in q:
    lower=lower_bound(i)
    upper=upper_bound(i)
    answer= lower+1 if lower!=upper else -1
    print(answer)