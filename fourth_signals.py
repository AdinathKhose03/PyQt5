from PyQt5.QtWidgets import *
app = QApplication([])
app.setStyle('Fusion')

window = QWidget()


button1 = QPushButton("click to show message 1")
button2 = QPushButton("click to show message 2")
button3 = QPushButton("click to show message 3")
button4 = QPushButton("click to show message 4")


def on_clicked_btn1():
    alert=QMessageBox()
    alert.setText("Jai Hind")
    alert.exec()

def on_clicked_btn2():
    alert=QMessageBox()
    alert.setText("Jai Bajrang Bali")
    alert.exec()

def on_clicked_btn3():
    alert = QMessageBox()
    alert.setText("Jai Shree Ram")
    alert.exec()

def on_clicked_btn4():
    alert = QMessageBox()
    alert.setText("Adinath Khose Zinda Bad")
    alert.exec()


button1.clicked.connect(on_clicked_btn1)
button2.clicked.connect(on_clicked_btn2)
button3.clicked.connect(on_clicked_btn3)
button4.clicked.connect(on_clicked_btn4)

layout = QVBoxLayout()
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)

window.setLayout(layout)
window.show()
app.exec()