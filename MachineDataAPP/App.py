#Standard Libraries
import json
import sys
import os
#External Libraries
from PyQt6 import uic
from PyQt6.QtCore import QObject, QUrl
from PyQt6.QtWidgets import QDialog, QLabel, QMainWindow, QApplication, QProgressBar, QPushButton
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest

#CONFIGURATION VARIABLES
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(DIRECTORY,'config.json')) as config_file:
    config = json.load(config_file)
SOCKETIO = config['SOCKETIO']
MACHINES = config['MACHINES']
#NETWORK REQUESTS MANAGER
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
    #HANDLING THE REQUESTS
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
#MainMenu
class MainWindow(QMainWindow):
    def __init__(self):
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
        self.dialogs = {}
        uic.loadUi(os.path.join(DIRECTORY, "MainWindow.ui"), self)
        self.network_manager = NetworkManager()
        self.setup_windows()
        self.setup_buttons()
    #SETTING UP WINDOWS
    def setup_windows(self):
        for machine in MACHINES:
            dialog = SingularMachineView()
            dialog.setObjectName(machine['DIALOG'])
            dialog.MachineID.setText(machine['NAME'])
            self.stackedWidget.addWidget(dialog)
            #STORING MACHINE DIALOGS AND WIDGETS IN DICT
            #ACCESS dialog THROUGH self.dialogs[MACHINES['ID']]['dialog']
            #ACCESS widgets THROUGH self.dialogs[MACHINES['ID']]['widgets'][widgettype] .get('name') or .items()
            self.dialogs[machine['ID']] = {
                'dialog': dialog,
                'widgets': {
                    'labels': {label.objectName(): label for label in dialog.findChildren(QLabel)},
                    'progress_bars': {progress_bar.objectName(): progress_bar for progress_bar in dialog.findChildren(QProgressBar)},
                    'buttons': {button.objectName(): button for button in dialog.findChildren(QPushButton)}
                }
            }
    #SETUP BUTTONS FOR STACKED WIDGET
    def setup_buttons(self):
        #CONNECT MAINMENU BUTTONS
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.FloorView))
        self.ButtonMainMenu.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainMenu))
        #CONNECT MACHINE DIALOG BUTTONS
        for machine in MACHINES:
            button = self.findChild(QPushButton, machine['BUTTON'])
            if button:
                dialog = self.dialogs[machine['ID']]['dialog']
                button.clicked.connect(lambda _, d=dialog: self.stackedWidget.setCurrentWidget(d))
            #CONNECT UPDATE BUTTONS
            update_button = self.dialogs[machine['ID']]['widgets']['buttons'].get('ButtonUpdate')
            update_button.clicked.connect(lambda _, d=machine['ID']: self.fetch_latest_data(d))
    #FETCHES LATEST DATA AND SETS CALLBACK
    def fetch_latest_data(self, machine_id):
        machine_ID = self.dialogs[machine_id]['dialog'].MachineID.text().replace("-", "")
        url = f"{SOCKETIO}/data/{machine_ID}/latest"
        self.network_manager.get(url, lambda data: self.update_labels(machine_id, data))
    #UPDATES LABELS OF MACHINE WHEN GET REQUEST IS PROCESSED
    def update_labels(self, machine_id, data):
        if data:
            response = json.loads(data)
            labels = self.dialogs[machine_id]['widgets']['labels']
            for label_name, label in labels.items():
                key = self.data_points.get(label_name)
                if key:
                    label.setText(f"{label.text().split(':')[0]}:{response.get(key, 'N/A')}")
            progress_bars = self.dialogs[machine_id]['widgets']['progress_bars']
            if 'PercentLeft' in progress_bars:
                progress_bars['PercentLeft'].setValue(response.get('percentage_left', 100))
        else:
            print("Failed to fetch data or no data received")
#SINGULAR MACHINE DIALOG
class SingularMachineView(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(DIRECTORY, "SingularMachine.ui"), self)
        self.ButtonExit.clicked.connect(lambda: main_window.stackedWidget.setCurrentWidget(main_window.FloorView))

#MAIN
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.setCentralWidget(main_window.stackedWidget)
main_window.showMaximized()
sys.exit(app.exec())
