import heapq

n=int(input())
li=list(map(int, input().split()))
pq=[li[-1]]
summ=li[-1]

max_avg=0
for k in range(n-2,0,-1):
    heapq.heappush(pq,li[k])
    summ+=li[k]

    min_n=pq[0]
    temp_avg=((summ-min_n)/(n-k-1))
    if temp_avg>max_avg:
        max_avg=temp_avg
print(f"{max_avg:.2f}")