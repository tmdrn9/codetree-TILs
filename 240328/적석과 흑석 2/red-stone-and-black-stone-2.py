c,n=map(int,input().split())
red=[int(input()) for _ in range(c)]
black=[list(map(int,input().split())) for _ in range(n)]
answer=0
red.sort()
black.sort(key=lambda x:x[1]-x[0])

###################
for b in black:
    for r in red:
        if b[0]<=r and b[1]>=r:
            answer+=1
            red.remove(r)
            # print(r,b)
            break

###################

print(answer)