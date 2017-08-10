import json
#load the data 
number_tree = json.loads(open('nums.json').read())
#model the node instance
class Node:
  def __init__(self, val):
    self.val = val
    self.edges = []
    #special instance variable that keeps track of its parent
    self.parent = None
      
  def add_edge(self, edge_node):
    self.edges.append(edge_node)
  
  def add_parent(self, p):
    self.parent = p

  def __eq__(self, other):
    return self.val == other.val
  
  def __hash__(self):
    return hash(self.val)

  def __repr__(self):
    return 'Node: {}, edges: {}'.format(self.val, ', '.join(str(e.val) for e in self.edges))
  
class Graph:
  def __init__(self, number_tree):
    self.number_tree = number_tree
    #state to keep track of all the nodes
    self.nodes = []
    #state that act as hash table for value and a node
    self.value_node = {}
    self._create_graph()
  
  def _create_graph(self):
    #for every value in the number_tree
    for value in self.number_tree:
      #try to access the node from the Graph
      node = self.value_node.get(value['val'])
      #if not node
      if not node:
        node = Node(value['val'])
        self.nodes.append(node)
        self.value_node[value['val']] = node
      #now foreach node attach the edges
      for e in value['edges']:
        #trey to get the edg node
        edge_node = self.value_node.get(e)
        if not edge_node:
          #we need to create one
          edge_node = Node(e)
          self.nodes.append(edge_node)
          self.value_node[e] = edge_node
        node.add_edge(edge_node)

def bfs(graph, start, end):
  start_node = graph.value_node.get(start)
  end_node = graph.value_node.get(end)
  if not start_node or not end_node:
    print('Please specify the valid start and end nodes')
    return
  q = []
  visited = set()
  q.append(start_node)
  visited.add(start_node)
  while q:
    current_node = q.pop(0)
    if current_node == graph.value_node.get(end):
      return current_node
    for e in current_node.edges:
      if e not in visited:
        q.append(e)
        visited.add(e)
        e.add_parent(current_node)

def traverse_back(node):
  if not node:
    return
  yield node.val
  yield from traverse_back(node.parent)

def main():
  #create a graph isntance
  graph = Graph(number_tree)
  #now apply the breadth first search
  last_node = bfs(graph, 1, 100)
  #this will return the last_node and then we finally trace back its parent recursively towards the root
  paths = list(traverse_back(last_node))
  print(paths)
  return paths

if __name__ == '__main__':
  main()




  
  
  

  

