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
  
  def __init__(self: Node, point: Point):
    self.point: Point = point
    self.edges: Node = []
    #to keep track of where it came from
    self.parent: Node = None

  def add_edge(self: Node, e: Node):
    self.edges.append(e)

  def __eq__(self: Node, other: Node):
    return self.point == other.point
  
  def __repr__(self: Node):
    return 'Node: {}'.format(self.point)
  
#an utitliy function that gives out left, right, top, bottom Point for the given Point 


def edges(point: Point, rows: int, cols: int):
  left_point = Point(point.x - 1, point.y) if point.x >= 0 and point.x < rows else None
  right_point = Point(point.x + 1, point.y) if point.x >= 0 and point.x < rows else None
  top_point = Point(point.x, point.y - 1) if point.y >= 0 and point.y < cols else None
  bottom_point = Point(point.x, point.y  + 1) if point.y >= 0 and point.y < cols else None
  return left_point, right_point, top_point, bottom_point


  