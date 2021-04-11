import random

res = [random.randrange(0, 10, 1) for i in range(100)]
print(res)

import fifo
import lru
import optimal

x = fifo.fifo(res)
y = lru.lru(res)
z = optimal.optimal(res)

print('Fifo', x)
print('lru', y)
print('optimal', z)
