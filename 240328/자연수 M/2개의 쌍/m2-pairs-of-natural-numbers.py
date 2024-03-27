from sortedcontainers import SortedDict
n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
li=sorted(li,key=lambda x:x[1])

print(li[0][1]+li[-1][1])