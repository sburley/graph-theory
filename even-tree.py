import sys

# read the first line into a list [n,m] where n is 
# the number of nodes and m is the number of edges
config = sys.stdin.readline().split(' ')
# declare some empty variables for later
edges = []
adj_list = {}
count = 0
b = []

# take all the edges and put them in a nested list
for i in range(int(config[1])):
    i = sys.stdin.readline().split(' ')
    edges.append((int(i[0]), int(i[1])))
    edges.append((int(i[1]), int(i[0])))

for start, end in edges:
    try:
        adj_list[end].append(start)
    except KeyError:
        adj_list[end] = [start]

def DFSiter(graph, root):
    '''
    For a given node, make a stack of all the 
    '''
    visited = []
    stack = graph[root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend([x for x in graph[node] if x not in visited])
    return visited
        
for a in adj_list:
    b.append(a)
for a in b:
    if len(DFSiter(adj_list, a)) % 2 == 0:
        count += 1

print(count-1)