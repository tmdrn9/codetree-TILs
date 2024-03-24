n=int(input())
li=list(map(int,input().split()))
answer=0
while len(li)>2:
    li=sorted(li)
    temp=li[0]+li[1]
    li.remove(li[0])
    li.remove(li[1])
    answer+=temp
    li.append(temp)
print(answer+sum(li))