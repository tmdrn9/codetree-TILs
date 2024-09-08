n=int(input())
li=list(map(int,input().split()))
ans,s=li[0],li[0]
for i in li[1:]:
    if s<0:
        s=i
        continue
    else:
        s+=i
    if ans<s:
        ans=s
print(ans)