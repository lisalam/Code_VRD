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


class ListeNomB(swing.JFrame):

				def __init__(self, listnomb):
					swing.JFrame.__init__(self, title="Nom de boite")
					self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
					self.__listnomb = listnomb
					self.run()

				def run(self):
					self.size = (200, 400)
					self.contentPane.layout = awt.BorderLayout()
					line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)


					Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel1.setBorder(line)
					label=swing.JLabel("")
					label.setText("Liste des noms de boites")
					Panel1.add(label)
			
					Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel2.setBorder(line)
					self.__displistnomb = swing.JList(self.__listnomb)
					Panel2.add(self.__displistnomb)
					barre = swing.JScrollPane(self.__displistnomb)
					Panel2.add(barre)
			
			
					Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
					Panel3.setBorder(line)
					select = swing.JButton("Select", actionPerformed=self.__select)
					Panel3.add(select)
					close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
					Panel3.add(close)
			
					self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
					self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
					self.contentPane.add(Panel3, awt.BorderLayout.SOUTH)
			
			
			
				def __select(self, event):
					print self.__listnomb.getSelectedValues()	
	

				def __close(self, event):
					time.sleep(0.01) 
					self.dispose()


			
if __name__ == "__main__":


	listnomb=[]
	nom1 = ("20130219_120830_632")
	nom2 = ("20130219_140840_141")
	nom3 = ("20130220_104435_275")
	nom4 = ("20130227_102727_525")
	
	

	listnomb=[nom1,nom2,nom3,nom4]
	ens=set()
	listnomb=list(ens)
	
	nomb = ListeNomB(listnomb)
	nomb.show()
