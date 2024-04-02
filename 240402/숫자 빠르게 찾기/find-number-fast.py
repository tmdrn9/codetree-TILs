n,m=map(int,input().split())
n_li=list(map(int,input().split()))
for _ in range(m):
    left,right=0,n-1
    ok=True
    target=int(input())
    while left<=right:
        mid=(left+right)//2
        if n_li[mid]==target:
            ok=False
            print(mid+1)
            break
        elif n_li[mid]>target:
            right=mid-1
        else:
            left=mid+1
    if ok:
        print(-1)