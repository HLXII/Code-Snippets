
import statistics

'''
The Fractional Knapsack problem is a variation of the knapsack problem

There are n items, with costs {c1, ... , cn} and weights {w1, ... , wn}.
You have a knapsack of size W, and you want to maximize the cost of the items you take.
You are allowed to break items into fractions of their weight.

The greedy algorithm solution is to sort the items by their price/weight ratio, then
choose the items with the highest ratio until the knapsack is full.
This requires sorting the items, which is O(nlog(n)), then iterating over the sorted
list, which is O(n). Thus, the overall solution is O(nlog(n))
'''

def FractionalKnapsackSort(costs, weights, maxWeight):
	"""
	Fractional Knapsack Algorithm that uses sorting

	Args:
		costs:		List of costs of the items
		weights:	List of the weights of the items

	Returns:
		Maximum cost of items that can be placed in the knapsack
	"""

	# Create list of the items
	pairings = list(zip(costs, weights))
	# Sorting based on ratio
	pairings.sort(key=lambda x: float(-x[0]/x[1]))

	totalWeight = 0
	totalCost = 0

	# Iterating over item list in order of largest ratio
	for itemCost, itemWeight in pairings:
		# If the current item does not fit in the knapsack completely
		if totalWeight + itemWeight > maxWeight:
			# Take a fraction of the item
			fraction = float( (maxWeight - totalWeight) / itemWeight)
			fractionCost = itemCost * fraction
			totalCost += fractionCost
			# Return total cost, as the knapsack is full
			return totalCost
		# Item fits in knapsack completely
		else:
			# Add item to knapsack and continue
			totalWeight += itemWeight
			totalCost += itemCost

	# If all the items were added and there's still space, just return the total
	# cost of all the items, as they can all be taken
	return totalCost

'''
However, there is a more efficient algorithm that uses a median selection algorithm
This creates a O(n) time-complexity algorithm

By finding the median of the list of price/weight ratios, the items can be split into
three groups:
	Items with lower ratios
	Items with equal ratios
	Items with larger ratios

Now some decisions must be made:
	Check the list of items with larger ratios. 
	Do the sum of their weights exceed the knapsack? 
		If so, then the optimal subset of items is within that list.
		Call the algorithm on the subset of items with larger ratios

		If not, then the optimal solution contains that subset, as well as some items
		from the set of items with equal ratios.
		Add all the items with larger ratios to the knapsack, then begin adding items
		from the subset with equal ratios to the knapsack
		Either after a couple items, the knapsack is full, or all the items from this
		subset are added to the knapsack
			If the knapsack is full, this is the solution, and the total cost can be returned

			If the knapsack isn't full, then some items from the set of items with lower ratios
			must be added.
			Call the algorithm on the subset of items with lower ratios, but also change
			the maximum capacity of the knapsack to the max capacity - added item weight
'''

def FractionalKnapsackMedian(costs, weights, maxWeight):
	"""
	Fractional Knapsack Algorithm that uses median selection

	Args:
		costs:		List of costs of the items
		weights:	List of the weights of the items

	Returns:
		Maximum cost of items that can be placed in the knapsack
	"""

	# Creating list of the items
	pairings = list(zip(costs, weights))

	# Creating list of ratios
	ratios = [float(c/w) for c,w in pairings] 

	# Creating subset lists for items
	lower = []
	equal = []
	higher = []

	# Finding median of ratios
	median = statistics.median(ratios)

	# Partitioning items into the three subsets
	for itemCost, itemWeight in pairings:
		if float(itemCost/itemWeight) < median:
			lower.append((itemCost, itemWeight))
		elif float(itemCost/itemWeight) == median:
			equal.append((itemCost, itemWeight))
		else:
			higher.append((itemCost, itemWeight))

	# Computing total weight of higher subset
	higherTotalWeight = sum([w for c,w in higher])

	totalWeight = 0;
	totalCost = 0;

	# Does the sum of the wieght of the higher subset exceed the max capacity?
	if higherTotalWeight > maxWeight:
		# The optimal set of items exists in this subset
		# Calling the algorithm again on this subset
		return FractionalKnapsackMedian([c for c,w in higher], [w for c,w in higher], maxWeight)
	else:
		# The higher subset are all in the knapsack, adding them
		totalWeight = higherTotalWeight
		totalCost = sum([c for c,w in higher])

		# Adding items that have ratios equal to the median to the knapsack
		# Until either the knapsack is full, or there are no more items left
		for itemCost, itemWeight in equal:
			# If the current item does not fit in the knapsack completely
			if totalWeight + itemWeight > maxWeight:
				# Take a fraction of the item
				fraction = float( (maxWeight - totalWeight) / itemWeight)
				fractionCost = itemCost * fraction
				totalCost += fractionCost
				# Return total cost, as the knapsack is full
				return totalCost
			# Item fits in knapsack completely
			else:
				# Add item to knapsack and continue
				totalWeight += itemWeight
				totalCost += itemCost

		# If this point is reached, then there is still space within the knapsack
		# Calling the algorithm again on the lower subset with a smaller max capacity
		newMaxWeight = maxWeight - totalWeight
		additionalCost = FractionalKnapsackMedian([c for c,w in lower], [w for c,w in lower], newMaxWeight)
		return totalCost + additionalCost

if __name__ == "__main__":

	print("Fractional Knapsack Problem")

	costs = 	[4, 1, 10, 2]
	weights = 	[7, 1, 9, 1]
	maxWeight = 13

	maximum = FractionalKnapsackSort(costs, weights, maxWeight)

	print("For items with {} costs and {} weights\nand a knapsack of size {}, the max is {}".format(costs, weights, maxWeight, maximum))

	maximum = FractionalKnapsackMedian(costs, weights, maxWeight)

	print("For items with {} costs and {} weights\nand a knapsack of size {}, the max is {}".format(costs, weights, maxWeight, maximum))





