n=int(input())
li=list(map(int,input().split()))
cnt=0
while len(li)!=0:
    print(li)
    maxvalue=li[0]
    if maxvalue == 0:
        cnt=-1
        break
    cnt+=1
    if maxvalue>len(li):
        break
    elif maxvalue==1:
        li=li[1:]
    else:
        l=li[1:maxvalue+1]
        li=li[l.index(max(l))+1:]
print(cnt)