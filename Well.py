

def f(**param) :
	if len(param) != 1 : return "erreur params"
	elif param.keys()[0] != "code" and param.keys()[0] != "lc" : 
		print param.keys()[0]
		return "erreur cles"
	elif param.keys()[0] == "code" : calculerLC(param["code"])
	else : calculerCode(param["lc"])

def calculerCode(lc) :
	print lc

def calculerLC(code) :
	print code

print "--- debut ---"

print f(lc=(2,5))
print f(code="B8")