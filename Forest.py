


"""
Given a set of vertices, what are all the possible forests/how many distinct forests exist

This seems like it's easy to look up, however I wanted to see if I could figure it out
"""

class Node:
	"""
	Graph Node
	"""

	def __init__(self, value, edges = []):
		self.value = value
		self.edges = edges


"""
To be a forest, there must not be any cycles. This removes a lot of possibilities,
as multiple edges between vertices would create cycles already, thus only one way edges
can exist between vertices.

Thus, given n nodes, the maximum number of edges isn't n^2, but (n choose 2)
This can be lessened even more by having a single tree, rather than a forest. To have
exactly one tree with no cycles, all the vertices must be connected in some way.
The simple example would be a straight line, which would have exactly (n-1) edges, which
will be the new maximum. Removing any edges would create a new tree, which will be a forest
which is okay.

The question is how to generate all forests.

First test will be combinatorial.
How many forests can be made with n vertices and m edges? Given 0 edges, only one distinct
forest can be made (all singleton trees).
Given 1 edge, two nodes must be chosen to be the two that have an edge. thus (n choose 2)
Given 2 edges, two distinct pairs must be chosen, however this becomes interesting. Either 3 nodes can be
chosen to create a chain, or 4 can be chosen to create two separate trees.
So, two distinct pairs of nodes must be chosen, the question is how to do that...
	There must be a set of all distinct pairs of nodes. Then given m edges, m pairs must be chosen
	from the set.
The set of all distinct pairs given n nodes will be n(n-1)/2 or (n choose 2). This will be the set of
possible edges to choose from.
From this set, m edges must be chosen, thus ( n(n-1)/2 choose m ) is the number of unique forests given
n nodes and m edges

But this doesn't consider cycles. Is there a way to build forests from scratch?
"""

"""
Second test will be recursion

Base case: With 1 vertex, there is exactly one distinct forest (the singleton)

Next case: If there are x distinct forests given n nodes ( f(n) = x ), then what is f(n+1)?
	Adding another node has multiple options:
		Don't connect to any other tree, leaving it a singleton					1
		Connect it to a node. Because there is only one connection point,
		A cycle can't form. Thus it will still remain a forest.
		Choosing from n nodes, the direction must be chosen, as well as the
		distinct forest to build it on, thus 									2n*x

	f(1) = 1, f(n+1) = 1 + 2*n*f(n)

This doesn't work either, as if the nodes are distinct, the last node added will never
have more than one edge attached.
"""










