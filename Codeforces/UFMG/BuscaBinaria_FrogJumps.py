t = int(input())

def eh_possivel(m, s):
    cont = 1
    for i in s:
        if i == 'L':
            cont += 1
        else:
            cont = 1

        if cont > m:
            return False
    
    return True

while t > 0:
    s = input()

    l = 1
    r = 2e5+10
    while l < r:
        m = int((l + r) / 2)

        if eh_possivel(m, s):
            r = m
        else:
            l = m+1

    print(r)

    t -= 1