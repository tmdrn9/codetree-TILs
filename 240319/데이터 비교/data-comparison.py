n1=int(input())
li1=list(map(int,input().split()))
n2=int(input())
li2=list(map(int,input().split()))

cha=set(li2)-set(li1)
answer=[]

for i in li2:
    if i in cha:
        answer.append(str(0))
    else:
        answer.append(str(1))
print(' '.join(answer))