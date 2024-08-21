from math import inf
from typing import List
import sys
from collections import deque
from sys import stdin
from collections import defaultdict
import heapq as H



# Contar Componentes 

# # https://cses.fi/problemset/task/1192

def flood_fill(x, y):
    global graph

    to_visit = [(x, y)]
    while to_visit:
        x, y = to_visit.pop()
        if 0 <= x < width and 0 <= y < length and graph[x][y] == ".":
            graph[x][y] = "x"
            to_visit.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

width, length = map(int, stdin.readline().split())
graph = list(map(lambda x: list(x.strip("\n")), stdin.readlines()))

room_count = 0
for row in range(width):
    for col in range(length):
        if graph[row][col] == ".":
            flood_fill(row, col)
            room_count += 1
print(room_count)

# # https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.g = grid
        islandCount = 0
        self.m, self.n = len(self.g), len(self.g[0])
        self.visited = [[False for x in range(self.n)] for y in range(self.m)]
        print(len(self.g), len(self.g[0]))
        print(len(self.visited), len(self.visited[0]))
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j] and self.g[i][j] != '0':
                    islandCount += 1
                    self.explore(i, j)
        return islandCount

    def explore(self, i, j):
        if i != 0:
            if not self.visited[i-1][j] and self.g[i-1][j] != '0':
                self.visited[i-1][j] = True
                self.explore(i-1, j)
        if j != 0:
            if not self.visited[i][j-1] and self.g[i][j-1] != '0':
                self.visited[i][j-1] = True
                self.explore(i, j-1)
        if i != self.m-1:
            if not self.visited[i+1][j] and self.g[i+1][j] != '0':
                self.visited[i+1][j] = True
                self.explore(i+1, j)
        if j != self.n-1:
            if not self.visited[i][j+1] and self.g[i][j+1] != '0':
                self.visited[i][j+1] = True
                self.explore(i, j+1)


# dijkstra

# # https://cses.fi/problemset/task/1671

def main():
    n, m = [int(x) for x in input().strip().split()]
    G = defaultdict(dict)
    for _ in range(m):
        a, b, w = [int(x) for x in input().strip().split()]
        if b not in G[a]:
            G[a][b] = w
        else:
            G[a][b] = min(G[a][b], w)

    shortest = [float("inf")] * (n + 1)
    shortest[1] = 0
    h = [(0, 1)]
    while h:
        distance, city = H.heappop(h)
        if distance > shortest[city]:
            continue
        for next_city in G[city]:
            duration = G[city][next_city]
            if shortest[next_city] > distance + duration:
                shortest[next_city] = distance + duration
                H.heappush(h, (distance + duration, next_city))

    print(*shortest[1:])

main()

# union find: 

# # https://cses.fi/problemset/task/1676

input = sys.stdin.readline  

def find(i):
    if Parent[i] == i:
        return i
    
    else:
        result = find(Parent[i])
        Parent[i] = result

        return result

def union(i, j):
    Parenti = find(i)
    Parentj = find(j)

    if Parenti == Parentj:
        return
    
    iSize = Size[Parenti]
    jSize = Size[Parentj]

    if iSize < jSize :
        i, j = j, i

    Parent[Parentj] = Parenti
    Size[Parenti] += Size[Parentj]

n, m = map(int, input().split())
Parent = [i for i in range(n+1)]
Size = [1 for i in range(n+1)]
Components = n
BiggestComponent = 1


for i in range(m):
    a, b = map(int, input().split())
    
    Parenta = find(a)
    Parentb = find(b)
    
    if Parenta != Parentb:
        Components -= 1
        union(a,b)
        size_a = Size[find(a)]
        BiggestComponent = max(BiggestComponent, size_a)

    print(Components, BiggestComponent)


# # https://leetcode.com/problems/find-if-path-exists-in-graph/description/

