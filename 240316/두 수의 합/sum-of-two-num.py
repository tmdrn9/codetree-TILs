import itertools
n,k=map(int,input().split())
li=list(map(int,input().split()))
cnt=0
for i in itertools.combinations(li,2):
    if sum(i)==k:
        cnt+=1

print(cnt)