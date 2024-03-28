c,n=map(int,input().split())
red=[int(input()) for _ in range(c)]
black=[list(map(int,input().split())) for _ in range(n)]
answer=0
red.sort()
black.sort(key=lambda x:x[1]-x[0])

###################
# for b in black:
#     for r in red:
#         if b[0]<=r and b[1]>=r:
#             answer+=1
#             red.remove(r)
#             break
cnt=-1
for r in red:
    cnt+=1
    if cnt==n:
        break
    if black[cnt][0]<=r and black[cnt][1]>=r:
        answer+=1
    else:
        continue
    
###################

print(answer)