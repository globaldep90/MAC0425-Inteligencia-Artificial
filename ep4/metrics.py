import sys
import math
import util

def gini( labels ) :
	"*** YOUR CODE HERE ***"
	# util.raiseNotDefined()
	# print labels
	counter = util.Counter()
	counter.incrementAll( labels , 1 )
	counter.normalize()
	res = 1
	for key in counter:
		res -= counter[key]*counter[key]
	return res

def error( labels ) :
	"*** YOUR CODE HERE ***"
	# util.raiseNotDefined()
	counter = util.Counter()
	counter.incrementAll( labels , 1 )
	counter.normalize()
	res = 1 - counter[counter.argMax()]
	return res

def entropy( labels ) :
	"*** YOUR CODE HERE ***"
	# util.raiseNotDefined()
	counter = util.Counter()
	counter.incrementAll( labels , 1 )
	counter.normalize()
	res = 0
	for key in counter:
		res -= counter[key]*math.log(counter[key])
	return res
