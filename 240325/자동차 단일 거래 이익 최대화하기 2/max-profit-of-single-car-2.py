n=int(input())
li=list(map(int,input().split()))
answer=0
temp=li[0]
for i in range(1,len(li)):
    cha=li[i]-temp

    if cha>answer:
        answer=cha
    elif cha>0:
        continue
    else:
        temp=li[i]
print(answer)