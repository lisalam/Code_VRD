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

from Data import Data

# ****************************** Début de la classe "Boite" ******************************

class Boite(object):
	""" Classe concernant uniquement les boites, et leur dictionnaires et listes associés """

	def __init__(self, nomboite, projet): 	
		self.__nomboite = nomboite
		self.__listGene = list()
		self.__listCond = list()
		self.__dicoWell = dict()
		self.__projet = projet
		self.__data = Data(self.__projet)

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
		dicolignes = self.__data.getdicolignes(self.__nomboite)
		#print dicolignes.keys()
		#print dicolignes[0], dicolignes[1]
		
		
		

	def __getNom(self) : return self.__nomboite

	def __getProjet(self) : return self.__projet

	def __setProjet(self, projet) : self.__projet = projet


# ------------------------------ Propriétés de la classe "Boite" ------------------------------

	genes=property(__getlistGene, doc = "Liste des gènes ...=")
	conds=property(__getlistCond, doc = "Liste des conditions ...=")
	dicoW=property(__getdicoWell, doc = "dictionnaire ...=")
	nom =property(__getNom, doc = " ...=")
	projet=property(__getProjet, __setProjet , doc = " ...=")
	

# ****************************** Fin de la classe "Boite" ******************************		

# TEST DE LA CLASSE

if __name__ == "__main__" :
	boite=Boite("20130227_102727_525", "/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools")
	#print boite.genes
	#print boite.conds
	#print boite.dicoW
	#print boite.nom
	#print boite.projet
	


	