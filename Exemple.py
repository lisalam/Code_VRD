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
class Exemple():
	""" Ceci est un exemple de base d'une classe"""
	
	def __init__(self, message="message par defaut"):	
		self.__message = message

	def func1(self, texte):
		print texte

	def func2(self):
		print self.__message

	def func3(self) :
		self.__priv1()

	def __priv1(self) :
		print self.__message
	
	
#**************** Fin de la classe Exemple ******


# ----------------------------------------------------------------------------
#   TEST DE LA CLASSE  

if __name__ == "__main__" :
	exemple=Exemple()

	exemple.func2()

	
