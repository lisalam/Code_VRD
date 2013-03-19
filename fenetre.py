import javax.swing as swing
import java.awt as awt
from javax.swing import BorderFactory
from javax.swing.border import EtchedBorder, TitledBorder
from java.awt import Font


class Test(swing.JFrame):

		def __init__(self):
			swing.JFrame.__init__(self, title="VRD_Tools")
			self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
			self.run()

		def run(self):
			self.size = (1000, 400)
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
			#Panel1.add(self.__Dossier)
			#self.contentPane.add(Panel1)
			bouton = swing.JButton("Browse", actionPerformed=self.__bouton)
			#self.contentPane.add(Panel1)
			Panel1.add(bouton)
			#label=swing.JLabel("Label2")
			#label.setText("Dossier")
			#Panel1.add(label)


			Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel2.setBorder(line)
			label=swing.JLabel("Label10")
			label.setText("Image")
			Panel2.add(label)
			self.__display10 = swing.JTextField(preferredSize=(70, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display10.text = ""
			Panel2.add(self.__display10)

			
			#Panel2.add(self.__Boite)
			#self.contentPane.add(Panel2)
			#bouton = swing.JButton("Select", actionPerformed=self.__bouton)
			#self.contentPane.add(Panel2)
			#Panel2.add(bouton)

			#self.__label=swing.JLabel("Images")
			#Panel2.add(self.__label)

			Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel3.setBorder(line)
			label=swing.JLabel("Label10")
			label.setText("Numero de Boite")
			Panel3.add(label)
			self.__display10 = swing.JTextField(preferredSize=(50, 30), horizontalAlignment=swing.SwingConstants.LEFT)
			self.__display10.text = ""
			Panel3.add(self.__display10)
			

			
			#Panel3.add(self.__Well)
			#self.contentPane.add(Panel3)
			#bouton = swing.JButton("Select", actionPerformed=self.__bouton)
			#self.contentPane.add(Panel3)
			#Panel3.add(bouton)

			Panel4=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel4.setBorder(line)
			Panel4.add(self.__Image)
			self.contentPane.add(Panel4)
			bouton = swing.JButton("Select", actionPerformed=self.__bouton)
			self.contentPane.add(Panel4)
			Panel4.add(bouton)
			
			generate = swing.JButton("Generate", size=(100, 70), actionPerformed=self.__generate)
			Panel2.add(generate)

			close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
			Panel2.add(close)

			
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
	test = Test()
	test.show()