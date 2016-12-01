from copy import deepcopy as copy
import util
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
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()

	def isLeaf( self , data , labels , depth ) :
		""" Verify stop conditions (whether to split is necessary) """
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()

	def getMostFrequentLabel( self , labels ) :
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()

	def bestSplit( self , data , labels ) :
		""" Get the best variable to split the dataset using the metric function """
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()

	def divideSet( self , data , label , variable ) :
		"""
		Given a variable, split the data set and labels in two sets.
		One data set with instances having variable as 0 and the
		other with instances having variable as 1
		"""
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()

	def classify( self , testData ) :
		"""
		Classify all test data using the learned tree model
		"""
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()
