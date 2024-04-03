n=int(input())
init=input()
final=input()

answer=0
mismatched = False

for i in range(n):
    if init[i]!=final[i]:
        if not mismatched:
            mismatched=True
            answer+=1

    else:
        mismatched = False
    print(mismatched)