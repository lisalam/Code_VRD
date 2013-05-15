#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, sys
import time
import glob
import os.path as path
import getpass
import shutil
import random
import math

username=getpass.getuser()

mypath=os.path.expanduser(os.path.join("~","Dropbox","Macros_Lisa","Code_VRD"))
sys.path.append(mypath)

from Data import Data
from Boite import Boite
from Well import Well

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class Controleur(object):

	def __init__(self): 
		self.__projet = ""
		self.__nomboite = ""

		self.__PROJET = 0
		self.__NOM_BOITE = 1
		self.__NUME_BOITE = 2
		self.__GENES = 3
		self.__WELLS = 4		
		self.__CONDS  = 5
		self.__IMAGES = 6
		self.dico=dict()

		self.__KEYS = ["Projet", "Nom_Boite", "Num_Boite", "Genes", "Wells", "Condition", "Images"]
		
		self.__dCode = [False,False,False,False,False,False,False]

		self.__dicoDatas = dict()

		self.__dicoEns = dict()

		self.__dicoEnsEnd = dict()
		for key in self.__KEYS : self.__dicoEnsEnd[key] = set()

		self.__boite = None

	def setData(self, param) : 
		# tests dict ok...
		#if len(param) <3 : return False
		for v in param.keys() :
			if v in self.__KEYS : continue
			else : return False

		try : param[self.__KEYS[0]]
		except KeyError : return False
		# fin tests -----
		# on rempli un dictionnaire avec les valeur et un code
		for i in range(len(self.__KEYS)) :
			try : param[self.__KEYS[i]]
			except KeyError :
				self.__dCode[i] = False
			else : 
				self.__dicoDatas[i] = param[self.__KEYS[i]]
				self.__dCode[i] = True
		return True

	def decisionTree(self) :

		# on teste si le projet est toujours le meme :
		if self.__projet != self.__dicoDatas[self.__PROJET] : self.__data = Data(self.__dicoDatas[self.__PROJET])

		#on genere les ensembles par nom de boite si fourni
		if self.__dCode[self.__NOM_BOITE] :

			# les noms de boites et les numeros sont geres par la classe Data :			
			# -1-  l'ensemble pour la valeur fournir a forcement un seul element
			self.__dicoEnsEnd["Nom_Boite"] = set([self.__dicoDatas[self.__NOM_BOITE]])  

			#print self.__dicoEnsEnd["Nom_Boite"]
			
			# -2-  on cree l'ensemble des n° de boite:
			temptuple = self.__data.dicoNumB[self.__dicoDatas[self.__NOM_BOITE]]
			self.__dicoEnsEnd["Num_Boite"] = set(temptuple[0])

			#print self.__dicoEnsEnd["Num_Boite"]

			# comme on connait la boite on utilise la classe Boite pour creer un objet Boite qui va servir a recuperer les genes et les conditions:
			if self.__nomboite != self.__dicoDatas[self.__NOM_BOITE] : self.__boite = Boite(self.__dicoDatas[self.__NOM_BOITE],  self.__dicoDatas[self.__PROJET])

			# -3-  on cree l'ensemble des genes de la boite:
			self.__dicoEnsEnd["Genes"] = set(self.__boite.genes)

			#print self.__dicoEnsEnd["Genes"]

			# -4-  on cree l'ensemble des Wells de la boite:
			values = [v[0].code for v in self.__boite.dicoW.values() if v[1] != "NA"]
			values.sort()
			self.__dicoEnsEnd["Wells"] = set(values[:-2])

			#for w in self.__dicoEnsEnd["Wells"] : print w.code

			# -5-  on cree l'ensemble des Conditions de la boite:
			self.__dicoEnsEnd["Condition"] = set(self.__boite.conds)

			#print self.__dicoEnsEnd["Condition"]

			# -6-  on cree l'ensemble des images-paths de la boite:
			templistpaths=[]
			for i in range(1, len(self.__boite.dicolignes)):
				templistpaths.append(os.path.join(self.__dicoDatas[self.__PROJET], self.__dicoDatas[self.__NOM_BOITE], self.__boite.dicolignes[i][self.__data.COL_FILENAME]))

			self.__dicoEnsEnd["Images"]=set(templistpaths)

			#for v in self.__dicoEnsEnd["Images"] : print v
			#print "-----"

			if self.__dCode[self.__WELLS] : # si un puit et fourni on garde que l'intersection des ensembles

				templistw = self.__getWelllists(self.__dicoDatas[self.__WELLS])

				self.__dicoEnsEnd["Wells"]=set([str(self.__dicoDatas[self.__WELLS])])

				enslistimages = set(templistw[2])
				self.__dicoEnsEnd["Images"] = self.__dicoEnsEnd["Images"].intersection(enslistimages)
				#for v in self.__dicoEnsEnd["Images"] : print v
				#print "-----"

				self.__dicoEnsEnd["Genes"]=set(templistw[1])
				self.__dicoEnsEnd["Condition"]=set(templistw[0])


			if self.__dCode[self.__GENES] : 

				dicoW = self.__boite.dicoW
				gene = self.__dicoDatas[self.__GENES]
				listecles = []

				self.__dicoEnsEnd["Genes"]=set([str(self.__dicoDatas[self.__GENES])])
				
				for v in dicoW.values() :
					if v[2] == gene : listecles.append(v[0].code)

				self.__dicoEnsEnd["Wells"]=set()
				self.__dicoEnsEnd["Images"]=set()
				self.__dicoEnsEnd["Condition"]=set()

				for code in listecles :
					templistw = self.__getWelllists(code)

					self.__dicoEnsEnd["Wells"]=self.__dicoEnsEnd["Wells"].union(set([str(code)]))

					enslistimages = set(templistw[2])
					self.__dicoEnsEnd["Images"] = self.__dicoEnsEnd["Images"].union(enslistimages)

					
					self.__dicoEnsEnd["Condition"]=self.__dicoEnsEnd["Condition"].union(set(templistw[0]))

				#print self.__dicoEnsEnd["Images"]

			if self.__dCode[self.__IMAGES] : 

				dicoW = self.__boite.dicoW
				listecles = []
				for v in dicoW.values() :
					templistimg = self.__getWelllists(v[0].code)[2]
					if self.__dicoDatas[self.__IMAGES] in templistimg : listecles.append(v[0].code)

				self.__dicoEnsEnd["Wells"]=set()
				self.__dicoEnsEnd["Genes"]=set()
				self.__dicoEnsEnd["Condition"]=set()

				for code in listecles :
					templistw = self.__getWelllists(code)

					self.__dicoEnsEnd["Wells"]=self.__dicoEnsEnd["Wells"].union(set([str(code)]))

					self.__dicoEnsEnd["Genes"]=self.__dicoEnsEnd["Genes"].union(set([str(templistw[1])]))
					
					self.__dicoEnsEnd["Condition"]=self.__dicoEnsEnd["Condition"].union(set(templistw[0]))
					
				self.__dicoEnsEnd["Images"] = set([str(self.__dicoDatas[self.__IMAGES])])


		else :
			# on teste si le projet est toujours le meme :
			if self.__projet != self.__dicoDatas[self.__PROJET] : self.__data = Data(self.__dicoDatas[self.__PROJET])
			self.__dicoEnsEnd["Nom_Boite"] = set(self.__data.listB)

			# si on a seulement le projet et un gene :
			if self.__dCode[self.__GENES] : 
				gene = self.__dicoDatas[self.__GENES]
				templistboites = []
				for nomboite in self.__data.listB :
					boite = Boite(nomboite,  self.__dicoDatas[self.__PROJET])
					if gene in boite.genes : 
						templistboites.append(nomboite)
						self.__dicoEnsEnd["Condition"]=self.__dicoEnsEnd["Condition"].union(set(boite.conds))
						nb = self.__data.dicoNumB[nomboite][0]
						self.__dicoEnsEnd["Num_Boite"]=self.__dicoEnsEnd["Num_Boite"].union(set([str(nb)]))

				self.__dicoEnsEnd["Nom_Boite"] = self.__dicoEnsEnd["Nom_Boite"].intersection(set(templistboites))
				self.__dicoEnsEnd["Genes"] = set([str(gene)])
				

			
			if self.__dCode[self.__CONDS] :
				cond = self.__dicoDatas[self.__CONDS]
				templistconds = []
				for nomboite in self.__data.listB :
					boite = Boite(nomboite,  self.__dicoDatas[self.__PROJET])
					if cond in boite.conds :  
						templistconds.append(nomboite)
						self.__dicoEnsEnd["Genes"]=self.__dicoEnsEnd["Genes"].union(set(boite.genes))
						nb = self.__data.dicoNumB[nomboite][0]
						self.__dicoEnsEnd["Num_Boite"]=self.__dicoEnsEnd["Num_Boite"].union(set([str(nb)]))

				self.__dicoEnsEnd["Nom_Boite"] = self.__dicoEnsEnd["Nom_Boite"].intersection(set(templistconds))
				self.__dicoEnsEnd["Condition"] = set([str(cond)])


			for nomboite in self.__dicoEnsEnd["Nom_Boite"]:
				boite = Boite(nomboite,  self.__dicoDatas[self.__PROJET])
				templistpaths=[]
				for i in range(1, len(boite.dicolignes)):
					templistpaths.append(os.path.join(self.__dicoDatas[self.__PROJET], nomboite, boite.dicolignes[i][self.__data.COL_FILENAME]))
			self.__dicoEnsEnd["Images"]=set(templistpaths)
			
		return True

	def viewWells(self, nomboite, projet):
			# on recupere le dicowell et on classe les cles et on cree une liste des valeurs classees

		if self.__boite == None : self.__boite = Boite(nomboite,  projet)
		if nomboite != self.__dicoDatas[self.__NOM_BOITE] : self.__boite = Boite(nomboite,  projet)
			
		self.__boite = Boite(nomboite,  projet)
		dicowell = self.__boite.dicoW
		listecles = dicowell.keys()
		listecles.sort()
		listevals = []
		for cle in listecles : listevals.append("\t,\t".join([dicowell[cle][0].code, dicowell[cle][1], dicowell[cle][2]]))

		return listevals[0:-2]

	def __getWelllists(self, codewell) :
		tuplewell = self.__boite.dicoW[codewell]
		cond = [tuplewell[1]]
		gene= [tuplewell[2]]
		listimages = tuplewell[0].getImagesPaths(self.__dicoDatas[self.__PROJET], self.__dicoDatas[self.__NOM_BOITE], codewell)
		return [cond, gene, listimages]

	def __getdicoEnsEnd(self) : return self.__dicoEnsEnd
	
	dicoEnsEnd = property(__getdicoEnsEnd, doc="dictionnaire  ... =")

if __name__ == "__main__":

	c = Controleur()
	param=dict()
	param["Projet"]="/Users/lisalamasse/Desktop/Metasensors HCS/Bacillus_Ibidi_96well_angio1"
	param["Nom_Boite"] = "20130410_162617_825"
	param["Wells"]="A7"
	c.setData(param)
	c.decisionTree()
	print c.dicoEnsEnd
	#c.viewWells("20130410_162617_825", "/Users/lisalamasse/Desktop/Metasensors HCS/Bacillus_Ibidi_96well_angio1")
	

	