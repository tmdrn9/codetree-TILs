n=int(input())
li=list(map(int,input().split()))
ans,s=li[0],li[0]
for i in li[1:]:
    s+=i
    if s<0:
        s=0
        continue
    if ans<s:
        ans=s
print(ans)