import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle("Adinath Khose")

        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Hello")
        self.layout().addWidget(my_label)
        



app = qtw.QApplication([])
mw=MainWindow()

app.exec()