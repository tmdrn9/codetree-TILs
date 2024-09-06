import heapq

n=int(input())
li=list(map(int, input().split()))

mean_li=[]
for k in range(1,n-1):
    temp=li[k:]
    heapq.heapify(temp)
    heapq.heappop(temp)
    mean_li.append(sum(temp)/(n-k-1))
print(f"{max(mean_li):.2f}")