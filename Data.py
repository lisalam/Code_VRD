# -*- coding: iso-8859-15 -*-

import sys
import os
import os.path as path
import getpass
import re

username=getpass.getuser()

mypath=os.path.expanduser(os.path.join("~","Dropbox","Macros_Lisa","Code_VRD"))
sys.path.append(mypath)

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')

#**************** Debut de la classe Data ******
class Data(object):
	""" Classe principale des donnees construit tous les dictionnaires au niveau du projet """
	
	#"init" permet d'initialiser
	
	def __init__(self, projet): # le self rend l'action privée, propre au programmeur	
		self.__projet = projet
		self.__dicoText = dict()
		self.__dicoGene = dict()
		self.__dicoNumBoite = dict()
		self.__dicoNomBoite = dict()
		self.__dicoCond = dict()
		self.__flagdicoCond = 0
		self.__flagdicoGene = 0
		self.dicolignes = dict()
		
		print self.__run()		

# création des dictionnaires vides que l'on va utiliser, dans la fonction init, on aura plus qu'à appeler la fonction pour la faire marcher après

	def __run(self) :

		if self.__getlisteboites()== "erreur dossiers" : return "erreur dossiers"
		else : self.__listeboites=self.__getlisteboites()
			
		if self.__getdicoText() == "erreur dossiers" : return "erreur dossiers"
		else : 	self.__dicoText = self.__getdicoText() # dans la fonction run, remplir le dictionnaire si il n'y pas "erreur dossiers"

		self.__makedicolignes()
		
		if self.__GenerateTitre() == "erreur dans les colonnes" : return "erreur dans les colonnes"
		else : pass

		if self.__getdicoGene() == "erreur dossiers" : return "erreur dossiers"
		else : self.__dicoGene = self.__getdicoGene()

		if self.__getdicoNumBoite() == "erreur dossiers" : return "erreur dossiers"
		else : self.__dicoNumBoite = self.__getdicoNumBoite()

		if self.__getdicoNomBoite() == "erreur dossiers" : return "erreur dossiers"
		else : self.__dicoNomBoite = self.__getdicoNomBoite()

		#print "self.__dicoNumBoite :"
		#print self.__dicoNumBoite
		#print "self.__dicoNomBoite :"
		#print self.__dicoNomBoite
		#print "self.__dicoCond :"
		#print self.__getdicoCond()

		return "ok"


	def __getdicoCond(self): 
		
		self.__flagdicoGene = 1
		
		tempdico=dict()
		for b in self.__listeboites :
			dicolignes = self.dicolignes[b] # recupere le dictionnaire pour la boite avec ttes les lignes du fichier texte
			listecond=list()
			enscond=set()
			for i in range(1, len(dicolignes)-1) :
				enscond.add(dicolignes[i][self.COL_COND])
			for i in range(len(enscond)) : listecond.append(enscond.pop())

			tempdico[b]=listecond
			
		return tempdico # renvoi un dict avec pour toutes les boites toutes les conditions presentes dans la boite.			

	
	def __getdicoNumBoite(self): # la clé est le nom de la boite et la clé est le numéro et le nom de la boite
		tempdico=dict()
		for i in range(len(self.__listeboites)): # pour chaque ligne de chaque dossier de mon répertoire
			boite=self.__listeboites[i]
			f=self.__dicoText[boite]
			fichier=open(f,"r") # ouvrir le fichier en lecture seule
			alllines = fichier.read() # lire chaque ligne du fichier, ici on veut lire que la première ligne
			sep=self.getLineSep(alllines)
			#sep="\r"
			ligne = alllines.split(sep) # on coupe la ligne avec "\r" ou avec "\n"
			ligne1 = ligne[1]
			listvals = ligne1.split("\t") # on splitte au niveau des tabulations la ligne déjà splittée avant
			nb = listvals[self.COL_NUMEROBOITE]
			tempdico[boite]=(nb, boite) # le dictionnaire temporaire tempdico a pour clé la boite et pour valeur son numéro et son nom de boite (son nom de fichier)
		
		
		return tempdico

		
	def __getdicoNomBoite(self):
		tempdico=dict()
		for i in range(len(self.__listeboites)):
			boite=self.__listeboites[i]
			f=self.__dicoText[boite]
			fichier=open(f,"r")
			alllines = fichier.read()
			sep=self.getLineSep(alllines)
			ligne = alllines.split(sep)
			ligne1 = ligne[1]
			listvals = ligne1.split("\t")
			nomb = listvals[self.COL_FOLDER]
			numb = listvals[self.COL_NUMEROBOITE]
			tempdico[numb]=(numb, nomb)
			
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
		
		return tempdico 

		

	def __getdicoGene(self): 
		self.__flagdicoGene = 1
		tempdico=dict()
		for boite in self.__listeboites :
			dicolignes =  self.dicolignes[boite] # recupere le dictionnaire pour la boite avec ttes les lignes du fichier texte
			listegene=list()
			ensgene=set()
			for i in range(1, len(dicolignes)-1) :
				#print dicolignes[i]
				ensgene.add(dicolignes[i][self.COL_GENES])
			for i in range(len(ensgene)) : listegene.append(ensgene.pop())
			tempdico[boite]=listegene
		return tempdico
			

	def __makedicolignes(self) :
		
		for boite in self.__listeboites :
			f = self.__dicoText[boite]
			fichier = open(f,"r") #ouvrir le fichier en lecture seule
			alllines=fichier.readlines() # lire toutes les lignes du fichier renvoi une liste avec tout le fichier
			alllines = "".join(alllines)
			alllines = alllines.replace(" ","_")
			alllines=re.split("[(\r\n), (\r), (\n), (\n\r)]+", alllines)
			dicolignes=dict() # création d'un dictionnaire pour les lignes
			for i in range(0,len(alllines)): # boucle avec index
				ligne=alllines[i].split("\t")
				if len(ligne) >1 : dicolignes[i]=ligne # ligne est une liste pour laquelle chaque valeur est une des colonnes du fichier texte initial

			self.dicolignes[boite] = dicolignes

	def __getlisteboites(self):		
		tempboites=os.listdir(self.__projet) # récupération listes de dossiers et des fichiers
		if len(tempboites)<2 : return "erreur dossiers"
		listeboites=[v for v in tempboites if os.path.isdir(os.path.join (self.__projet,v))] # tous les dossiers de mon répertoire		
		return listeboites


	def __GenerateTitre(self): # création de constantes qui seront fixes, pour pas appeler à chaque fois le numéro de la colonne qui nous interesse
		dicolignes = self.dicolignes[self.__listeboites[0]]
		titre=dicolignes[0]
