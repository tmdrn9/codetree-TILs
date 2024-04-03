n=int(input())
init=list(input())
final=list(input())
cnt=0
def change(temp):
    return list(map(lambda x:'G' if x=='H' else 'H',temp))

for i in range(n-1,-1,-1):
    if init[i]!=final[i]:
        cnt+=1
        init=change(init)
print(cnt)