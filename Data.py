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
	
	def __init__(self, projet):	
		self.__projet = projet
		self.__dicoText = dict()
		self.__boiteGene = dict()
		self.__boiteN = dict()
		self.__boiteB = dict()
		self.__boitecond = dict()

		print self.__run()		

	def __run(self) :

		if self.__builddicoText() == "erreur dossiers" : return "erreur dossiers"
		else : self.__dicoText = self.__builddicoText()
		
		self.__boiteGene = self.__buildboiteGene()

		return "ok"

	def __builddicoText(self) :
		tempdico=dict()
		tempboites=os.listdir(self.__projet) # récupération listes de dossiers et des fichiers
		if len(tempboites)<2 : return "erreur dossiers"
		listpaths=[os.path.join(self.__projet,v) for v in tempboites if os.path.isdir(os.path.join(self.__projet,v))] # liste en intensions, ne garde que les dossiers et les transforment en "path" complet 
		listboites=[v for v in tempboites if os.path.isdir(os.path.join (self.__projet,v))] # tous les dossiers de mon répertoire
		for i in range(len(listboites)):
			mot=os.path.join(listpaths[i],"Texte",(listboites[i]+"_labels.txt"))
			if os.path.isfile(mot):
				tempdico[listboites[i]]=mot

		return tempdico

		

	def __buildboiteGene(self) :
		pass
	
#**************** Fin de la classe Exemple ******


# ----------------------------------------------------------------------------
#   TEST DE LA CLASSE  

if __name__ == "__main__" :
	data=Data("/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools")

	
