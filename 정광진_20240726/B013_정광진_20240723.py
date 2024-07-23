import sys
from collections import deque
input = sys.stdin.readline
a, b, c = map(int, input().split())

q = deque()
q.append((0, 0))

visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True

result = []

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))
        
def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y
        
        if x == 0:
            result.append(z)
            
        water = min(x, b - y)
        pour(x - water, y + water)
    
        water = min(x, c - z)
        pour(x - water, y)
        
        water = min(y, c - z)
        pour(x, y - water)
        
        water = min(y, a - x)
        pour(x + water, y - water)
        
        water = min(z, a - x)
        pour(x + water, y)

        water = min(z, b - y)
        pour(x, y + water)
        
bfs()

result.sort()
print(' '.join(map(str, result)))