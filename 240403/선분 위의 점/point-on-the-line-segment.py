n,m=map(int,input().split())
n_li=sorted(list(map(int,input().split())))

def lower_bound(li,target): #target이 처음으로 나오는 위치
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

def upper_bound(li,target): #target을 초과하는 값이 처음으로 나오는 위치
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

def twoFind(line,t):
    left,right=0,n-1
    if t[left]>line[1] or t[right]<line[0]:
        return 0
    else:
        low=lower_bound(n_li,line[0])
        up=upper_bound(n_li,line[1])
        return up-low
        

for _ in range(m):
    line=tuple(map(int,input().split()))
    print(twoFind(line,n_li))