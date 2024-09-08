n,k=map(int,input().split())
n_li=[]
for _ in range(n):
    n_li.append(int(input()))
hap=0
for i in n_li[::-1]:
    if k==0:
        break
    if k<i:
        continue
    j=k//i
    hap+=j
    k-=(j*i)

print(hap)