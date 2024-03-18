s=list(input())
u=set(s)
answer='None'
for i in u:
    if s.count(i)==1:
        answer=i
        break
print(answer)