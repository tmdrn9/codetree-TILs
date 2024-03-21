n,g=map(int,input().split())
invite={1}
for _ in range(g):
    group=set(list(map(int,input().split()))[1:])
    if len(group.intersection(invite))!=0 and len(group-invite) == 1:
        for i in group:
            invite.add(i)
print(len(invite))