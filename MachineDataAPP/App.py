import json
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication, QPushButton
#Config file
with open('config.json') as config_file:
    config = json.load(config_file)
SOCKETIO = config['SOCKETIO']
MACHINES = config['MACHINES']
#SOCKETIO
class SocketIO():
    def __init__(self):
        pass
#MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainWindow.ui", self)
        self.setup_windows()
        #CONNNECT BUTTONS
        self.MachineViewButton.clicked.connect(self.machine_view.show())
    #INITIALIZING WINDOWS
    def setup_windows(self):
        self.machine_view = MachineView()
        for machine in MACHINES:
            window = self.find(QDialog, machine['BUTTON'])
            if not window:
                machine['NAME'] = SingularMachineView()
    #BRINGS WINDOW TO FRONT
    def show_window(self, window):
        window.show()
#MACHINE VIEW WINDOW
class MachineView(QDialog):
    def __init__(self):    
        super().__init__()
        uic.loadUi("MachineView.ui", self)
        self.setup_windows()
        self.setup_buttons()
    def setup_buttons(self):
        for machine in MACHINES:
            button = self.findChild(QPushButton, machine['BUTTON'])
            if button:
                button.clicked.connect(lambda _, name=machine['NAME']: self.show_window(name))
    def show_window(self, name):
        name.show()
#FLOOR VIEW WINDOW
class FloorView(QDialog):
    def __init__(self):    
        super().__init__()
        uic.loadUi("FloorView.ui", self)
#SINGLE MACHINE VIEW
class SingularMachineView(QDialog):
    def __init__(self):    
        super().__init__()
        uic.loadUi("SingularMachine.ui", self)
#Run the app
app = QApplication([])
window = MainWindow()
window.show()
app.exec()