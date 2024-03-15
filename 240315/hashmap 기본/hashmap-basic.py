n=int(input())
d=dict()
for i in range(n):
    temp=(input().split())
    if temp[0]=='add':
        d[temp[1]]=temp[2]
    elif temp[0]=='remove':
        d.pop(temp[1])
    else:
        if temp[1] in d:
            print(d[temp[1]])
        else:
            print('None')