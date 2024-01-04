from queue import LifoQueue

t = int(input())

while t > 0:
    s = input()
    pilha = LifoQueue()
    ans = 'S'

    for i in s:
        if i == '(' or i == '[' or i == '{':
            pilha.put(i)
        else:
            if not pilha.empty():
                aux = pilha.get()

                if i == ')' and aux == '(':
                    pass
                elif i == ']' and aux == '[':
                    pass
                elif i == '}' and aux == '{':
                    pass
                else:
                    ans = 'N'
                    break
            else:
                ans = 'N'
                break
    
    if not pilha.empty() and ans == 'S':
        ans = 'N'

    
    print(ans)

    t -= 1