class Solution: 
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]

        def find(num: int):
            if parent[num] != num:
                parent[num] = find(parent[num])
            return parent[num]

        def union(num1: int, num2: int):
            num1, num2 = find(num1), find(num2)
            if num1 > num2:
                parent[num1] = num2
            else:
                parent[num2] = num1

        for n1, n2 in edges:
            union(n1, n2)
        print(parent)
        return find(parent[source]) == find(parent[destination])
    

# caminhos mínimos / bfs

# # https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        distance = [[inf]*n for _ in range(n)]
        q = [(0, 0)]
        distance[0][0] = 1

        def visitCell(x, y, d): 

            if distance[x][y]==inf:
                q.append((x, y))

            distance[x][y] = min(distance[x][y], d)

        while q:
            x, y = q.pop(0)
            newD = distance[x][y]+1

            if x-1>=0:
                if grid[x-1][y]==0:
                    visitCell(x-1, y, newD)

                if y-1>=0 and grid[x-1][y-1]==0:
                    visitCell(x-1, y-1, newD)    
                     
                if y+1<n and grid[x-1][y+1]==0:
                    visitCell(x-1, y+1, newD)

            if x+1<n:
                if grid[x+1][y] == 0:
                    visitCell(x+1, y, newD)

                if y-1>=0 and grid[x+1][y-1]==0:
                    visitCell(x+1, y-1, newD)

                if y+1<n and grid[x+1][y+1]==0:
                    visitCell(x+1, y+1, newD)

            if y-1>=0 and grid[x][y-1]==0:
                visitCell(x, y-1, newD)

            if y+1<n and grid[x][y+1]==0:
                visitCell(x, y+1, newD)

        return -1 if distance[n-1][n-1]==inf else distance[-1][-1]
    
# # https://leetcode.com/problems/open-the-lock/description/

class Solution:
    
    def __init__( self ):
        self.ans = 0
        self.d = None
        self.p = { "0000" }        
        self.q = set()
        self.t = None
        
        
    def next( self, s ):
        for i in range( 4 ):
            if s[i] == "0":
                m = "9", "1"
            elif s[i] == "9":
                m = "8", "0"
            else:
                o = ord( s[i] )
                m = chr( o - 1 ), chr( o + 1 )
                
            for p in m:
                q = s[ : i ] + p + s[ i + 1 : ]
                
                if q not in self.d:
                    self.d.add( q )
                    self.q.add( q )
                    
        
        
    def openLock( self, deadends: List[str], target: str ) -> int:
        if "0000" in deadends:
            return -1
        
        self.d = set( deadends )
        self.t = target
        
        return self.open()
        
        
        
    def open( self ):
        if self.t in self.p:
            return self.ans
        elif len( self.p ) < 1:
            return -1
        
        for s in self.p:
            self.next( s )
                
        self.ans += 1
        self.p = self.q
        self.q = set()
        
        return self.open()
    
# # https://cses.fi/problemset/task/1193

def main():
    rows, cols = [int(x) for x in input().strip().split()]
    maze = [input() for _ in range(rows)]
    distance = [-2 if c == "#" else -1 for row in maze for c in row]

    level = []
    bp = {}
    bIdx = None

    for r in range(rows):
        for c in range(cols):

            if maze[r][c] == "A":
                idx = r * cols + c
                level.append(idx)
                distance[idx] = 0
                bp[idx] = None

            if maze[r][c] == "B":
                bIdx = r * cols + c

    dist = 0

    while level:
        dist += 1
        new_level = []

        while level:
            idx = level.pop()
            r, c = divmod(idx, cols)
            new_idx = idx - 1

            if c - 1 >= 0 and distance[new_idx] == -1:
                distance[new_idx] = dist
                bp[new_idx] = idx
                new_level.append(new_idx)

            new_idx = idx + 1

            if c + 1 < cols and distance[new_idx] == -1:
                distance[new_idx] = dist
                bp[new_idx] = idx
                new_level.append(new_idx)

            new_idx = idx - cols

            if r - 1 >= 0 and distance[new_idx] == -1:
                distance[new_idx] = dist
                bp[new_idx] = idx
                new_level.append(new_idx)

            new_idx = idx + cols

            if r + 1 < rows and distance[new_idx] == -1:
                distance[new_idx] = dist
                bp[new_idx] = idx
                new_level.append(new_idx)

            if distance[bIdx] != -1:
                level.clear()
                break

        if distance[bIdx] != -1:
            break

        level = new_level

    if distance[bIdx] == -1:
        print("NO")
        return

    path = []
    curr = bIdx

    while True:
        prev = bp[curr]

        if prev is None:
            break
        if curr == prev - cols:
            path.append("U")
        elif curr == prev + cols:
            path.append("D")
        elif curr == prev - 1:
            path.append("L")
        else:
            path.append("R")
        curr = prev

    print("YES")
    print(distance[bIdx])
    print("".join(path[::-1]))
    
