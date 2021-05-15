# 최단경로 알고리즘

- 두 노드를 잇는 가장 짧은 경로를 찾는 알고리즘
- 가중치 그래프에서 **간선(Edge)의 가중치 합이 최소**가 되도록 만든다

---

### 다익스트라 알고리즘 (**음의 가중치**를 허용하지 않는 경우)

-

```py
import heapq

mygraph = {
  'A': {'B':8, 'C':1, 'D':2},
  'B': {},
  'C': {'B':5, 'D':2},
  'D': {'E':3, 'F':5},
  'E': {'F':1},
  'F': {'A':5}
}

def dijkstra(graph, start):
  distances = {node: float('inf') for in graph}
  distances[start] = 0
  queue = []

  heapq.heappush(queue, [distances[start], start])

  while queue:
    current_distance, current_node = heapq.heappop(queue) # 구조분해 할당

    if distances[current_node] < current_distance:
      continue

    for adjacent, weight in graph[current_node].items():
      distance = current_distance + weight

      if distance < distances[adjacent]:
        distances[adjacent] = distance
        heapq.heappush(queue, [distance, adjacent])

  return distances
```
