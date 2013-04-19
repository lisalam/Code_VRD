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


import string

from Data import Data

# ------------------------ Début de la classe "Well" ------------------------

class Well():
	""" Classe concernant uniquement les puits """

	def __init__(self,**param):

		self.__code = ""
		self.__LC = ""
		
		if len(param) != 1 : print "erreur"
		elif param.keys()[0] != "code" and param.keys()[0] != "lc" : 
			print param.keys()[0]
			print "erreur cles"
		elif param.keys()[0] == "code" : self.__calculerLC(param["code"])
		else : self.__calculerCode(param["lc"])

		self.__boite = ""
		self.__projet = ""
		self.__dicolignes = dict()


	def __calculerCode(self,lc) :
		l = string.uppercase[int(lc[0])-1]
		c = str(lc[1])
		code=l+c
		self.__code = code
		self.__LC = lc

	def __calculerLC(self,code) :
		l = string.uppercase.index(code[0])+1
		c = code[1:]
		lc = (str(l),c)
		self.__LC = lc
		self.__code = code

	def getImagesPaths(self, projet, nomboite, codepuit) :
		if projet != self.__projet : 
			self.__data = Data(projet)
			self.__projet = projet
		if nomboite != self.__boite : 
			self.__dicolignes = self.__data.dicolignes[nomboite]
			self.__boite = nomboite
		
		templist = []
		for v in self.__dicolignes.values() :
			if v[self.__data.COL_WELL] == codepuit :
				templist.append(os.path.join(self.__projet, self.__boite, v[self.__data.COL_FILENAME]))
		return templist
				
		
		
	

	def __getCode(self) : return self.__code
	def __getLC(self) : return self.__LC

	def setCode(self) : pass
	def setLC(self) : pass
	

	code = property(__getCode, setCode, doc="ma doc ... =")
	LC = property(__getLC, setLC, doc="ma doc ... =")


print "--- debut ---"

# ------------------------ Fin de la classe "Well" ------------------------

if __name__ == "__main__" :
	w=Well(lc=(1,12))
	print w.code
	print w.LC
	print w.getImagesPaths("/Users/lisalamasse/Desktop/Metasensors HCS/Bacillus_Ibidi_96well_angio1", "20130410_162617_825", "A7") 


#print calculerCode(lc=(2,5))
#print calculerLC(code="B8")










