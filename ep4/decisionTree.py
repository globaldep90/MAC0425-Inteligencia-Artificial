# Yara Grassi Gouffon
# NUSP 4172560

from copy import deepcopy as copy
import util
import metrics
import classificationMethod

class DecisionNode :
	def __init__( self , column = -1 , value = None , label = None , leftchild = None , rightchild = None ) :
		self.column = column
		self.value = value
		self.label = label
		self.leftchild = leftchild
		self.rightchild = rightchild

	def __str__( self ) :
		"""
		Return a string representing the structure of DecisionNode
		This function will be implicitly called when printed a DecisionNode object using print function
		"""
		"*** YOUR CODE HERE (Optional) ***"
		util.raiseNotDefined()
		return 'Node'

class DecisionTreeClassifier( classificationMethod.ClassificationMethod ) :
	def __init__( self , legalLabels ) :
		self.guess = None
		self.type = "decisiontree"

	def train( self , data , labels , args ) :
		"""
		Learn the tree model
		"""
		self.maxdepth = int( args[ 'maxdepth' ] )
		self.metric = args[ 'metric' ]
		self.numrows = len( data )
		self.numcolumns = len( data[ 0 ] )
		self.tree = self.buildTree( data , labels )

	def buildTree( self , data , labels , depth = 0 ) :
		""" Recursive function to learn the tree model """
		if self.isLeaf(data, labels, depth):
			return DecisionNode(-1, None, self.getMostFrequentLabel(labels))

		split = self.bestSplit(data, labels)
		data0, data1, labels0, labels1 = self.divideSet(data, labels, split)
		return DecisionNode(split, None, None, self.buildTree(data0, labels0, depth+1), self.buildTree(data1, labels1, depth+1))

	def isLeaf( self , data , labels , depth ) :
		""" Verify stop conditions (whether to split is necessary) """
		if depth >= self.maxdepth:
			return True
		counter = util.Counter()
		counter.incrementAll(labels, 1)
		if counter[0] == 0 or counter[1]==0:
			return True
		return all(data[0] == d for d in data)

	def getMostFrequentLabel( self , labels ) :
		counter = util.Counter()
		counter.incrementAll( labels , 1 )
		return counter.argMax()

	def bestSplit( self , data , labels ) :
		""" Get the best variable to split the dataset using the metric function """
		val = float("inf")
		res = 0
		vars = len(data[0])
		n = len(data)
		for var in range(vars):
			set0 = []
			set1 = []
			for i in range(n):
				if data[i][var] == 0:
					set0.append(labels[i])
				else:
					set1.append(labels[i])
			temp = float(len(set0))/n*self.metric(set0)
			temp += float(len(set1))/n*self.metric(set1)
			if val>temp:
				val = temp
				res = var
		return res


	def divideSet( self , data , labels , variable ) :
		"""
		Given a variable, split the data set and labels in two sets.
		One data set with instances having variable as 0 and the
		other with instances having variable as 1
		"""
		"*** YOUR CODE HERE ***"
		n = len(data)
		data0 = []
		data1 = []
		labels0 = []
		labels1 = []
		for i in range(n):
			if data[i][variable]==0:
				data0.append(data[i])
				labels0.append(labels[i])
			else:
				data1.append(data[i])
				labels1.append(labels[i])
		return (data0, data1, labels0, labels1)


	def classify( self , testData ) :
		"""
		Classify all test data using the learned tree model
		"""
		results = []
		for t in testData:
			results.append(self.test(self.tree, t))
		return results

	def test(self, node, data):
		while node.column != -1:
			if data[node.column] == 1:
				node = node.rightchild
			else:
				node = node.leftchild
		return node.label
