n,g=map(int,input().split())
invite={1}
total=[]
for _ in range(g):
    group=set(list(map(int,input().split()))[1:])
    total.append(group)
    if len(group.intersection(invite))!=0 and len(group-invite) == 1:
        for i in group:
            invite.add(i)
for gr in total:
    if len(gr.intersection(invite))!=0 and len(gr-invite) == 1:
        for i in gr:
            invite.add(i)

print(len(invite))