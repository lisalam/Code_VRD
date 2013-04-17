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


class ListeCond(swing.JFrame):

				def __init__(self, listcond):
					swing.JFrame.__init__(self, title="Conditions")
					self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
					self.__listcond = listcond
					self.run()

				def run(self):
					self.size = (200, 400)
					self.contentPane.layout = awt.BorderLayout()
					line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)


					Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel1.setBorder(line)
					label=swing.JLabel("")
					label.setText("Liste des Conditions")
					Panel1.add(label)
			
					Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel2.setBorder(line)
					self.__displistcond = swing.JList(self.__listcond)
					Panel2.add(self.__displistcond)
					barre = swing.JScrollPane(self.__displistcond)
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
					print self.__listcond.getSelectedValues()	
	

				def __close(self, event):
					time.sleep(0.01) 
					self.dispose()


			
if __name__ == "__main__":


	listcond=[]
	cond1 = ("LB")
	cond2 = ("Glucose")
	cond3 = ("Succinate")
	cond4 = ("Gluconate")
	
	

	listcond=[cond1,cond2,cond3,cond4]
	
	cond = ListeCond(listcond)
	cond.show()
