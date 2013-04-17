#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
import javax.swing as swing
import java.awt as awt
from javax.swing import BorderFactory
from javax.swing.border import EtchedBorder, TitledBorder
from java.awt import Font

from java.awt import TextField, Panel, GridLayout, ComponentOrientation, Label, Checkbox, BorderLayout, Button, Color, FileDialog, Frame, Font

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

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class ListeImage(swing.JFrame):

		def __init__(self, listimp):
			swing.JFrame.__init__(self, title="Images")
			self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
			self.__listimp = listimp
			self.run()

		def run(self):
			self.size = (500, 400)
			self.contentPane.layout = awt.BorderLayout()
			line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)


			Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
			Panel1.setBorder(line)
			label=swing.JLabel("")
			label.setText("Liste des Images")
			Panel1.add(label)
			

			Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
			Panel2.setBorder(line)
			listtitles=[imp.getTitle() for imp in self.__listimp]
			self.__listimages = swing.JList(listtitles)
			barre = swing.JScrollPane(self.__listimages)
			Panel2.add(barre)
			
			Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
			Panel3.setBorder(line)
			select = swing.JButton("Show Selected", actionPerformed=self.__select)
			Panel3.add(select)
			hide = swing.JButton("Hide Selected", size=(100, 70), actionPerformed=self.__hide)
			Panel3.add(hide)
			close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
			Panel3.add(close)
			
			self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
			self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
			self.contentPane.add(Panel3, awt.BorderLayout.SOUTH)
			
		def __hide(self, event):
			titles = self.__listimages.getSelectedValues()
			for imp in self.__listimp :
				if imp.getTitle() in titles : imp.hide()
			
		def __select(self, event):
			titles = self.__listimages.getSelectedValues()
			for imp in self.__listimp :
				if imp.getTitle() in titles : imp.show()
				
	

		def __close(self, event):
			time.sleep(0.01) 
			self.dispose()


			
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

	toto = ListeImage(listimp)
	toto.show()
	
	
	for imp in listimp :
		print imp.getOriginalFileInfo().directory , imp.getOriginalFileInfo().fileName
