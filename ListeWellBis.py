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


class ListeWellBis(swing.JFrame):

				def __init__(self, listwell):
					swing.JFrame.__init__(self, title="Well")
					self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
					self.__listwell = listwell
					self.run()

				def run(self):
					self.size = (200, 300)
					self.contentPane.layout = awt.BorderLayout()
					line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)

					Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel1.setBorder(line)
					label=swing.JLabel("")
					label.setText("Liste des Puits")
					Panel1.add(label)
					menu = swing.JMenuBar()
					Panel1.add(menu)
					
					Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel2.setBorder(line)
					self.__displistwell = swing.JList(self.__listwell)
					self.__displistwell.setVisibleRowCount(14)
					self.__displistwell.setFixedCellWidth(75) 
					Panel2.add(self.__displistwell)
					barre = swing.JScrollPane(self.__displistwell)
					Panel2.add(barre)
					
					
					Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
					Panel3.setBorder(line)


					self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
					self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
					self.contentPane.add(Panel3, awt.BorderLayout.SOUTH)



if __name__ == "__main__":

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
	
	well = ListeWellBis(listwell)
	well.show()


						