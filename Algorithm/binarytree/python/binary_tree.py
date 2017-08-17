import os
import sys
import collections

#a sample representation of node

class Node:
  def __init__(self, val, right=None, left=None):
    self.val = val
    self.right = right
    self.left = left
  
  def add_node(self, node):
    #check to see if the node val is less
    if node.val <= self.val:
      if not self.left:
        self.left = node
      else:
        self.left.add_node(node)
    else:
      #we assume it is greater than the current_node value so it goes to tright
      if not self.right:
        self.right = node
      else:
        self.right.add_node(node)
  
  def traverse(self):
    if self.left:
      self.left.traverse()
    print(self.val)
    if self.right:
      self.right.traverse()
  
  def search(self, node):
    if not node:
      raise ValueError('None not accepted')
    if self == node:
      return self
    elif node.val < self.val
    
  
  def __eq__(self, other):
    return self.val == other.val

  def __gt__(self, other):
    return self.val > other.val
  
  def __lt__(self, other):
    return self.val < other.val
  
  def __ge__(self, other):
    return self.val >= other.val
  
  def __le__(self, other):
    return self.val <= other.val
  
  def __repr__(self):
    return 'Node: {}'.format(self.val)
  
  