# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 나의 문제 해석
# 각 노드마다 x-1, x+1 2*x 총 3개의 루트를 가지게 된다.
# 따라서 탐색할 인접 노드는 각 노드 당 3개씩 고정이다.
# 가장 빠른 경로를 찾는 문제는 BFS를 사용.


from collections import deque


def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == k:
            return visited[v]
        for i in (v - 1, v + 1, 2 * v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)


n, k = 5, 17  # 4
visited = [0 for i in range(100001)]

print(bfs(n))
