import json

movie_tree = json.loads(open('kevinbacon.json').read())

class Node:
  def __init__(self, val):
    self.val = val
    self.edges = []
    self.parent = None
  
  def add_edge(self, e):
    self.edges.append(e)
    e.edges.append(self)
  
  def add_parent(self, p):
    self.parent = p
  
  def __eq__(self, other):
    return self.val == other.val
  
  def __hash__(self):
    return hash(self.val)
  
  def __repr__(self):
    return 'Node: {}, edges: {}'.format(self.val, ', '.join(str(e.val) for e in self.edges))

class Graph:
  '''This class Keeps tracks of all the nodes and prepare the look up table for bfs manipulation '''

  def __init__(self, movie_tree):
    self.movie_tree = movie_tree
    self.nodes = []
    self.value_node = {}
    self.create_graph()
  
  def create_graph(self):
    #for every 
    for movie in self.movie_tree['movies']:
      movie_node = self.value_node.get(movie['title'])
      if not movie_node:
        movie_node = Node(movie['title'])
        self.nodes.append(movie_node)
        self.value_node[movie['title']] = movie_node
      for edge in movie['cast']:
        edge_node = self.value_node.get(edge)
        if not edge_node:
          #the create one
          edge_node = Node(edge)
          self.nodes.append(edge_node)
          self.value_node[edge] = edge_node
        movie_node.add_edge(edge_node)
  

#now implementation of bfs
def bfs(g, start, end):
  start_node = g.value_node.get(start)
  end_node = g.value_node.get(end)
  visited = set()
  queue = []
  queue.append(start_node)
  visited.add(start_node)
  while queue:
    current_node = queue.pop(0)
    if current_node == end_node:
      return current_node
    for edge in current_node.edges:
      if edge not in visited:
        queue.append(edge)
        visited.add(edge)
        edge.add_parent(current_node)

def traverse(node):
  if not node:
    return
  yield node.val
  yield from traverse(node.parent)

def main():
  g = Graph(movie_tree)
  target = bfs(g, 'Javier Bardem', 'Kevin Bacon')
  paths  = traverse(target)
  print(list(paths))

if __name__ == '__main__':
  main()



