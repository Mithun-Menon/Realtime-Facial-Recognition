import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

# Create the application object
app = QApplication(sys.argv)

# Create a widget for the main window
window = QWidget()
window.setStyleSheet("background-color: #b48b8b;")

window.setWindowTitle('Realtime Video Aided Facial Recognition System')

# Create a label for the video feed
video_label = QLabel(parent=window)
video_label.setStyleSheet("background-color: #0;")

video_label.setGeometry(10, 10, 640, 480)

# Create a table for the attendance data
table = QTableWidget(parent=window)
table.setStyleSheet("background-color: #0;")

table.setGeometry(660, 10, 300, 460)
table.setColumnCount(3)
table.setHorizontalHeaderLabels(['Name', 'Time', 'Status'])

# Create a button to start and stop the recognition process
button = QPushButton('Start', parent=window)
button.setGeometry(10, 500, 640, 30)

# Define a function to be called when the button is clicked
def on_button_clicked():
    if button.text() == 'Start':
        button.setText('Stop')
        # Start the recognition process
    else:
        button.setText('Start')
        # Stop the recognition process

# Connect the button to the function
button.clicked.connect(on_button_clicked)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())

