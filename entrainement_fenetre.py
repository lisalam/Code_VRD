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
			line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)

			
			
			Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel1.setBorder(line)
			Panel1.add(self.__Dossier)
			
			
			Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel2.setBorder(line)
			Panel2.add(self.__Boite)
			
			Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel3.setBorder(line)
			Panel3.add(self.__Dossier)
			bouton = swing.JButton("Select", actionPerformed=self.__bouton)
			self.contentPane.add(Panel1)
			Panel3.add(bouton)
			
			Panel4=swing.JPanel(awt.FlowLayout(awt.FlowLayout.LEFT))
			Panel4.setBorder(line)
			Panel4.add(self.__Boite)
			bouton = swing.JButton("Select", actionPerformed=self.__bouton)
			self.contentPane.add(Panel1)
			Panel4.add(bouton)
			
			self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
			self.contentPane.add(Panel2, awt.BorderLayout.SOUTH)
			self.contentPane.add(Panel3, awt.BorderLayout.WEST)
			self.contentPane.add(Panel4, awt.BorderLayout.EAST)
			
			
		def __bouton(self):
			pass	
			
		def __bouton1(self):
			pass	


if __name__ == "__main__":
	test = Test()
	test.show()