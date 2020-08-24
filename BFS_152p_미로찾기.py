n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x,y):
    if x<-1