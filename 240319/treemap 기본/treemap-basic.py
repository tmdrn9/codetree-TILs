from sortedcontainers import SortedDict

n=int(input())
d = SortedDict()

for i in range(n):
    li=input().split()

    if len(li)==3:
        d[int(li[1])]=int(li[2])

    elif len(li)==2:
        if li[0]=='find':
            if int(li[1]) in d:
                print(d[int(li[1])])
            else:
                print(None)
        else:
            d.pop(int(li[1]))

    else:
        if len(d)==0:
            print('None')
        else:
            li=list(map(str,d.values()))
            # for i in d:
            #     li.append(str(i))
            print(' '.join(li))