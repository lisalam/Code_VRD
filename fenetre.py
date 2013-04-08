#!/usr/bin/python
# -*- coding: iso-8859-15 -*-


from ij import ImageStack, ImagePlus, IJ, WindowManager
from ij.gui import Roi, NonBlockingGenericDialog
from ij.plugin.frame import RoiManager
from ij.process import ImageProcessor

from java.awt import TextField, Panel, GridLayout, ComponentOrientation, Label, Checkbox, BorderLayout, Button, Color, FileDialog, Frame, Font


import os, sys
import javax.swing as swing
import java.awt as awt
from javax.swing import BorderFactory, JFrame, JFileChooser
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
from ListeGene import ListeGene
from ListeCond import ListeCond

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class Fenetre(swing.JFrame):

		def __init__(self):
			swing.JFrame.__init__(self, title="VRD_Tools")
			self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
			self.__selImages=[]
			self.__selGenes=[]
			self.__selWells=[]
			self.__selConds=[]
			self.__selectdir = "/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools"
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
			self.__dispDossier.text = self.__selectdir
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
			Panel2.add(label)
			self.__dispNomBoite = swing.JTextField(preferredSize=(200, 30), horizontalAlignment=swing.SwingConstants.CENTER)
			self.__dispNomBoite.text = "20130227_102727_525"
			Panel2.add(self.__dispNomBoite)
			label=swing.JLabel("Numero de la boite : ", horizontalAlignment=swing.SwingConstants.RIGHT)
			Panel2.add(label)
			self.__dispNumBoite = swing.JTextField(preferredSize=(200, 30), horizontalAlignment=swing.SwingConstants.CENTER)
			self.__dispNumBoite.text = ""
			Panel2.add(self.__dispNumBoite)
			label=swing.JLabel("Images :", horizontalAlignment=swing.SwingConstants.RIGHT)
			Panel2.add(label)
			self.__dispImage = swing.JTextField(preferredSize=(200, 30), horizontalAlignment=swing.SwingConstants.CENTER)
			self.__dispImage.text = ""
			Panel2.add(self.__dispImage)
			label=swing.JLabel("Gene :", horizontalAlignment=swing.SwingConstants.RIGHT)
			Panel2.add(label)
			self.__dispGene = swing.JTextField(preferredSize=(150, 30), horizontalAlignment=swing.SwingConstants.CENTER)
			self.__dispGene.text = ""
			Panel2.add(self.__dispGene)
			label=swing.JLabel("Well :", horizontalAlignment=swing.SwingConstants.RIGHT)
			Panel2.add(label)
			self.__dispWell = swing.JTextField(preferredSize=(150, 30), horizontalAlignment=swing.SwingConstants.CENTER)
			self.__dispWell.text = ""
			Panel2.add(self.__dispWell)
			label=swing.JLabel("Condition :", horizontalAlignment=swing.SwingConstants.RIGHT)
			Panel2.add(label)
			self.__dispCond = swing.JTextField(preferredSize=(50, 30), horizontalAlignment=swing.SwingConstants.CENTER)
			self.__dispCond.text = ""
			Panel2.add(self.__dispCond)
			label=swing.JLabel("Ligne :", horizontalAlignment=swing.SwingConstants.RIGHT)
			Panel2.add(label)
			self.__dispLigne = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__choixLigne = swing.JComboBox( [" ","A", "B", "C","D","E","F","G","H"]) 
			self.contentPane.add(self.__choixLigne)
			Panel2.add(self.__choixLigne)
			label=swing.JLabel("Colonne :", horizontalAlignment=swing.SwingConstants.RIGHT)
			Panel2.add(label)
			self.__dispCol = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__choixCol = swing.JComboBox( [" ","1", "2", "3","4","5","6","7","8","9","10","11","12"]) 
			self.contentPane.add(self.__choixCol)
			Panel2.add(self.__choixCol)
			
			
			Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
			Panel3.setBorder(line)
			generate = swing.JButton("Generate", size=(100, 70), actionPerformed=self.__generate)
			Panel3.add(generate)
			close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
			Panel3.add(close)
			help = swing.JButton("Help", size=(100, 70), actionPerformed=self.__help)
			Panel3.add(help)
			

			self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
			self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
			self.contentPane.add(Panel3, awt.BorderLayout.SOUTH)

			
			
		def __browse(self, event):
				IJ.showMessage("Select project directory")
				self.__selectdir=IJ.getDirectory("image")
				
				choix = swing.JFileChooser(self.__selectdir)
				choix.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
				retour=choix.showOpenDialog(self)
				if(retour==swing.JFileChooser.APPROVE_OPTION) :
					self.__selectdir = choix.getSelectedFile().getAbsolutePath()
					self.__dispDossier.text = self.__selectdir
					

		def __generate(self, event):
			print "ok"
			print self.__choixLigne.getSelectedItem() 
			print self.__choixCol.getSelectedItem()
			
			if len(self.__selGenes) >1 :
				self.__dispGene.text = ""
				p = ListeGene(self.__selGenes)
				p.show()
			else : self.__dispGene.text = self.__selGenes[0]
			
			m = ListeCond(self.__selConds)
			m.show()
			f = ListeImage(self.__selImages)
			f.show()
			h = ListeWell(self.__selWells)
			h.show()
			
			

		def __close(self, event):
			print "ok close"
			time.sleep(0.01) 
			self.dispose()

		def __help(self, event):
			IJ.log("""
		--------------------------------------------------------------------------------------
		It is a window in which you can filter certain information to be others, 
		you can select the box number, the well, the gene and have all the information concerning
		--------------------------------------------------------------------------------------
		Dossier = Enter your file 
		--------------------------------------------------------------------------------------
		Nom de la boite = Enter your name's plate, you can't have a list of images of an entire plate
		Numero de la boite = Enter number's plate
		Images = You have a list of images 
		Ligne and Colonne = You can enter the well's code 
		Gene = Enter the code of mutants
		Condition = Enter the condition
		--------------------------------------------------------------------------------------
		
		--------------------------------------------------------------------------------------
		Generate = when you click on this button, you generate three windows with the list of images,
		of genes and conditions
		Close = Close every windows
		--------------------------------------------------------------------------------------
		
		""")


		def getDossier(self) : return self.__dispDossier.text
		def setDossier(self, nom) : self.__dispDossier.text = nom
		
		def getNomB(self) : return self.__dispNomBoite.text
		def setNomB(self, nomb) : self.__dispNomBoite.text = nomb
		
		def getNumB(self) : return self.__dispNumBoite.text
		def setNumB(self, numb) : self.__dispNumBoite.text = numb
		
		def getPuit(self) : return self.__dispWell.text
		def setPuit(self, listwell) : self.__dispWell.text = listwell
		
		def getCond(self) : return self.__dispCond.text
		def setCond(self, listcond) : self.__dispCond.text = listcond
		
		def getGene(self) : return self.__dispGene.text
		def setGene(self, listgenes) :
			self.__selGenes = listgenes
			if len(listgenes) >1 :
				self.__dispGene.text = ""
				p = ListeGene(listgenes)
				p.show()
			else : self.__dispGene.text = listgenes[0]
		
		def getLigne(self) : return self.__choixLigne.getSelectedItem() 
		def setLigne(self, ligne) : self.__choixLigne.setSelectedItem(ligne)
		
		def getCol(self) : return self.__choixCol.getSelectedItem()
		def setCol(self, col) : self.__choixCol.setSelectedItem(col)
		
		def getSelImages(self) : return self.__selImages
		def setSelImages(self, listselImages) : self.__selImages = listselImages
		

		dossier = property(getDossier, setDossier, doc="  ")
		nomb = property(getNomB, setNomB, doc="  ")
		numb = property(getNumB, setNumB, doc="  ")
		puit = property(getPuit, setPuit, doc="  ")
		cond = property(getCond, setCond, doc="  ")
		gene = property(getGene, setGene, doc="  ")
		ligne = property(getLigne, setLigne, doc="  ")
		col = property(getCol, setCol, doc="  ")
		selImages = property(getSelImages, setSelImages, doc=" return list of ImagePLus images")

			
			
