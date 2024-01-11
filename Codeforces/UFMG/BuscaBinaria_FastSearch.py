from bisect import bisect_left, bisect_right

n = int(input())
v = list(map(int, input().split()))
v.sort()

k = int(input())
ans = []

while k > 0:
    l,r = map(int, input().split())

    lower_bound = bisect_left(v, l)
    upper_bound = bisect_right(v, r)

    ans.append(upper_bound - lower_bound)
    
    """
    VOlTAR AQUI DENOVO E TAMBÉM EM C++ PRA IMPLEMENTAR LOWER_BOUND E UPPER_BOUND SEM FUNÇÃO PRONTA!!!!!!!!!!!
        # lower_bound:
        x=0
        y=n-1

        while x < y:
            m = int((x+y) / 2)

            if v[m] == l:
                y = m
                break
            elif v[m] > l:
                y = m
            else:
                x = m+1

        if v[y] < l:
            y+=1

        #print(v)
        #print("lower_bound:", y)
        # upper_bound:
        x2=0
        y2=n-1

        while x2 < y2:
            m = int((x2+y2) / 2)

            if v[m] > r:
                y2=m
            else:
                x2 = m+1

        if v[y2] <= r:
            y2 += 1
        

        #print("upper_bound:", y2)

        ans.append(y2 - y)
    """
    k -= 1

for i in ans:
    print(i, end=" ")