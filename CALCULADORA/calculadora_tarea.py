import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "tarea_calculadora.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Calculator(QtWidgets.QMainWindow):
	def __init__(self, parent = None):
		super(Calculator, self).__init__(parent)
		uic.loadUi("tarea_calculadora.ui", self)
		
		 
		self.btn_calcular.clicked.connect(self.btn_calcular_clicked)
		self.radio_suma.clicked.connect(self.radio_suma_clicked)
		self.radio_resta.clicked.connect(self.radio_resta_clicked)
		self.radio_multiplicacion.clicked.connect(self.radio_multiplicacion_clicked)
		self.radio_division.clicked.connect(self.radio_division_clicked)
		self.text_primer_valor.setText (str(float(0)))
		self.text_segundo_valor.setText (str(float(0)))
		self.text_resultado.setText (str(float(0)))
		self.radios = ''
		self.show()

	
	def btn_calcular_clicked(self):
		
		if self.radios == self.radio_suma.text():
			self.text_resultado.setText(str(round(float(self.text_primer_valor.text()) + float(self.text_segundo_valor.text()),2)))
		elif self.radios == self.radio_resta.text():
			self.text_resultado.setText(str(round(float(self.text_segundo_valor.text()) - float(self.text_segundo_valor.text()),2)))
		elif self.radios == 'multiplicacion':
			self.text_resultado.setText(str(round(float(self.text_primer_valor.text()) * float(self.text_segundo_valor.text()),2)))
		elif self.radios == 'division':
			self.text_resultado.setText(str(round(float(self.text_segundo-valor.text()) / float(self.text_segundo_valor.text()),2)))

	
	def radio_suma_clicked(self):
		self.radios = self.radio_suma.text()

	def radio_resta_clicked(self):
		self.radios = self.radio_resta.text()

	def radio_multiplicacion_clicked(self):
		self.radios = 'multiplicacion'

	def radio_division_clicked(self):
		self.radios = 'division'	

           
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Calculator()
    app.exec()
