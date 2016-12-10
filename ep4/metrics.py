import sys
import math
import util

def gini( labels ) :
	counter = util.Counter()
	counter.incrementAll( labels , 1 )
	counter.normalize()
	res = 1
	for key in counter:
		res -= counter[key]*counter[key]
	return res

def error( labels ) :
	counter = util.Counter()
	counter.incrementAll( labels , 1 )
	counter.normalize()
	return 1 - counter[counter.argMax()]

def entropy( labels ) :
	counter = util.Counter()
	counter.incrementAll( labels , 1 )
	counter.normalize()
	res = 0
	for key in counter:
		res -= counter[key]*math.log(counter[key])
	return res
