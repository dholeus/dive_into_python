def info(object, spacing=10, collapse=1):
	"""Print methods and doc strings of modules, classes, etc."""
	methodList = [method for method in dir(object) if callable(getattr(object, method))]
	processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	print "\n".join(["%s %s" %
						(method.ljust(spacing),
						processFunc(str(getattr(object, method).__doc__)))
						for method in methodList])

if __name__ == "__main__":
	print info.__doc__

#arguments are a dictionary. Can be called in any order by naming them.
#str() converts pretty much anything(any object) into a string
#dir() returns a list of attributes and methods of any object
#type, str, dir and rest of python's funcitons are grouped into a module "__builtin__"
#getattr() returns any attribute of any object. Return value is the attribute(method)
#lambda function take many arguments and returns value of a "single" expression


	
