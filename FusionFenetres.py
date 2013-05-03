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

				def __init__(self):
					swing.JFrame.__init__(self, title="Data")
					self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
					self.run()

				def run(self):

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

					listnumb=[]
					num1= ("1")
					num2 = ("2")
					num3 = ("3")
					num4 = ("4")
					listnumb=[num1,num2,num3,num4]

					listnomb=[]
					nom1 = ("20130219_120830_632")
					nom2 = ("20130219_140840_141")
					nom3 = ("20130220_104435_275")
					nom4 = ("20130227_102727_525")
					listnomb=[nom1,nom2,nom3,nom4]

					listcond=[]
					cond1 = ("LB")
					cond2 = ("Glucose")
					cond3 = ("Succinate")
					cond4 = ("Gluconate")
					listcond=[cond1,cond2,cond3,cond4]

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


				
					self.size = (1000, 1000)
					self.contentPane.layout = awt.BorderLayout()
					line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)
				

					Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel1.setBorder(line)
			
					Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel2.setBorder(line)
					panelistwell = ListeWellBis(listwell).getContentPane()
					Panel2.add(panelistwell)
					panelistgenes = ListeGeneBis(listgenes).getContentPane()
					Panel2.add(panelistgenes)
					panelistnumb = ListeNumBBis(listnumb).getContentPane()
					Panel2.add(panelistnumb)
					panelistnomb = ListeNomBBis(listnomb).getContentPane()
					Panel2.add(panelistnomb)
					panelistcond = ListeCondBis(listcond).getContentPane()
					Panel2.add(panelistcond)
					panelistim = ListeImageBis(listimp).getContentPane()
					Panel2.add(panelistim)
					

					
					Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel3.setBorder(line)
					

					Panel4=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel4.setBorder(line)


					
					Panel5=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
					Panel5.setBorder(line)
					select = swing.JButton("Select", actionPerformed=self.__select)
					Panel5.add(select)
					closeall = swing.JButton("Close All images", size=(100, 70), actionPerformed=self.__closeall)
					Panel5.add(closeall)
					close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
					Panel5.add(close)
					
			
					self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
					self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
					self.contentPane.add(Panel3, awt.BorderLayout.EAST)
					self.contentPane.add(Panel4, awt.BorderLayout.WEST)
					self.contentPane.add(Panel5, awt.BorderLayout.SOUTH)
					
			
			
			
				def __select(self, event):
					print self.__listcond.getSelectedValues()	
	

				def __close(self, event):
					time.sleep(0.01) 
					self.dispose()

				def __closeall(self, event):
					pass


			
if __name__ == "__main__":
	fusion=FusionFenetres()
	fusion.show()

	