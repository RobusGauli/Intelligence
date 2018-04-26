import os
import sys
import collections
import itertools
import inspect
from inspect import signature
from inspect import Signature
from inspect import Parameter
#a s ample representation of node

class Node:
  def __init__(self, val, right=None, left=None):
    self.val = val
    self.right = right
    self.left = left
  
  def _add_node(self, node):
    #check to see if the node val is less
    if node <= self:
      if not self.left:
        self.left = node
      else:
        self.left._add_node(node)
    else:
      #we assume it is greater than the current_node value so it goes to tright
      if not self.right:
        self.right = node
      else:
        self.right._add_node(node)
  
  def traverse(self):
    if self.left:
      self.left.traverse()
    print(self.val)
    if self.right:
      self.right.traverse()
    
  def lazy_traverse(self):
    '''Tree traversal using generator'''
    if self.left:
      yield from self.left.lazy_traverse()
    yield self
    if self.right:
      yield from self.right.lazy_traverse()

  
  def _search(self, node):
    if not node:
      raise ValueError('None not accepted')
    if self == node:
      return self
    elif self.left and node <= self:
      #check for the left search
      return self.left._search(node)
    elif self.right:
      return self.right._search(node)
    else:
      return None
    
  def __iter__(self):
    return self.lazy_traverse()

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
  


class BinaryTree:
  
  def __init__(self):
    self.root = None
  
  def add(self, val):
    if not self.root:
      self.root = Node(val)
    else:
      self.root._add_node(Node(val))
  
  def search(self, val):
    return self.root._search(Node(val))

  def traverse(self):
    return iter(self)

  def __repr__(self):
    return 'B Tree Root -> {}'.format(self.root)
  
  def __iter__(self):
    return iter(self.root)
