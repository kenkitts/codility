from collections import deque

def rotate(array: list, n: int):
    if len(array) == 0:
        return array
    queue = deque(array)
    for i in range(n):
        item = queue.pop()
        queue.appendleft(item)
    return list(queue)

print(rotate(['a','b','c'], 0))


