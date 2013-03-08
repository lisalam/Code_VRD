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


#**************** Debut de la classe Data ******
class Data():
	""" Classe principale des donnees construit tous les dictionnaires au niveau du projet """
	
	#"init" permet d'initialiser
	
	def __init__(self, projet): # le self rend l'action privée, propre au programmeur	
		self.__projet = projet
		self.__dicoText = dict()
		self.__boiteGene = dict()
		self.__boiteN = dict()
		self.__boiteB = dict()
		self.__boitecond = dict()
		
		print self.__run()		

# création des dictionnaires vides que l'on va utiliser, dans la fonction init, on aura plus qu'à appeler la fonction pour la faire marcher après

	def __run(self) :

		if self.__getlisteboites()== "erreur dossiers" : return "erreur dossiers"
		else : self.__listeboites=self.__getlisteboites() 
	
		if self.__getdicoText() == "erreur dossiers" : return "erreur dossiers"
		else : 	self.__dicoText = self.__getdicoText() # dans la fonction run, remplir le dictionnaire si il n'y pas "erreur dossiers"

		if self.__GenerateTitre() == "erreur dans les colonnes" : "erreur dans les colonnes"

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
		for i in range(len(self.__listeboites)):
			listecond=list()
			self.__boitecond[self.__listeboites[i]]=listecond # la clé du dictionnaire est le nom de boite et la valeur sont les conditions présentes dans la boite

		return listecond # on retourne la liste des conditions présentes dans la boite que l'on aura appeler 

	
	def __getboiteN(self): # la clé est le nom de la boite et la clé est le numéro et le nom de la boite
		tempdico=dict()
		for i in range(len(self.__listeboites)): # pour chaque ligne de chaque dossier de mon répertoire
			boite=self.__listeboites[i] 
			f=self.__dicoText[boite]
			fichier=open(f,"r") # ouvrir le fichier en lecture seule
			alllines = fichier.readlines()[0] # lire chaque ligne du fichier, ici on veut lire que la première ligne
			ligne = alllines.split("\r")[0] # on coupe la ligne avec "\r"
			ligne = ligne.split("\t") # on splitte au niveau des tabulations la ligne déjà splittée avant
			nb = ligne[self.__COL_BOITE]
			tempdico[boite]=(nb, boite) # le dictionnaire temporaire tempdico a pour clé la boite et pour valeur son numéro et son nom de boite (son nom de fichier)
		
		
		return tempdico

		
	def __getboiteB(self):
		tempdico=dict()
		for i in range(len(self.__listeboites)):
			boite=self.__listeboites[i]
			f=self.__dicoText[boite]
			fichier=open(f,"r")
			alllines = fichier.readlines()[0]
			ligne = alllines.split("\r")[1]
			ligne = ligne.split("\t")
			nb = ligne[4]
			tempdico[nb]=(nb, boite)
			
		return tempdico


	def __getdicoText(self) : # nom du dossier et chemin du user au fichier texte correspondant au dossier 
		tempdico=dict()
		tempboites=os.listdir(self.__projet) # récupération listes de dossiers et des fichiers
		if len(tempboites)<2 : return "erreur dossiers"
		listpaths=[os.path.join(self.__projet,v) for v in tempboites if os.path.isdir(os.path.join(self.__projet,v))] # liste en intensions, ne garde que les dossiers et les transforment en "path" complet 
		for i in range(len(self.__listeboites)):
			mot=os.path.join(listpaths[i],"Texte",(self.__listeboites[i]+"_labels.txt"))
			if os.path.isfile(mot):
				tempdico[self.__listeboites[i]]=mot
		
		return tempdico # 

		

	def __getboiteGene(self) : # dictionnaire qui au nom de la boite sort tous les gènes contenus dans cette boite
		for i in range(len(self.__listeboites)):
			listegenes=list()
			self.__boiteGene[self.__listeboites[i]]=listegenes

		return listegenes
			

	def __getDicoLignes(self, boite) :
		f = self.__dicoText[boite]
		fichier = open(f,"r") #ouvrir le fichier en lecture seule
		alllines=fichier.readlines() # lire toutes les lignes du fichier
		alllines=alllines[0].split("\r") # on veut lire la première ligne [0] et séparer les éléments de la ligne (ici le fichier excel fait que l'on a qu'une ligne dans tout le fichier)
		dicoligne=dict() # création d'un dictionnaire pour les lignes
		for i in range(0,len(alllines)): # boucle avec index
			ligne=alllines[i].split("\t")
			dicoligne[i]=ligne # ligne est une liste pour laquelle chaque valeur est une des colonnes du fichier texte initial
			
		return dicoligne # renvoi un dictionaire pour boite donnée avec toute les lignes sous forme de liste du fichier texte, la clé est le n° de ligne

	def __getlisteboites(self):		
		tempboites=os.listdir(self.__projet) # récupération listes de dossiers et des fichiers
		if len(tempboites)<2 : return "erreur dossiers"
		listeboites=[v for v in tempboites if os.path.isdir(os.path.join (self.__projet,v))] # tous les dossiers de mon répertoire		
		return listeboites


	def __GenerateTitre(self): # création de constantes qui seront fixes, pour pas appeler à chaque fois le numéro de la colonne qui nous interesse
		dicoligne = self.__getDicoLignes(self.__listeboites[0])
		titre=dicoligne[0]
		for i in range(len(titre)):
			if titre[i]=="Condition": 
				self.__COL_BOITE = i
				continue
			if titre[i]=="Jobrun Name": 
				self.__COL_JOBRUNNAME = i
				continue
			if titre[i]=="File Name": 
				self.__COL_FILENAME = i
				continue
			if titre[i]=="Frame Time": 
				self.__COL_FRAMETIME = i
				continue
			if titre[i]=="numero de boite": 
				self.__COL_NUMEROBOITE = i
				continue
			if titre[i]=="Genes": 
				self.__COL_GENES = i
				continue
			if titre[i]=="Well": 
				self.__COL_WELL = i
				continue
			if titre[i]=="Well Index": 
				self.__COL_WELLINDEX = i
				continue
			if titre[i]=="PointLoop Index": 
				self.__COL_POINTLOOPINDEX = i
				continue
			if titre[i]=="WellLoop Index": 
				self.__COL_WELLLOOPINDEX = i
				continue
			if titre[i]=="X": 
				self.__COL_X = i
				continue
			if titre[i]=="Y": 
				self.__COL_Y = i
				continue
			if titre[i]=="Z1": 
				self.__COL_Z1 = i
				continue
			if titre[i]=="Frame Index": 
				self.__COL_FRAMEINDEX = i
				continue
			if titre[i]=="plateRow": 
				self.__COL_LIGNE = i
				continue
			if titre[i]=="plateColumn": 
				self.__COL_COL = i
				continue
			if titre[i]=="UIDs": 
				self.__COL_UIDS = i
				continue

		else : return "erreur dans les colonnes"

		return "ok"

				
				
				
	

	
#**************** Fin de la classe Data ******


# ----------------------------------------------------------------------------
#   TEST DE LA CLASSE  

if __name__ == "__main__" :
	data=Data("/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools")

	
