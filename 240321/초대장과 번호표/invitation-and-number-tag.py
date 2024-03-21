n,g=map(int,input().split())
invite={1}
total=[]
# for _ in range(g):
#     group=set(list(map(int,input().split()))[1:])
#     total.append(group)
#     if len(group-invite) == 1:
#         for i in group:
#             invite.add(i)


total=[(set(list(map(int,input().split()))[1:])) for _ in range(g)]
for i in range(g):
    gr=total[i]
    cha=gr-invite
    if len(cha) == 1:
        for j in cha:
            invite.add(j)
            print(j)
        i=0



print(len(invite))