def fatorial(n):
    fat = 1

    for i in range(1, n+1):
        fat *= i
    
    return fat

n = int(input())
print(fatorial(n))