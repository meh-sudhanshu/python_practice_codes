from heapq import heappop, heappush, _heapify_max

max_heap = [1,4,2,6]

_heapify_max(max_heap)

print(heappop(max_heap))
_heapify_max(max_heap)
print(heappop(max_heap))
_heapify_max(max_heap)
print(heappop(max_heap))


print(max_heap)
