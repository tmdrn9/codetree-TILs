n=int(input())
init=input()
final=input()

def divide(base,strr):
    li=[]
    start=0
    for i,n in enumerate(strr[1:]):
        if i==len(strr)-2:
            li.append((start,i+1))
        if base!=n:
            li.append((start,i))
            start=i+1
            base=n
    return li

li=divide(init[0],init)
diff=[]
cnt=0
for n,(i,j) in enumerate(zip(init,final)):
    if i!=j:
        diff.append(n)
for i in li:
    ok=False
    for j in diff:
        if i[0]<=j and j<=i[1]:
            diff.remove(j)
            ok=True
    if ok:
        cnt+=1
print(cnt)