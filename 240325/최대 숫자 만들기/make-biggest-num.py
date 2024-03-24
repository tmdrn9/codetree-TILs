from functools import cmp_to_key
# 이 순서가 우리가 원하는 순서라면 0보다 작은 값을, 
# 반대라면 0보다 큰 값을
# 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
def compare(x,y):
    if x+y>y+x:
        return -1
    if y+x>x+y:
        return 1
    return 0

n=int(input())
li=[input() for _ in range(n)]
li=sorted(li,key=cmp_to_key(compare))

print(''.join(li))