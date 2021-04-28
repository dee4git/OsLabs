import fifo
import lru
import optimal

q = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
q = 8, 0, 0, 1, 0, 2, 7, 1
print('-------fifo-----')
fifo.fifo(q)
print()
print()
print('-------lru-----')
lru.lru(q)
print()
print()
print('--------optimal------')
# optimal.optimal(q)
