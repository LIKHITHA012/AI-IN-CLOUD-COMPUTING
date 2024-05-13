def bfs(graph, start_node):
    visited = []  # List to keep track of visited nodes
    queue = [start_node]  # Initialize the queue with the start node
    
    while queue:
        node = queue.pop(0)  # Dequeue the first node in the queue
        if node not in visited:
            visited.append(node)  # Mark the node as visited
            print(node, end=" ")  # Process the node (e.g., print or perform actions)
            
            # Enqueue all unvisited neighbors of the current node
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    print("\nBFS traversal completed.")

# Define the graph as a dictionary
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# Specify the start node for BFS
start_node = '5'

# Perform BFS traversal starting from the specified node
print("BFS traversal:")
bfs(graph, start_node)



#dfs
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph [node]:
            dfs(visited, graph, neighbor)
            
print("DFS:")
dfs(visited, graph,'5')
