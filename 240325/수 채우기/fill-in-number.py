n=int(input())
n5,remain=divmod(n,5)
if remain==0:
    print(n5)
elif remain%2==0:
    n2,_=divmod(remain,2)
    print(n5+n2)
else:
    if remain==1:
        print(n5+2)
    else:
        print(n5+3)