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
	""" Classe concernant uniquement les boites, et leur dictionnaires et listes associés """

	def __init__(self, nomboite): 	
		self.__nomboite = nomboite
		self.__listGene = list()
		self.__listCond = list()
		self.__dicoWell = dict()
		

		print self.__run()


	def __run(self):

		if self.__getlistGene()== "erreur gene" : return "erreur gene"
		else : self.__listGene=self.__getlistGene() 
		
		if self.__getlistCond() == "erreur condition" : return "erreur condition"
		else : self.__listCond=self.__getlistCond()

		if self.__getdicoWell() == "erreur puit" : return "erreur puit"
		else : self.__dicoWell=self.__getdicoWell() 
	
		
		return "ok"


	
	def __getlistGene(self):
		pass
	
	def __getlistCond(self):
		pass
		
			
	def __getdicoWell(self):
		pass

		
	

# ------------------------------ Propriétés de la classe "Boite" ------------------------------

	genes=property(__getlistGene, doc = "Liste des gènes ...=")
	conds=property(__getlistCond, doc = "Liste des conditions ...=")
	dicoW=property(__getdicoWell, doc = "dictionnaire ...=")
	

# ****************************** Fin de la classe "Boite" ******************************		

# TEST DE LA CLASSE

if __name__ == "__main__" :
	boite=Boite("20130227_102727_525")
	print boite.genes
	print boite.conds
	print boite.dicoW
	


	