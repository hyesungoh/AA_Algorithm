import sys
input = sys.stdin.readline

def find(node):
    # 현재 노드가 루트 노드일 시
    if node == parent[node]:
        # 루트 노드 값을 반환
        return node

    # 루트 노드가 아닐 시 재귀적으로 탐색
    p = find(parent[node])
    # 루트 노드를 현재 node 값에 저장
    parent[node] = p
    return p # 해당 루트 노드 값을 반환

    # 루트 노드가 아닐 시 탐색한 후 할당, 반환하는 과정을 경로 압축 최적화라고 한다
    # return find(parent[u])와 같이 작성시 경로 압축 최적화가 안되었다고 할 수 있는데
    # 이는 단순히 배열에 할당하지 않기 때문인가 ?
    # 아무튼 사용 이유는 한 쪽으로 치우쳐진 트리일 때 걸리는 시간이라고 한다.
    # 문제를 더 풀어가며 이해해야할 부분 같다.


def union(a, b):
    # a, b의 루트 노드를 찾는다.
    parent_a = find(a)
    parent_b = find(b)

    # 루트노드가 갖지 않을 시 b의 루트 노드에 a 루트 노드 값을 저장
    # a의 루트 노드에 b 루트 노드 값을 저장해도 된다.
    if parent_a != parent_b:
        parent[parent_b] = parent_a


n, m = map(int, input().split())
# 각 노드의 루트 노드를 저장할 배열
# 처음에는 자기 자신을 루트 노드로 생성
parent = [i for i in range(n+1)]

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        parent_a = find(a)
        parent_b = find(b)
        print("YES" if parent_a == parent_b else "NO")
