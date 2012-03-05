#dive into python example 2.1
def buildConnectionString(params):
	"""Build a connection string from a dictionary of parameters.
	returns a string."""
	return ";".join(["%s=%s" % (k,v) for k, v in params.items()])

if __name__ == "__main__":	#name is main when this module is run directly, when imported as a module, name will be something else
	myParams = {"server":"donoghue","database":"master","uid":"sa","pwd":"secret"}
	print buildConnectionString(myParams)
