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

# ****************************** Début de la classe "Boite" ******************************

class Boite():
	""" Classe concernant uniquement les boites, et leur dictionnaires associés """

	def __init__(self, boite): 	
		self.__boite = boite
		self.__dicocond = dict()
		self.__dicoBUID = dict()
		self.__dicocondinv = dict()
		
		print self.__run()


	def __run(self):
		