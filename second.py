# window = QWidget cha instance
# layout = QVBoxLayout cha instance
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout, QPushButton, QLabel
app = QApplication([])
window = QWidget()

label2 = QLabel("Girte hai shahsavar maidane jang mai vo tifl kya girenge jo ghutno ke bal chale the")
inner_layout = QHBoxLayout()
inner_layout.addWidget(label2)

layout = QVBoxLayout()
layout.addWidget(QPushButton("Like"))
layout.addWidget(QPushButton("Comment"))

inner_layout.addLayout(layout)

label = QLabel("Hello Qt")
inner_layout.addWidget(label)

window.setLayout(inner_layout)
window.show()
#app.setStyle('Fusion')
app.exec()