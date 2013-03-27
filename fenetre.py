#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
import javax.swing as swing
import java.awt as awt
from javax.swing import BorderFactory
from javax.swing.border import EtchedBorder, TitledBorder
from java.awt import Font



import sys
import os
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

from ListeImage import ListeImage

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class Fenetre_modif(swing.JFrame):

		def __init__(self):
			swing.JFrame.__init__(self, title="VRD_Tools")
			self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
			self.run()

		def run(self):
			self.size = (1000, 400)
			self.contentPane.layout = awt.BorderLayout()
			line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)

			Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel1.setBorder(line)
			label=swing.JLabel("")
			label.setText("Dossier")
			Panel1.add(label)
			self.__dispDossier = swing.JTextField(preferredSize=(400, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__dispDossier.text = "/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools"
			Panel1.add(self.__dispDossier)
			browse = swing.JButton("Browse", actionPerformed=self.__browse)
			Panel1.add(browse)

			grid = awt.GridLayout()
			grid.setRows(4)
			grid.setHgap(1)
			grid.setVgap(1)
			Panel2=swing.JPanel(grid)
			Panel2.setBorder(line)
			
			
			label=swing.JLabel("Nom de la boite : ", horizontalAlignment=swing.SwingConstants.RIGHT)
			#label.setText("Nom de la boite : ")
			Panel2.add(label)
			self.__dispNomBoite = swing.JTextField(preferredSize=(200, 30), horizontalAlignment=swing.SwingConstants.CENTER)
			self.__dispNomBoite.text = "20130227_102727_525"
			Panel2.add(self.__dispNomBoite)
			label=swing.JLabel()
			label.setText("Numero de la boite")
			Panel2.add(label)
			self.__dispNumBoite = swing.JTextField(preferredSize=(200, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__dispNumBoite.text = ""
			Panel2.add(self.__dispNumBoite)
			label=swing.JLabel()
			label.setText("Images")
			Panel2.add(label)
			self.__dispImage = swing.JTextField(preferredSize=(200, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__dispImage.text = ""
			Panel2.add(self.__dispImage)
			label=swing.JLabel()
			label.setText("Gene")
			Panel2.add(label)
			self.__dispGene = swing.JTextField(preferredSize=(150, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__dispGene.text = ""
			Panel2.add(self.__dispGene)
			label=swing.JLabel()
			label.setText("Well")
			Panel2.add(label)
			self.__dispWell = swing.JTextField(preferredSize=(150, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__dispWell.text = ""
			Panel2.add(self.__dispWell)
			label=swing.JLabel()
			label.setText("Condition")
			Panel2.add(label)
			self.__dispCond = swing.JTextField(preferredSize=(50, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__dispCond.text = ""
			Panel2.add(self.__dispCond)
			label=swing.JLabel()
			label.setText("Ligne")
			Panel2.add(label)
			self.__dispLigne = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__choixLigne = swing.JComboBox( ["A", "B", "C","D","E","F","G","H"]) 
			self.contentPane.add(self.__choixLigne)
			Panel2.add(self.__choixLigne)
			label=swing.JLabel()
			label.setText("Colonne")
			Panel2.add(label)
			self.__dispCol = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__choixCol = swing.JComboBox( ["1", "2", "3","4","5","6","7","8","9","10","11","12"]) 
			self.contentPane.add(self.__choixCol)
			Panel2.add(self.__choixCol)
			
			
			Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
			Panel3.setBorder(line)
			generate = swing.JButton("Generate", size=(100, 70), actionPerformed=self.__generate)
			Panel3.add(generate)
			close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
			Panel3.add(close)
			

			self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
			self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
			self.contentPane.add(Panel3, awt.BorderLayout.SOUTH)

			
			
		def __browse(self, event):
			print "ok browse"


		def __generate(self, event):
			print "ok"
			print self.__choixLigne.getSelectedItem() 
			print self.__choixCol.getSelectedItem()
			f = ListeImage()
			f.show()
			

		def __close(self, event):
			print "ok close"
			time.sleep(0.01) 
			self.dispose()

		def getDossier(self) : return self.__dispDossier.text
		def setDossier(self, nom) : self.__dispDossier.text = nom
		def getNomB(self) : return self.__dispNomBoite.text
		def setNomB(self, nomb) : self.__dispNomBoite.text = nomb
		def getNumB(self) : return self.__dispNumBoite.text
		def setNumB(self, numb) : self.__dispNumBoite.text = numb
		def getPuit(self) : return self.__dispWell.text
		def setPuit(self, puit) : self.__dispWell.text = puit
		def getCond(self) : return self.__dispCond.text
		def setCond(self, cond) : self.__dispCond.text = cond
		def getGene(self) : return self.__dispGene.text
		def setGene(self, gene) : self.__dispGene.text = gene
		def getLigne(self) : return self.__choixLigne.getSelectedItem() 
		def setLigne(self, ligne) : self.__choixLigne.setSelectedItem(ligne)
		def getCol(self) : return self.__choixCol.getSelectedItem()
		def setCol(self, col) : self.__choixCol.setSelectedItem(col)


		dossier = property(getDossier, setDossier, doc="  ")
		nomb = property(getNomB, setNomB, doc="  ")
		numb = property(getNumB, setNumB, doc="  ")
		puit = property(getPuit, setPuit, doc="  ")
		cond = property(getCond, setCond, doc="  ")
		gene = property(getGene, setGene, doc="  ")
		ligne = property(getLigne, setLigne, doc="  ")
		col = property(getCol, setCol, doc="  ")

			
			
if __name__ == "__main__":
	fenetre = Fenetre_modif()
	fenetre.show()

	fenetre.numb = "25"
	fenetre.nomb = "nomb"
	fenetre.puit = "puit"
	fenetre.cond = "cond"
	fenetre.ligne = "B"
	fenetre.col = "2"
	
	print fenetre.dossier
	print fenetre.numb
	print fenetre.nomb
	print fenetre.puit
	print fenetre.cond
	print fenetre.gene
	print fenetre.ligne
	print fenetre.col
	
	
	
	

	