if __name__ == "__main__":

	listimp=[]
	imp1 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0000.tif")
	imp2 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0001.tif")
	imp3 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0002.tif")
	imp4 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0003.tif")
	imp5 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0004.tif")
	imp6 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0005.tif")
	imp7 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0006.tif")
	imp8 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0007.tif")
	imp9 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0008.tif")
	imp10 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0009.tif")
	imp11 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0010.tif")
	imp12 = ImagePlus("/Users/lisalamasse/Dropbox/Macros_Lisa/ManipsTM/cells/cell0011.tif")
	listimp=[imp1,imp2,imp3, imp4, imp5, imp6, imp7, imp8, imp9, imp10, imp11, imp12 ]


	listcond=[]
	cond1 = ("LB")
	cond2 = ("Glucose")
	cond3 = ("Succinate")
	cond4 = ("Gluconate")
	listcond=[cond1,cond2,cond3,cond4]


	listgenes=[]
	gene1 = ("A579")
	gene2 = ("A009")
	gene3 = ("A017")
	gene4 = ("A025")
	gene5 = ("A033")
	gene6 = ("A041")
	gene7 = ("A049")
	gene8 = ("A057")
	gene9 = ("A065")
	gene10 = ("A073")
	gene11 = ("A081")
	gene12 = ("A089")
	listgenes=[gene1,gene2,gene3,gene4,gene5,gene6,gene7,gene8,gene9,gene10,gene11,gene12]
	listgenes=["A123"]


	listwell=[]
	well1 = ("A1")
	well2 = ("A2")
	well3 = ("A3")
	well4 = ("A4")
	well5 = ("A5")
	well6 = ("A6")
	well7 = ("A7")
	well8 = ("A8")
	well9 = ("A9")
	well10 = ("A10")
	well11 = ("A11")
	well12 = ("A12")
	listwell=[well1,well2,well3,well4,well5,well6,well7,well8,well9,well10,well11,well12]


	fenetre = Fenetre()
	fenetre.show()

	fenetre.numb = "25"
	fenetre.nomb = "20130219_120830_632"
	fenetre.puit = "B2"
	fenetre.cond = "LB"
	fenetre.ligne = "B"
	fenetre.col = "2"
	fenetre.selImages=listimp
	fenetre.gene=listgenes
	fenetre.puit=listwell
	fenetre.cond=listcond
	
	
	print fenetre.dossier
	print fenetre.numb
	print fenetre.nomb
	print fenetre.puit
	print fenetre.cond
	print fenetre.gene
	print fenetre.ligne
	print fenetre.col
	print fenetre.selImages
	
	
	
	

	