main()

# grafo bipartido

# # https://leetcode.com/problems/is-graph-bipartite/description/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        RED = -1
        BLACK = -2
        NONE = 0

        def rotate_color(color):
            if color == RED:
                return BLACK
            else: 
                return RED 

        visited = [False] * len(graph) 
        colored = [NONE] * len(graph)
        color = RED
        for i in range(len(graph)):
            if visited[i]:
                continue
            else:
                q = [i]
                while q:
                    nq = []
                    color = rotate_color(color)
                    for now in q:
                        visited[now] = True
                        if colored[now] == NONE:
                            colored[now] = color
                        else:
                            if colored[now] != color:
                                return False
                        for nh in graph[now]:
                            if visited[nh]:
                                continue
                            else:
                                nq.append(nh)
                    q = nq
        return True

# detecção de ciclo em grafo não-direcionado

# # https://cses.fi/problemset/task/1669

def detect_cicle(adj, n):
    visited = [False] * n
    prev = [None] * n

    def _bfs(source):
        queue = deque([source])
        visited[source] = True

        while queue:
            node = queue.pop()

            for neig in adj[node]:
                if visited[neig]:
                    if neig == prev[node]:
                        continue
                    else:
                        return (neig, node)

                visited[neig] = True
                prev[neig] = node
                queue.appendleft(neig)
               
        return False
    
    cycle = False
    for node in range(n):
        if visited[node]:
            continue
        if cycle:
            break
        cycle = _bfs(node)

    if cycle:
        start, end = cycle

        path = deque()
        while start is not None or end is not None:
            if prev[start] is not None:
                path.append(start)
                start = prev[start]

            if prev[end] is not None:
                path.appendleft(end)
                end = prev[end]
               
            if path[0] == path[-1]:
                break

            if start == end:
                path.append(start)
                path.appendleft(end)
                break
        
        start, end = 0, len(path) - 1
        while path[start] == path[end]:
            start += 1
            end -= 1
        start, end = start - 1, end + 1
        
        path = list(path)[start:end+1]

        print(len(path))
        print(*[i + 1 for i in path])
    else:
        print("IMPOSSIBLE")


def main():
    n, m = map(int, sys.stdin.readline().split())
    adjency = [[] for _ in range(n)]

    for _ in range(m):
        a, b = [int(i) - 1 for i in sys.stdin.readline().split()]
        adjency[a].append(b)
        adjency[b].append(a)

    detect_cicle(adjency, n)


if __name__ == "__main__":
    main()

# kruskal

# # https://cses.fi/problemset/task/1675

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, roads):
    roads.sort(key=lambda x: x[2])

    dsu = DisjointSetUnion(n)
    min_cost = 0
    edges_used = 0

    for u, v, cost in roads:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            min_cost += cost
            edges_used += 1
            
            if edges_used == n - 1:
                return min_cost

    return "IMPOSSIBLE"

def main():
    n, m = map(int, input().split())
    roads = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        roads.append((a - 1, b - 1, c))

    result = kruskal(n, roads)
    print(result)

if __name__ == "__main__":
    main()

        



        