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
		self.__dicoBoiteCond = dict()
		self.__dicoBoiteUID = dict()
		self.__dicoBoiteCondInv = dict()
		
		print self.__run()


	def __run(self):

		if self.__getlisteboites()== "erreur dossiers" : return "erreur dossiers"
		else : self.__listeboites=self.__getlisteboites() 
		
		if self.__getlisteCondBoite() == "erreur boite" : return "erreur boite"
		else : self.__listeCondBoite=self.__getlisteCondBoite()

		if self.__getdicoBoiteCond() == "erreur boite" : return "erreur boite"
		else : self.__dicoBoiteCond=self.__getdicoBoiteCond() 
	
		if self.__getdicoBoiteUID() == "erreur boite" : return "erreur boite"
		else : 	self.__dicoBoiteUID = self.__getdicoBoiteUID() 

		if self.__getdicoBoiteCondInv() == "erreur boite" : return "erreur boite"
		else : self.__dicoBoiteCondInv == self.__getdicoBoiteCondInv()

		
		return "ok"


	
	def __getBoiteCond(self, boite):
		tempdico=dict()
		for b in self.__listeCondBoite :
			dicolignes = self.__getdicolignes(b) # recupere le dictionnaire pour la boite avec ttes les lignes du fichier texte
			listecond=list()
			enscond=set()
			for l in dicolignes.values() :
				enscond.add(l[self.__COL_COND])
				for i in range(len(enscond)) : listecond.append(enscond.pop())

		return tempdico

	
	def __getlisteCondBoite(self):
		pass
		
			

	def __getdicoBoiteUID(self):
		pass

		

	def __getdicoBoiteCondInv(self):
		pass

# ------------------------------ Propriétés de la classe "Boite" ------------------------------











# ****************************** Fin de la classe "Boite" ******************************		

# TEST DE LA CLASSE

if __name__ == "__main__" :
	boite=Boite 


	