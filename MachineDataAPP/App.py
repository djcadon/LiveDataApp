#Standard Libraries
import json
import sys
import os
#External Libraries
from PyQt6 import uic
from PyQt6.QtCore import QObject, QUrl
from PyQt6.QtWidgets import QDialog, QLabel, QMainWindow, QApplication, QProgressBar, QWidget, QPushButton
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
        self.websocket.disconnected.connect(self.on_disconnected)
        self.websocket.textMessageReceived.connect(self.on_message)
        self.websocket.errorOccurred.connect(self.on_error)

    def connect(self, url):
        print(f"Connecting to {url}...")
        self.websocket.open(QUrl(url))

    def on_connected(self):
        print("Connected to WebSocket server")
        self.websocket.sendTextMessage("Hello from PyQt!")

    def on_disconnected(self):
        print("Disconnected from WebSocket server")

    def on_message(self, message):
        print(f"Message received: {message}")

    def on_error(self, error):
        print(f"WebSocket error: {error}")
class NetworkManager(QObject):
    def __init__(self):
        super().__init__()
        self.network_manager = QNetworkAccessManager(self)
    #GET REQUEST
    def get(self, url: str, callback=None):
        request = QNetworkRequest(QUrl(url))
        reply = self.network_manager.get(request)
        reply.finished.connect(lambda: self.handle_response(reply, callback))
    #POST REQUEST
    def post(self, url: str, data: str, callback=None):
        request = QNetworkRequest(QUrl(url))
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, data.encode())
        reply.finished.connect(lambda: self.handle_response(reply, callback))
    #HANDLE REPLY
    def handle_response(self, reply: QNetworkReply, callback):
        if reply.error() == QNetworkReply.NetworkError.NoError:
            data = reply.readAll().data().decode()
            print(data)
            if callback:
                callback(data)
        else:
            print("Error:", reply.errorString())
            if callback:
                callback(None)
#MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        #UI INITIALIZATION
        super().__init__()
        self.data_points = {
            'TimeStamp':'time_stamp',
            'Mold':'mold',
            'ShotCount':'shot_count',
            'CycleTime':'cycle_time',
            'FillingPeak':'filling_peak',
            'PlastTime':'plast_time',
            'VPSwitchPos':'vp_switch_pos',
            'MinCushPos':'min_cush_pos',
            'HrLeft':'hr_left',
            'MinLeft':'min_left',
            'PercentLeft':'percentage_left',
            'ShotLeft':'shot_left'}
        uic.loadUi(os.path.join(DIRECTORY,"MainWindow.ui"), self)
        self.network_manager = NetworkManager()
        self.setup_windows()
        self.setup_buttons()
        #REQUESTS AND REAL TIME UPDATE SETUP
        #self.websocket = WebSocketClient()
        #self.websocket.connect("ws://192.168.1.153:5000")
    #INITIALIZING WINDOWS
    def setup_windows(self):
        self.machine_views = {}
        for machine in MACHINES:
            dialog = SingularMachineView()
            dialog.setObjectName(machine['DIALOG'])
            dialog.MachineID.setText(machine['NAME'])
            self.stackedWidget.addWidget(dialog)
            self.machine_views[machine['ID']] = dialog
            update_button = dialog.findChild(QPushButton, 'ButtonUpdate')
            update_button.clicked.connect(lambda _, d=dialog: self.fetch_latest_data(d))
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
    #FETCHING LATEST DATA 
    def fetch_latest_data(self, dialog):
        machine_ID = dialog.MachineID.text().replace("-", "")
        url = f"{SOCKETIO}/data/{machine_ID}/latest"
        self.network_manager.get(url, lambda data: self.update_labels(dialog, data))
    #UPDATE THE LABELS FROM CALLBACK
    def update_labels(self, dialog, data):
        if data:
            # Assuming JSON response
            response = json.loads(data)
            for label in dialog.findChildren(QLabel):
                label_name = label.objectName()
                key = self.data_points.get(label_name)
                if key:
                    label.setText(f"{label.text().split(':')[0]}:{response.get(key, 'N/A')}")
                else:
                    print(f"No matching key for label: {label_name}")
            percent_left = dialog.findChildren(QProgressBar)
            if percent_left:
                print(response.get("PercentLeft",""))
                #percent_left.setValue(response.get("PercentLeft",""))
        else:
            print("Failed to fetch data or no data received")
#SINGLE MACHINE VIEW
class SingularMachineView(QDialog):
    def __init__(self):    
        super().__init__()
        uic.loadUi(os.path.join(DIRECTORY,"SingularMachine.ui"), self)
        self.ButtonExit.clicked.connect(lambda: main_window.stackedWidget.setCurrentWidget(main_window.FloorView))
#Run the app
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.setCentralWidget(main_window.stackedWidget)
main_window.showMaximized()
sys.exit(app.exec())