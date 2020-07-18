graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}


def BFS(graph,start):
    queue=[]
    visited=set()
    queue.append(start)
    visited.add(start)

    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=graph[vertex]
        for node in nodes:
            if node not in visited:
                queue.append(node)
                visited.add(node)
        print(vertex)

# BFS(graph,"A")


def DFS(graph,start):
    stack=[]
    visited=set()
    stack.append(start)
    visited.add(start)

    while len(stack)>0:
        vertex=stack.pop()
        nodes=graph[vertex]
        for node in nodes:
            if node not in visited:
                stack.append(node)
                visited.add(node)
        print(vertex)

# DFS(graph,"A")

seen=set()
def DFS(node):
    seen.add(node)
    print(node)
    nodes=graph[node]
    for w in nodes:
        if w not in seen:
            DFS(w)

DFS("A")