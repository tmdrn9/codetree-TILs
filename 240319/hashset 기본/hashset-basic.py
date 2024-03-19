n=int(input())
s=set()
for i in range(n):
    temp=input().split()
    if temp[0]=='add':
        s.add(int(temp[1]))
    elif temp[0]=='remove':
        s.remove(int(temp[1]))
    else:
        if int(temp[1]) in s:
            print('true')
        else:
            print('false')