#		print titre
#		for v in titre : print v
		for i in range(0,len(titre)):
#			print i
			if titre[i]=="Jobrun_Folder": 
				self.COL_FOLDER = i
				#print i,  "Jobrun Folder"
				continue
			if titre[i]=="Condition": 
				self.COL_COND = i
				#print i,  "Condition"
				continue
			if titre[i]=="Jobrun_Name": 
				self.COL_JOBRUNNAME = i
				#print i,  "Jobrun Name"
				continue
			if titre[i]=="File_Name": 
				self.COL_FILENAME = i
				#print i,  "File Name"
				continue
			if titre[i]=="Frame_Time": 
				self.COL_FRAMETIME = i
				#print i,  "Frame Time"
				continue
			if titre[i]=="Genes": 
				self.COL_GENES = i
				#print i,  "Genes"
				continue			
			if titre[i]=="Well": 
				self.COL_WELL = i
				#print i,  "Well"
				continue			
			if titre[i]=="Well_Index": 
				self.COL_WELLINDEX = i
				#print i,  "Well Index"
				continue
			if titre[i]=="PointLoop_Index": 
				self.COL_POINTLOOPINDEX = i
				#print i,  "PointLoop Index"
				continue
			if titre[i]=="WellLoop_Index": 
				self.COL_WELLLOOPINDEX = i
				#print i,  "WellLoop Index"
				continue
			if titre[i]=="X": 
				self.COL_X = i
				#print i,  "X"
				continue
			if titre[i]=="Y": 
				self.COL_Y = i
				#print i,  "Y"
				continue
			if titre[i]=="Z1": 
				self.COL_Z1 = i
				#print i,  "Z1"
				continue
			if titre[i]=="Frame_Index": 
				self.COL_FRAMEINDEX = i
				#print i,  "Frame Index"
				continue
			if titre[i]=="TimeLapse_Index": 
				self.COL_TLINDEX = i
				#print i,  "TimeLapse Index"
				continue
			if titre[i]=="numerodeboite": 
				self.COL_NUMEROBOITE = i
				#print i,  "numerodeboite"
				continue			
			if titre[i]=="plateRow": 
				self.COL_LIGNE = i
				#print i,  "plateRow"
				continue
			if titre[i]=="plateColumn": 
				self.COL_COL = i
				#print i,  "plateColumn"
				continue				
			if titre[i].split("\r")[0]=="UIDs": 
				self.COL_UIDS = i
				#print i,  "UIDs"
				continue

		else : return "erreur dans les colonnes "+str(i)

		return "ok"

	def getLineSep(self, texte) :
		t1=texte.split("\r")
		t2=texte.split("\n")
		if len(t1)>len(t2) : return "\r"
		else : return "\n"

	def __createDicoG(self) :
		if self.__flagdicoGene == 0 : self.__getdicoGene()
		return self.__dicoGene

	def __createDicoC(self) :
		if self.__flagdicoCond == 0 : self.__getdicoCond()
		return self.__dicoCond


# -------- propriétés de la classe Data --------

	dicoG=property(__getdicoGene, doc="dictionnaire  ... =")  #renvoi un dictionnaire avec comme clé toutes les boites et en valeur tous les genes
	dicoC=property(__getdicoCond, doc="dictionnaire ...=")    #renvoi un dictionnaire avec comme clé toutes les boites et en valeur tous les conditions
	listB=property(__getlisteboites, doc="liste ...=")        #renvoi une liste avec toutes les boites du projet (= dossier)
	dicoNumB=property(__getdicoNumBoite, doc="dictionnaire ...=") #renvoi un dictionnaire avec comme clé toutes les noms des boites et en valeur le n° et le nom de la boite
	dicoNomB=property(__getdicoNomBoite, doc="dictionnaire ...=")	#renvoi un dictionnaire avec comme clé tous les n° des boites et en valeur le n° et les noms des boites correspondant a ce n°
	
# **************** Fin de la classe Data *****************



# ----------------------------------------------------------------------------
#   TEST DE LA CLASSE  

if __name__ == "__main__" :
	data=Data("/Users/lisalamasse/Desktop/Metasensors HCS/Bacillus_Ibidi_96well_angio1")
	#print "dicoG", data.dicoG
	#print "----- fin dicoG -----"
	#print data.dicoC
	#print "----- fin dicoC -----"
	#print data.listB
	#print "----- fin listB -----"
	#print data.dicoNumB
	#print "----- fin dicoNumB -----"
	#print data.dicoNomB
	#print "----- fin dicoNomB -----"
	#print data.dicolignes["20130410_183703_374"]
	

	
