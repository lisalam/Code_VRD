# -*- coding: iso-8859-15 -*-

import sys
import os
import os.path as path
import getpass


username=getpass.getuser()

mypath=os.path.expanduser(os.path.join("~","Dropbox","Macros_Lisa","Code_VRD"))
sys.path.append(mypath)

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


#**************** Debut de la classe Exemple ******
class Data():
	""" Ceci est un exemple de base d'une classe"""
	
	def __init__(self):	
		pass
	
	
#**************** Fin de la classe Exemple ******


# ----------------------------------------------------------------------------
#   TEST DE LA CLASSE  

if __name__ == "__main__" :
	data=Data()

	
