#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
import javax.swing as swing
import java.awt as awt
from javax.swing import BorderFactory
from javax.swing.border import EtchedBorder, TitledBorder
from java.awt import Font
#from java.swing.colorchooser import DefaultColorSelectionModel



class Fenetre(swing.JFrame):

		def __init__(self):
			swing.JFrame.__init__(self, title="VRD_Tools")
			self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
			self.run()

		def run(self):
			self.size = (600, 250)
			self.contentPane.layout = awt.BorderLayout()
			
			
			self.__Dossier = swing.JTextField(preferredSize=(400, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__Boite = swing.JTextField(preferredSize=(400, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__Well = swing.JTextField(preferredSize=(400, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__Image = swing.JTextField(preferredSize=(400, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			
			
			
			line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)

			
			Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel1.setBorder(line)
			label=swing.JLabel("Label10")
			label.setText("Dossier")
			Panel1.add(label)
			self.__display10 = swing.JTextField(preferredSize=(300, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display10.text = ""
			Panel1.add(self.__display10)
			bouton = swing.JButton("Browse", actionPerformed=self.__bouton)
			Panel1.add(bouton)
			
			Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
			Panel2.setBorder(line)
			generate = swing.JButton("Generate", size=(100, 70), actionPerformed=self.__generate)
			Panel2.add(generate)
			close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
			Panel2.add(close)

			Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel3.setBorder(line)
		
			grid0 = awt.GridLayout()
			grid0.setRows(4)
			Panel3=swing.JPanel(grid0)
			Panel3.setBorder(line)
			label=swing.JLabel("")
			label.setText("Nom de la boite")
			Panel3.add(label)
			self.__display2 = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display2.text = ""
			Panel3.add(self.__display2)
			
			label=swing.JLabel()
			label.setText("Numero de la boite")
			Panel3.add(label)
			self.__display3 = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display3.text = ""
			Panel3.add(self.__display3)

			label=swing.JLabel()
			label.setText("Images")
			Panel3.add(label)
			self.__display4 = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display4.text = ""
			Panel3.add(self.__display4)

			Panel4=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel4.setBorder(line)
			grid1 = awt.GridLayout()
			grid1.setRows(3)
			grid1.setColumns(2)
			Panel4=swing.JPanel(grid1)
			label=swing.JLabel("")
			label.setText("Well")
			Panel4.add(label)
			self.__display2 = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display2.text = ""
			Panel4.add(self.__display2)
			label=swing.JLabel()
			label.setText("Ligne")
			Panel4.add(label)
			self.__display3 = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display3.text = ""
			Panel4.add(self.__display3)
			label=swing.JLabel()
			label.setText("Colonne")
			Panel4.add(label)
			self.__display3 = swing.JTextField(preferredSize=(100, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display3.text = ""
			Panel4.add(self.__display3)


			
# ---------TESTS----------


			#menu = swing.JScrollBar(1, 8, 10, 1, 250)
			#self.contentPane.add(menu)

			#menu = swing.JSpinner()
			#self.contentPane.add(menu)

			#menu = swing.JSplitPane()
			#self.contentPane.add(menu)

			#menu = swing.JToolBar("Image",1)
			#self.contentPane.add(menu)

			#menu = swing.JTree()
			#self.contentPane.add(menu)

			#menu = swing.RepaintManager()
			#self.contentPane.add(menu)

			#menu = swing.JPasswordField("")
			#self.contentPane.add(menu)

			#menu = swing.JTextArea("hello", 1, 8)
			#self.contentPane.add(menu)

			

#---------FIN TESTS----------

			
			self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
			self.contentPane.add(Panel2, awt.BorderLayout.SOUTH)
			self.contentPane.add(Panel3, awt.BorderLayout.WEST)
			self.contentPane.add(Panel4, awt.BorderLayout.EAST)
			
			
		def __bouton(self):
			pass	
			

		def __generate(self):
			pass

		def __close(self, event):
			self.oked = True
			time.sleep(0.01) 
			self.dispose()


			
if __name__ == "__main__":
	fenetre = Fenetre()
	fenetre.show()
