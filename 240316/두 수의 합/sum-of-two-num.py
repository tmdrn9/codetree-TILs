import itertools
n,k=map(int,input().split())
li=list(map(int,input().split()))
d={li[i]:i+1 for i in range(n)}

cnt=0
for i in li:
    if k-i in d:
        cnt+=1

print(int(cnt/2))