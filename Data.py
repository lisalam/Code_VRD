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
		self.__listboites=self.__getlisteboites()
		self.__dicoText = dict()
		self.__boiteGene = dict()
		self.__boiteN = dict()
		self.__boiteB = dict()
		self.__boitecond = dict()

		print self.__run()		

	def __run(self) :

		if self.__getdicoText() == "erreur dossiers" : return "erreur dossiers"
		else : self.__dicoText = self.__getdicoText()

		if self.__getboiteGene() == "erreur dossiers" : return "erreur dossiers"
		else : self.__boiteGene == self.__getboiteGene()

		if self.__getboiteN() == "erreur dossiers" : return "erreur dossiers"
		else : self.__boiteN == self.__getboiteN()

		if self.__getboiteB() == "erreur dossiers" : return "erreur dossiers"
		else : self.__boiteB == self.__getboiteB()

		if self.__getboitecond() == "erreur dossiers" : return "erreur dossiers"
		else : self.__boitecond == self.__getboitecond()
		

		return "ok"


	def __getboitecond(self):
		for i in range(len(self.__listboites)):
			pass
			#self.__getboitecond[self.__listboites[i]]=listecond

		
	
	def __getboiteN(self):
		tempdico=dict()
		for i in range(len(self.__listboites)):
			boite=self.__listboites[i]
			f=self.__dicoText[boite]
			fichier=open(f,"r")
			alllines = fichier.readlines()[0]
			ligne = alllines.split("\r")[1]
			ligne = ligne.split("\t")
			nb = ligne[4]
			tempdico[boite]=(nb, boite)
		return tempdico

		

		
	def __getboiteB(self):
		tempdico=dict()
		for i in range(len(self.__listboites)):
			boite=self.__listboites[i]
			f=self.__dicoText[boite]
			fichier=open(f,"r")
			alllines = fichier.readlines()[0]
			ligne = alllines.split("\r")[1]
			ligne = ligne.split("\t")
			nb = ligne[4]
			tempdico[nb]=(nb, boite)
		return tempdico


	def __getdicoText(self) :
		tempdico=dict()
		tempboites=os.listdir(self.__projet) # récupération listes de dossiers et des fichiers
		if len(tempboites)<2 : return "erreur dossiers"
		listpaths=[os.path.join(self.__projet,v) for v in tempboites if os.path.isdir(os.path.join(self.__projet,v))] # liste en intensions, ne garde que les dossiers et les transforment en "path" complet 
		for i in range(len(self.__listboites)):
			mot=os.path.join(listpaths[i],"Texte",(self.__listboites[i]+"_labels.txt"))
			if os.path.isfile(mot):
				tempdico[self.__listboites[i]]=mot

		return tempdico

		

	def __getboiteGene(self) :
		pass

	def __getDicoLignes(self, boite) :
		f = self.__dicoText[boite]
		fichier = open(f,"r") #ouvrir le fichier en lecture seule
		alllines=fichier.readlines() # lire toutes les lignes du fichier
		alllines=alllines[0].split("\r") # on veut lire la première ligne [0] et séparer les éléments de la ligne (ici le fichier excel fait que l'on a qu'une ligne dans tout le fichier)
		dicoligne=dict() # création d'un dictionnaire pour les lignes
		for i in range(1,len(alllines)): # boucle avec index
			ligne=alllines[i].split("\t")
			dicoligne[i]=ligne # ligne est une liste pour laquelle chaque valeur est une des colonnes du fichier texte initial

		return dicoligne

	def __getlisteboites(self):
		tempboites=os.listdir(self.__projet) # récupération listes de dossiers et des fichiers
		listboites=[v for v in tempboites if os.path.isdir(os.path.join (self.__projet,v))] # tous les dossiers de mon répertoire
		return listboites
	

	
#**************** Fin de la classe Exemple ******


# ----------------------------------------------------------------------------
#   TEST DE LA CLASSE  

if __name__ == "__main__" :
	data=Data("/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools")

	
