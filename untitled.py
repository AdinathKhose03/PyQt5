from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

app = QApplication([])

# Set the application style to 'fusion'
app.setStyle('fusion')

# Create QWidget instance
window = QWidget()

# Create QVBoxLayout instance
layout = QVBoxLayout()

# Create QLabel instances
label1 = QLabel("Hello Qt")
label2 = QLabel("Girte hai shahsavar maidane jang mai vo tifl kya girenge jo ghutno ke bal chale the")

# Create QPushButton instances
button_like = QPushButton("Like")
button_comment = QPushButton("Comment")

# Add widgets to the inner layout
inner_layout = QVBoxLayout()
inner_layout.addWidget(label2)

# Add widgets to the main layout
layout.addWidget(inner_layout)
layout.addWidget(button_like)
layout.addWidget(button_comment)
layout.addWidget(label1)

# Set the layout for the window
window.setLayout(layout)

# Show the window
window.show()

# Start the application's event loop
app.exec()
