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

from ListeGeneBis import ListeGeneBis
from ListeWellBis import ListeWellBis
from ListeImageBis import ListeImageBis
from ListeCondBis import ListeCondBis
from ListeNomBBis import ListeNomBBis
from ListeNumBBis import ListeNumBBis

class FusionFenetres(swing.JFrame):

				def __init__(self, dicolistes):
					swing.JFrame.__init__(self, title="Data")
					self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
					self.__dicolistes = dicolistes
					self.run()

				def run(self):

					self.size = (800, 1000)
					self.contentPane.layout = awt.BorderLayout()
					line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)
				
					Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel1.setBorder(line)
			
					Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel2.setBorder(line)
					panelistwell = ListeWellBis(self.__dicolistes["Wells"]).getContentPane()
					Panel2.add(panelistwell)
					panelistgenes = ListeGeneBis(self.__dicolistes["Genes"]).getContentPane()
					Panel2.add(panelistgenes)
					panelistnumb = ListeNumBBis(self.__dicolistes["Num_Boite"]).getContentPane()
					Panel2.add(panelistnumb)
					panelistnomb = ListeNomBBis(self.__dicolistes["Nom_Boite"]).getContentPane()
					Panel2.add(panelistnomb)
					panelistcond = ListeCondBis(self.__dicolistes["Condition"]).getContentPane()
					Panel2.add(panelistcond)
					panelistim = ListeImageBis(self.__dicolistes["Images"]).getContentPane()
					Panel2.add(panelistim)
					
					Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel3.setBorder(line)
					

					Panel4=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel4.setBorder(line)


					
					Panel5=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
					Panel5.setBorder(line)
					
					
					close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
					Panel5.add(close)
					
			
					self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
					self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
					self.contentPane.add(Panel3, awt.BorderLayout.EAST)
					self.contentPane.add(Panel4, awt.BorderLayout.WEST)
					self.contentPane.add(Panel5, awt.BorderLayout.SOUTH)
					
	

				def __close(self, event):
					time.sleep(0.01) 
					self.dispose()

				def __closeall(self, event):
					pass


			
if __name__ == "__main__":
	fusion=FusionFenetres()
	fusion.show()

	