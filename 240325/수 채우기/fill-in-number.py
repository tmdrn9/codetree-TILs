n=int(input())
n5,remain=divmod(n,5)
n2,remain2=divmod(remain,2)
answer= n5+n2 if remain2==0 else -1
print(answer)