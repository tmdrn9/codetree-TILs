n,g=map(int,input().split())
invite={1}
total=[set(list(map(int,input().split()))[1:]) for _ in range(g)]
total=sorted(total,key=lambda x:len(x))
i=0
while len(total) != i:
    gr=total[i]
    cha=gr-invite
    if len(cha) == 1:
        invite=invite.union(cha)
        total.remove(gr)
        i=0
    else:
        i+=1

print(len(invite))