n=int(input())
li=[input() for _ in range(n)]
d=dict()
answer=''
for i in li:
    t=int(10/len(i))
    d[i*t]=i
for i in sorted(d.items(),reverse=True):
    answer+=i[1]
print(answer)
# print(''.join(answer))