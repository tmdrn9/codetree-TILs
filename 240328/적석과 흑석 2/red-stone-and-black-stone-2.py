c,n=map(int,input().split())
red=[int(input()) for _ in range(c)]
black=[list(map(int,input().split())) for _ in range(n)]
# c,n=6,8
# red=[13,28,43,2,0,21] #[int(input()) for _ in range(c)]
# black=[[0,21],[1,20],[12,14],[14,33],[22,38],[0,11],[12,19],[0,31]]
answer=0
red.sort()
black.sort(key=lambda x:x[1]-x[0])
black.sort(key=lambda x:x[1])
# print(red)
# print(black)
###################
for b in black:
    for r in red:
        if b[0]<=r and b[1]>=r:
            answer+=1
            red.remove(r)
            break
# ###################

print(answer)