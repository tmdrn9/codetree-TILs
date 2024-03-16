import itertools
n,k=map(int,input().split())
li=list(map(int,input().split()))

cnt=0
for i in li:
    if k-i in li:
        cnt+=1

print(int(cnt/2))