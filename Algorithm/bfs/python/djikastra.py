import json
from collections import namedtuple
from queue import PriorityQueue
letter = json.loads(open('letter.json').read())

class Node:
	
	def __init__(self, label):
		self.label = label
		self.edges = []
		self.parent = None
		self.cost = 999999
	
	def __eq__(self, other):
		return self.label == other.label
	
	def __hash__(self):
		return hash(self.label)
	
	def __repr__(self):
		return 'Node: {}'.format(self.label)

DistanceEdge = namedtuple('DistanceEdge', 'distance edge')

class Graph:
	
	def __init__(self, letter):
		self.letter = letter
		self.label_node = {}
		self.nodes = []
		self._create_graph()
	
	def _create_graph(self):
		for v in self.letter:
			_value = v['val']
			#try getting from the hash map table
			node = self.label_node.get(_value)
			if not node:
				node = Node(_value)
				self.nodes.append(node)
				self.label_node[_value] = node
			for edge in v['edges']:
				_e_value = edge['val']
				_e_node = self.label_node.get(_e_value)
				if not _e_node:
					_e_node = Node(_e_value)
					self.nodes.append(_e_node)
					self.label_node[_e_value] = _e_node
				#now update th edges
				node.edges.append(DistanceEdge(edge['cost'], _e_node))


def search(g, start, end):
	start_node = g.label_node[start]
	start_node.cost = 0
	end_node = g.label_node[end]
	visited = set()	
	q = PriorityQueue()
	q.put_nowait((start_node.cost, start_node))
	while q:
		current_node = q.get_nowait()[1]
		visited.add(current_node)	
		if current_node == end_node:
			return current_node
		for edge in current_node.edges:
			edge_node = edge.edge
			if edge_node not in visited:
			#existing cost to this node
				current_cost = edge_node.cost
				#calculate the new cost
				new_cost = current_node.cost + edge.distance
				if new_cost <= current_cost:
					#then make this new cost as the cost for the node
					edge_node.cost = new_cost
					#again make this node's parent to the current_node
					edge_node.parent = current_node
					q.put_nowait((edge_node.cost, edge_node))
					
def traverse(node):
	if not node:
		return 
	yield node.label
	yield from traverse(node.parent)


def main():
	g = Graph(letter)
	n = search(g, 'b', 'k')
	print(list(traverse(n)))

if __name__ == '__main__':
	main()










