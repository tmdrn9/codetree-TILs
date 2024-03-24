n=int(input())
li=list(map(int,input().split()))
answer=0
while len(li)>2:
    li=sorted(li)
    a,b=li[0],li[1]
    temp=a+b
    li=li[2:]
    answer+=temp
    li.append(temp)
print(answer+sum(li))