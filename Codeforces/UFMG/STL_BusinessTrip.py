k = int(input())
ans = 0

v = list(map(int, input().split()))
v.sort(reverse=True) 

for i in v:
    if k <= 0:
        break

    k -= i
    ans+=1

if k > 0:
    ans = -1

print(ans)

