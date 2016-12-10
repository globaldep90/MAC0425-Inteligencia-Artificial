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

		counter = util.Counter()
		counter.incrementAll( labels , 1 )
		self.guess = counter.argMax()
		
		self.tree = self.buildTree( data , labels )


		# print counter
		# print self.guess

	def buildTree( self , data , labels , depth = 0 ) :
		""" Recursive function to learn the tree model """
		"*** YOUR CODE HERE ***"
		# print labels
		# util.raiseNotDefined()
		tree = DecisionNode(self.bestSplit(data, labels), None, self.guess)
		# print "tree"
		# print tree.label
		return tree

	def isLeaf( self , data , labels , depth ) :
		""" Verify stop conditions (whether to split is necessary) """
		"*** YOUR CODE HERE ***"
		if depth >= self.maxdepth:
			return True
		counter = util.Counter()
		counter.incrementAll(labels, 1)
		if counter[0] == 0 or counter[1]==0:
			return True
		return all(data[0] == d for d in data)

	def getMostFrequentLabel( self , labels ) :
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()

	# def bestSplit( self , data , labels ) :
	# 	""" Get the best variable to split the dataset using the metric function """
	# 	"*** YOUR CODE HERE ***"
	# 	# util.raiseNotDefined()
	# 	print "data", data
	# 	val = float("inf")
	# 	res = 0
	# 	vars = util.Counter()
	# 	vars.incrementAll(labels, 1)
	# 	for var in vars.keys():
	# 		# vars[var] = entropy(labels)
	# 		# set1 = []
	# 		# set2 = []
	# 		set1 = vars.copy()
	# 		set2 = vars.copy()
	# 		for var2 in vars:
	# 			if var2 <= var:
	# 				# set1.append(var2)
	# 				set2[var2] = 0
	# 			else:
	# 				# set2.append(var2)
	# 				set1[var2] = 0
	# 		temp = (set1.totalCount()*metrics.entropy(set1) + set2.totalCount()*metrics.entropy(set2))/vars.totalCount()
	# 		print vars, set1, set2
	# 		print temp
	# 		if val>temp:
	# 			val = temp
	# 			res = var
	# 	return res
	# 	# return vars.argMax()

	def bestSplit( self , data , labels ) :
		""" Get the best variable to split the dataset using the metric function """
		"*** YOUR CODE HERE ***"
		# util.raiseNotDefined()
		# print "data", data
		# print "metric", self.metric
		print len(data)
		val = float("inf")
		res = 0
		vars = len(data[0])
		n = len(data)
		# print 
		# vars = util.Counter()
		# vars.incrementAll(labels, 1)
		for var in range(vars):
			# vars[var] = entropy(labels)
			set0 = []
			set1 = []
			# set0 = vars.copy()
			# set1 = vars.copy()
			for i in range(n):
				if data[i][var] == 0:
					set0.append(labels[i])
					# set1[var2] = 0
				else:
					set1.append(labels[i])
					# set0[var2] = 0
			# temp = (len(set0)*metrics.entropy(set0) + len(set1)*metrics.entropy(set1))/vars
			temp = (len(set0)*metrics.entropy(set0) + len(set1)*metrics.entropy(set1))/n
			# temp = (len(set0)*metrics.error(set0) + len(set1)*metrics.error(set1))/vars
			# print vars, set0, set1
			print var, temp, len(set0), len(set1)
			if val>temp:
				val = temp
				res = var
		return res
		# return vars.argMax()


	def divideSet( self , data , label , variable ) :
		"""
		Given a variable, split the data set and labels in two sets.
		One data set with instances having variable as 0 and the
		other with instances having variable as 1
		"""
		"*** YOUR CODE HERE ***"
		# util.raiseNotDefined()
		n = len(data)
		set0 = []
		set1 = []
		for i in range(n):
			if data[i][variable]==0:
				set0.append(data[i])
			else:
				set1.append(data[i])
		return (set0, set1)


	def classify( self , testData ) :
		"""
		Classify all test data using the learned tree model
		"""
		"*** YOUR CODE HERE ***"
		# util.raiseNotDefined()
		# return [ self.guess for i in testData ]
		print "yay"
		print self.guess
		return self.guess
