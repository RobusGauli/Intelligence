''' A grid based bfs implementation '''
import os
import collections


class Point:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __repr__(self):
    return 'Point({}, {})'.format(self.x, self.y)
  
  def __hash__(self):
    return hash((self.x, self.y))

class Node:
  
  def __init__(self: Node, point: Point) -> None:
    self.point: Point = point
    self.edges: Node = []
    #to keep track of where it came from
    self.parent: Node = None

  def add_edge(self: Node, e: Node):
    self.edges.append(e)

  def __eq__(self: Node, other: Node) -> bool:
    return self.point == other.point
  
  def __hash__(self):
    return hash(self.point)
  
  def __repr__(self: Node) -> str:
    return 'Node: {}'.format(self.point)
  
#an utitliy function that gives out left, right, top, bottom Point for the given Point 

EdgePoints = collections.namedtuple('EdgePoint', 'left right top bottom')

def edges(point: Point, rows: int, cols: int) -> EdgePoints:
  '''Utility to spit out the edges for the given points'''

  left_point = Point(point.x - 1, point.y) if point.x - 1 >= 0 and point.x - 1 < rows else None
  right_point = Point(point.x + 1, point.y) if point.x + 1 >= 0 and point.x + 1 < rows else None
  top_point = Point(point.x, point.y - 1) if point.y - 1 >= 0 and point.y - 1 < cols else None
  bottom_point = Point(point.x, point.y  + 1) if point.y + 1 >= 0 and point.y + 1 < cols else None

  return EdgePoints(left_point, right_point, top_point, bottom_point)


class Graph:
  def __init__(self: Graph, points: list, rows: int, cols: int) -> None:
    self.points = list(points)
    self.nodes: list = []
    self.point_node = {}
    self.create_graph(rows, cols)
    
  
  def create_graph(self: Graph, rows: int, cols: int) -> None:
    for point in self.points:
      p_node = self.point_node.get(point)
      if not p_node:
        p_node = Node(point)
        self.nodes.append(p_node)
        self.point_node[point] = p_node
      #get the edge_points
      for edge_point in edges(point, rows, cols):
        if edge_point:
          #if it is not none, get the node associated with that
          n = self.point_node.get(edge_point)
          if not n:
            n = Node(edge_point)
            self.nodes.append(n)
            self.point_node[edge_point] = n
          p_node.add_edge(n)


def bfs(graph: Graph, start_point: Point, end_point: Point) -> Node:
  start_node: Node = graph.point_node.get(start_point)
  end_node: Node = graph.point_node.get(end_point)
  
  _q: list = []
  visited: set = set()
  _q.append(start_node)

  while _q:
    current_node = _q.pop(0)
    visited.add(current_node)
    if current_node == end_node:
      return current_node
    for edge_node in current_node.edges:
      if edge_node not in visited:
        _q.append(edge_node)
        edge_node.parent = current_node


def traverse(node: Node) -> list:
  if not node:
    return
  yield node.point
  yield from traverse(node.parent)

def main():
  rows = 4
  cols = 4
  points = (Point(row, col) for row in range(rows) for col in range(cols))
  g = Graph(points, rows, cols)
  start = Point(0, 0)
  end = Point(3, 3)
  target = bfs(g, start, end)
  if target:
    paths = list(traverse(target))
    print(paths)

if __name__ == '__main__':
  main()
  



