from queue import SimpleQueue

q = SimpleQueue()

aux = ord('A')
for i in range(16):
    q.put(chr(aux+i))


for i in range(15):
    m,n = map(int, input().split())

    if m > n:
        q.put(q.get())
        q.get()
    else:
        q.get()
        q.put(q.get())

print(q.get())