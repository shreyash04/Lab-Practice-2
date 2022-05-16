from collections import defaultdict

# Function to perform DFS graph traversal
def DFS(u, visited, graph):
    if u not in visited:
        visited.add(u)
        print(u, end=" ")
    
        for v in graph[u]:
            DFS(v, visited, graph)


# Function to perform BFS graph traversal
def BFS(start, visited, graph):
    q = []
    q.append(start)
    visited[start] = True
    
    while len(q)!=0:
        u = q.pop(0)
        print(u, end=" ")
        
        for v in graph[u]:
            if visited[v] == False:
                q.append(v)
                visited[v] = True
    
    
# Main Program
vertices = int(input("Enter no. of vertices : "))
edges = int(input("Enter no. of edges : "))

graph = defaultdict(list)
print()
for _ in range(edges):
    u, v = map(int, input("Enter edge (u,v) : ").split())
    graph[u].append(v)
    # graph[v].append(u)

start = int(input("\nEnter starting node : "))

visited = set()
print("DFS :", end=" ")
DFS(start, visited, graph)

visited = [False]*vertices
print("\nBFS :", end=" ")
BFS(start, visited, graph)
