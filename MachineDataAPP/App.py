#Standard Libraries
import json
import os
#External Libraries
from PyQt6 import uic
from PyQt6.QtCore import QObject, QUrl
from PyQt6.QtWidgets import QDialog, QLabel, QMainWindow, QApplication, QWidget, QPushButton
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt6.QtWebSockets import QWebSocket

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
#Config file
with open(os.path.join(DIRECTORY,'config.json')) as config_file:
    config = json.load(config_file)
SOCKETIO = config['SOCKETIO']
MACHINES = config['MACHINES']
#WEBSOCKET
class WebSocketClient(QObject):
    def __init__(self):
        super().__init__()
        self.websocket = QWebSocket()
        self.websocket.connected.connect(self.on_connected)
        self.websocket.textMessageReceived.connect(self.on_message)
    #CONNECT FUNCTION
    def connect(self, url):
        self.websocket.open(QUrl(url))
    #CONNECT EVENT
    def on_connected(self):
        print("Connected to WebSocket server")
    #RECEIVED A JSON MESSAGE FROM SOCKET
    def on_message(self, message):
        print("Message received:", message)
        # Handle the real-time message here, update the UI if needed
    #SEND A JSON MESSAGE TO API
    def send_message(self, message):
        self.websocket.sendTextMessage(message)
#MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        #UI INITIALIZATION
        super().__init__()
        uic.loadUi(os.path.join(DIRECTORY,"MainWindow.ui"), self)
        self.setup_windows()
        self.setup_buttons()
        #REQUESTS AND REAL TIME UPDATE SETUP
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.on_finished)
        self.websocket = WebSocketClient()
        self.websocket.connect("ws://192.168.1.153:5000")
        self.data_points = {
            'time_stamp': "Time Stamp: N/A",
            'mold': "Mold: N/A",
            'shot_count': "Shot Count: N/A",
            'cycle_time': "Cycle Time: N/A",
            'filling_peak': "Filling Peak: N/A",
            'plast_time': "Plast Time: N/A",
            'vp_switch_pos': "VP Switch Pos: N/A",
            'min_cush_pos': "Min Cush Pos: N/A",
            'hr_left': "Hours Left: N/A",
            'min_left': "Minutes Left: N/A",
            'percentage_left': "Percentage Left: N/A",
            'shot_left': "Shots Left: N/A"}
    #INITIALIZING WINDOWS
    def setup_windows(self):
        self.machine_views = {}
        for machine in MACHINES:
            dialog = SingularMachineView()
            dialog.setObjectName(machine['DIALOG'])
            dialog.MachineID.setText(machine['NAME'])
            self.stackedWidget.addWidget(dialog)
            self.machine_views[machine['ID']] = dialog
    #BUTTON LINKING
    def setup_buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.FloorView))
        self.exit_button = self.findChild(QPushButton, "ButtonMainMenu")
        self.exit_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainMenu))
        for machine in MACHINES:
            button = self.findChild(QPushButton, machine['BUTTON'])
            if button:
                dialog = self.machine_views.get(machine['ID'])
                if dialog:
                    button.clicked.connect(lambda _, d=dialog: self.stackedWidget.setCurrentWidget(d))
    #GET REQUEST RESPONSE HANDLER
    def on_finished(self, reply:QNetworkReply):
        if reply.error() == QNetworkReply.NetworkError.NoError:
            data = reply.readAll().data().decode()
            print("Data received:", data)
        else:
            print("Error:", reply.errorString())
#SINGLE MACHINE VIEW
class SingularMachineView(QDialog):
    def __init__(self):    
        super().__init__()
        uic.loadUi(os.path.join(DIRECTORY,"SingularMachine.ui"), self)
        self.ButtonExit.clicked.connect(lambda: main_window.stackedWidget.setCurrentWidget(main_window.FloorView))
#Run the app
app = QApplication([])
main_window = MainWindow()
main_window.setCentralWidget(main_window.stackedWidget)
main_window.showMaximized()
app.exec()