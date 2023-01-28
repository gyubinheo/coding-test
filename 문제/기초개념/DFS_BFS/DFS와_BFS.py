# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque


n, m, v = 4, 5, 1
arr = ["1 2", "1 3", "1 4", "2 4", "3 4"]

graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, arr[i].split())
    graph[a][b] = graph[b][a] = 1
dfs_visited = [0] * 5
bfs_visited = [0] * 5


def dfs(v):
    # v 방문
    dfs_visited[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        # v의 인접 노드인 i에 방문하지 않았다면
        if graph[v][i] == 1 and dfs_visited[i] == 0:
            # i 방문
            dfs(i)


def bfs(v):
    queue = deque([v])
    # v 방문
    bfs_visited[v] = 1
    # 큐가 빌 때까지
    while queue:
        # 큐에서 노드를 하나 뺌
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            # v의 인접 노드인 i에 방문하지 않았다면
            if graph[v][i] == 1 and bfs_visited[i] == 0:
                # i 방문
                queue.append(i)
                bfs_visited[i] = 1


dfs(v)
print()
bfs(v)
