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
from Well import Well


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
		temp = self.__data.dicoG
		return temp[self.__nomboite]
	
	def __getlistCond(self):
		temp = self.__data.dicoC
		return temp[self.__nomboite]
		
			
	def __getdicoWell(self):
		tempdict = dict()
		dicolignes = self.__data.dicolignes[self.__nomboite] # recuperation du fichier texte labels sous forme de dictionnaire pour la boite en cours
		ensTotal = set()
		ensLignes = set()
		for val in self.PUITS_96() : ensTotal.add(val.code) #ensemble des codes = ensemble de strings
		for val in dicolignes.values() :
			if val != "Well" :
				tempcode = val[self.__data.COL_WELL]
				w = Well(code=tempcode)				#objet classe Well
				cond = val[self.__data.COL_COND]
				gene = val[self.__data.COL_GENES]
			
				ensLignes.add(w.code)				# ensemble des codes = strings
				tempdict[w.code]=(w, cond, gene)

		ensInter =ensTotal.difference(ensLignes)

		for w in ensInter : tempdict[w]=(Well(code=w), "NA", "NA")

		return tempdict
		
			
		#print dicolignes.keys()
		#print dicolignes[0], dicolignes[1]
		
		
		

	def __getNom(self) : return self.__nomboite

	def __getProjet(self) : return self.__projet

	def __setProjet(self, projet) : self.__projet = projet

	@staticmethod
	def PUITS_96() :
		templist = list()
		for i in range(1,9) :
			for j in range(1,13) :
				p = Well(lc=(i,j))
				templist.append(p)

		#templist = [Well(i,j) for i in range(1,9) for j in range(1,13)] # 2 boucles imbriquées l'une avec l'autre et un "append", alors on peut faire une liste en intension et c'est le cas sur cette ligne


		templist.sort()

		return templist
		


# ------------------------------ Propriétés de la classe "Boite" ------------------------------

	genes=property(__getlistGene, doc = "Liste des gènes ...=")
	conds=property(__getlistCond, doc = "Liste des conditions ...=")
	dicoW=property(__getdicoWell, doc = "dictionnaire ...=")
	nom =property(__getNom, doc = " ...=")
	projet=property(__getProjet, __setProjet , doc = " ...=")
	

# ****************************** Fin de la classe "Boite" ******************************		

# TEST DE LA CLASSE

if __name__ == "__main__" :
	boite=Boite("20130410_162617_825", "/Users/lisalamasse/Desktop/Metasensors HCS/Bacillus_Ibidi_96well_angio1")
	#boite=Boite("20130410_183703_374", "/Users/lisalamasse/Desktop/Metasensors HCS/Bacillus_Ibidi_96well_angio1")
	print boite.genes[0:3]
	print boite.conds[0:3]
	print boite.dicoW.items()[0]
	#print boite.nom
	#print boite.projet
	#print Boite.PUITS_96()


	#print boite.dicoW["B12"][0].code , boite.dicoW["B12"][0].LC, boite.dicoW["B12"][1], boite.dicoW["B12"][2]


