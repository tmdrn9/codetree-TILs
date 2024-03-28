n=int(input())
li=[tuple(map(int, input().split())) for _ in range(n)]
li.sort(key=lambda x:x[1])
answer=0
temp=li[0][1]
# print(li)
for i in range(n-1):
    if temp<=li[i+1][0]:
        temp=li[i+1][1]
        continue
    else:
        answer+=1

print(answer)