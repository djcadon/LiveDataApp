# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MachineView.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 1000)
        Dialog.setMaximumSize(QSize(1920, 1080))
        Dialog.setMouseTracking(False)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 791, 551))
        self.MachineLayout = QGridLayout(self.gridLayoutWidget)
        self.MachineLayout.setSpacing(20)
        self.MachineLayout.setObjectName(u"MachineLayout")
        self.MachineLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.MachineLayout.addItem(self.horizontalSpacer, 0, 1, 1, 5)

        self.Button752 = QPushButton(self.gridLayoutWidget)
        self.Button752.setObjectName(u"Button752")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button752.sizePolicy().hasHeightForWidth())
        self.Button752.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.Button752.setFont(font)

        self.MachineLayout.addWidget(self.Button752, 1, 2, 1, 1)

        self.Button1001 = QPushButton(self.gridLayoutWidget)
        self.Button1001.setObjectName(u"Button1001")
        sizePolicy.setHeightForWidth(self.Button1001.sizePolicy().hasHeightForWidth())
        self.Button1001.setSizePolicy(sizePolicy)
        self.Button1001.setFont(font)

        self.MachineLayout.addWidget(self.Button1001, 1, 4, 1, 1)

        self.Button6102 = QPushButton(self.gridLayoutWidget)
        self.Button6102.setObjectName(u"Button6102")
        sizePolicy.setHeightForWidth(self.Button6102.sizePolicy().hasHeightForWidth())
        self.Button6102.setSizePolicy(sizePolicy)
        self.Button6102.setFont(font)

        self.MachineLayout.addWidget(self.Button6102, 6, 3, 1, 1)

        self.Button2803 = QPushButton(self.gridLayoutWidget)
        self.Button2803.setObjectName(u"Button2803")
        sizePolicy.setHeightForWidth(self.Button2803.sizePolicy().hasHeightForWidth())
        self.Button2803.setSizePolicy(sizePolicy)
        self.Button2803.setFont(font)

        self.MachineLayout.addWidget(self.Button2803, 3, 5, 1, 1)

        self.Button4001 = QPushButton(self.gridLayoutWidget)
        self.Button4001.setObjectName(u"Button4001")
        sizePolicy.setHeightForWidth(self.Button4001.sizePolicy().hasHeightForWidth())
        self.Button4001.setSizePolicy(sizePolicy)
        self.Button4001.setFont(font)

        self.MachineLayout.addWidget(self.Button4001, 5, 1, 1, 1)

        self.Button6101 = QPushButton(self.gridLayoutWidget)
        self.Button6101.setObjectName(u"Button6101")
        sizePolicy.setHeightForWidth(self.Button6101.sizePolicy().hasHeightForWidth())
        self.Button6101.setSizePolicy(sizePolicy)
        self.Button6101.setFont(font)

        self.MachineLayout.addWidget(self.Button6101, 6, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(44, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.MachineLayout.addItem(self.verticalSpacer_2, 1, 6, 7, 1)

        self.ButtonExit = QPushButton(self.gridLayoutWidget)
        self.ButtonExit.setObjectName(u"ButtonExit")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.ButtonExit.setIcon(icon)
        self.ButtonExit.setIconSize(QSize(32, 32))
        self.ButtonExit.setCheckable(False)
        self.ButtonExit.setChecked(False)

        self.MachineLayout.addWidget(self.ButtonExit, 0, 0, 1, 1)

        self.Button2002 = QPushButton(self.gridLayoutWidget)
        self.Button2002.setObjectName(u"Button2002")
        sizePolicy.setHeightForWidth(self.Button2002.sizePolicy().hasHeightForWidth())
        self.Button2002.setSizePolicy(sizePolicy)
        self.Button2002.setFont(font)

        self.MachineLayout.addWidget(self.Button2002, 2, 4, 1, 1)

        self.Button3001 = QPushButton(self.gridLayoutWidget)
        self.Button3001.setObjectName(u"Button3001")
        sizePolicy.setHeightForWidth(self.Button3001.sizePolicy().hasHeightForWidth())
        self.Button3001.setSizePolicy(sizePolicy)
        self.Button3001.setFont(font)

        self.MachineLayout.addWidget(self.Button3001, 4, 1, 1, 1)

        self.Button2801 = QPushButton(self.gridLayoutWidget)
        self.Button2801.setObjectName(u"Button2801")
        sizePolicy.setHeightForWidth(self.Button2801.sizePolicy().hasHeightForWidth())
        self.Button2801.setSizePolicy(sizePolicy)
        self.Button2801.setFont(font)

        self.MachineLayout.addWidget(self.Button2801, 3, 3, 1, 1)

        self.Button3002 = QPushButton(self.gridLayoutWidget)
        self.Button3002.setObjectName(u"Button3002")
        sizePolicy.setHeightForWidth(self.Button3002.sizePolicy().hasHeightForWidth())
        self.Button3002.setSizePolicy(sizePolicy)
        self.Button3002.setFont(font)

        self.MachineLayout.addWidget(self.Button3002, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.MachineLayout.addItem(self.verticalSpacer, 1, 0, 7, 1)

        self.Button2001 = QPushButton(self.gridLayoutWidget)
        self.Button2001.setObjectName(u"Button2001")
        sizePolicy.setHeightForWidth(self.Button2001.sizePolicy().hasHeightForWidth())
        self.Button2001.setSizePolicy(sizePolicy)
        self.Button2001.setFont(font)

        self.MachineLayout.addWidget(self.Button2001, 2, 3, 1, 1)

        self.Button3501 = QPushButton(self.gridLayoutWidget)
        self.Button3501.setObjectName(u"Button3501")
        sizePolicy.setHeightForWidth(self.Button3501.sizePolicy().hasHeightForWidth())
        self.Button3501.setSizePolicy(sizePolicy)
        self.Button3501.setFont(font)

        self.MachineLayout.addWidget(self.Button3501, 4, 4, 1, 1)

        self.Button5501 = QPushButton(self.gridLayoutWidget)
        self.Button5501.setObjectName(u"Button5501")
        sizePolicy.setHeightForWidth(self.Button5501.sizePolicy().hasHeightForWidth())
        self.Button5501.setSizePolicy(sizePolicy)
        self.Button5501.setFont(font)

        self.MachineLayout.addWidget(self.Button5501, 6, 1, 1, 1)

        self.Button3101 = QPushButton(self.gridLayoutWidget)
        self.Button3101.setObjectName(u"Button3101")
        sizePolicy.setHeightForWidth(self.Button3101.sizePolicy().hasHeightForWidth())
        self.Button3101.setSizePolicy(sizePolicy)
        self.Button3101.setFont(font)

        self.MachineLayout.addWidget(self.Button3101, 4, 3, 1, 1)

        self.Button17001 = QPushButton(self.gridLayoutWidget)
        self.Button17001.setObjectName(u"Button17001")
        sizePolicy.setHeightForWidth(self.Button17001.sizePolicy().hasHeightForWidth())
        self.Button17001.setSizePolicy(sizePolicy)
        self.Button17001.setFont(font)

        self.MachineLayout.addWidget(self.Button17001, 6, 4, 1, 1)

        self.Button4501 = QPushButton(self.gridLayoutWidget)
        self.Button4501.setObjectName(u"Button4501")
        sizePolicy.setHeightForWidth(self.Button4501.sizePolicy().hasHeightForWidth())
        self.Button4501.setSizePolicy(sizePolicy)
        self.Button4501.setFont(font)

        self.MachineLayout.addWidget(self.Button4501, 5, 3, 1, 1)

        self.Button5001 = QPushButton(self.gridLayoutWidget)
        self.Button5001.setObjectName(u"Button5001")
        sizePolicy.setHeightForWidth(self.Button5001.sizePolicy().hasHeightForWidth())
        self.Button5001.setSizePolicy(sizePolicy)
        self.Button5001.setFont(font)

        self.MachineLayout.addWidget(self.Button5001, 5, 4, 1, 1)

        self.Button5002 = QPushButton(self.gridLayoutWidget)
        self.Button5002.setObjectName(u"Button5002")
        sizePolicy.setHeightForWidth(self.Button5002.sizePolicy().hasHeightForWidth())
        self.Button5002.setSizePolicy(sizePolicy)
        self.Button5002.setFont(font)

        self.MachineLayout.addWidget(self.Button5002, 5, 5, 1, 1)

        self.Button17002 = QPushButton(self.gridLayoutWidget)
        self.Button17002.setObjectName(u"Button17002")
        sizePolicy.setHeightForWidth(self.Button17002.sizePolicy().hasHeightForWidth())
        self.Button17002.setSizePolicy(sizePolicy)
        self.Button17002.setFont(font)

        self.MachineLayout.addWidget(self.Button17002, 6, 5, 1, 1)

        self.Button1802 = QPushButton(self.gridLayoutWidget)
        self.Button1802.setObjectName(u"Button1802")
        sizePolicy.setHeightForWidth(self.Button1802.sizePolicy().hasHeightForWidth())
        self.Button1802.setSizePolicy(sizePolicy)
        self.Button1802.setFont(font)

        self.MachineLayout.addWidget(self.Button1802, 2, 2, 1, 1)

        self.Button751 = QPushButton(self.gridLayoutWidget)
        self.Button751.setObjectName(u"Button751")
        sizePolicy.setHeightForWidth(self.Button751.sizePolicy().hasHeightForWidth())
        self.Button751.setSizePolicy(sizePolicy)
        self.Button751.setFont(font)

        self.MachineLayout.addWidget(self.Button751, 1, 1, 1, 1)

        self.Button4002 = QPushButton(self.gridLayoutWidget)
        self.Button4002.setObjectName(u"Button4002")
        sizePolicy.setHeightForWidth(self.Button4002.sizePolicy().hasHeightForWidth())
        self.Button4002.setSizePolicy(sizePolicy)
        self.Button4002.setFont(font)

        self.MachineLayout.addWidget(self.Button4002, 5, 2, 1, 1)

        self.Button2004 = QPushButton(self.gridLayoutWidget)
        self.Button2004.setObjectName(u"Button2004")
        sizePolicy.setHeightForWidth(self.Button2004.sizePolicy().hasHeightForWidth())
        self.Button2004.setSizePolicy(sizePolicy)
        self.Button2004.setFont(font)

        self.MachineLayout.addWidget(self.Button2004, 3, 1, 1, 1)

        self.Button1801 = QPushButton(self.gridLayoutWidget)
        self.Button1801.setObjectName(u"Button1801")
        sizePolicy.setHeightForWidth(self.Button1801.sizePolicy().hasHeightForWidth())
        self.Button1801.setSizePolicy(sizePolicy)
        self.Button1801.setFont(font)

        self.MachineLayout.addWidget(self.Button1801, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.MachineLayout.addItem(self.horizontalSpacer_2, 8, 1, 1, 5)

        self.Button2802 = QPushButton(self.gridLayoutWidget)
        self.Button2802.setObjectName(u"Button2802")
        sizePolicy.setHeightForWidth(self.Button2802.sizePolicy().hasHeightForWidth())
        self.Button2802.setSizePolicy(sizePolicy)
        self.Button2802.setFont(font)

        self.MachineLayout.addWidget(self.Button2802, 3, 4, 1, 1)

        self.Button2003 = QPushButton(self.gridLayoutWidget)
        self.Button2003.setObjectName(u"Button2003")
        sizePolicy.setHeightForWidth(self.Button2003.sizePolicy().hasHeightForWidth())
        self.Button2003.setSizePolicy(sizePolicy)
        self.Button2003.setFont(font)

        self.MachineLayout.addWidget(self.Button2003, 2, 5, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font)

        self.MachineLayout.addWidget(self.pushButton_7, 7, 1, 1, 1)

        self.Button1301 = QPushButton(self.gridLayoutWidget)
        self.Button1301.setObjectName(u"Button1301")
        sizePolicy.setHeightForWidth(self.Button1301.sizePolicy().hasHeightForWidth())
        self.Button1301.setSizePolicy(sizePolicy)
        self.Button1301.setFont(font)

        self.MachineLayout.addWidget(self.Button1301, 1, 5, 1, 1)

        self.Button3502 = QPushButton(self.gridLayoutWidget)
        self.Button3502.setObjectName(u"Button3502")
        sizePolicy.setHeightForWidth(self.Button3502.sizePolicy().hasHeightForWidth())
        self.Button3502.setSizePolicy(sizePolicy)
        self.Button3502.setFont(font)

        self.MachineLayout.addWidget(self.Button3502, 4, 5, 1, 1)

        self.Button2501 = QPushButton(self.gridLayoutWidget)
        self.Button2501.setObjectName(u"Button2501")
        sizePolicy.setHeightForWidth(self.Button2501.sizePolicy().hasHeightForWidth())
        self.Button2501.setSizePolicy(sizePolicy)
        self.Button2501.setFont(font)

        self.MachineLayout.addWidget(self.Button2501, 3, 2, 1, 1)

        self.Button753 = QPushButton(self.gridLayoutWidget)
        self.Button753.setObjectName(u"Button753")
        sizePolicy.setHeightForWidth(self.Button753.sizePolicy().hasHeightForWidth())
        self.Button753.setSizePolicy(sizePolicy)
        self.Button753.setFont(font)

        self.MachineLayout.addWidget(self.Button753, 1, 3, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Button752.setText(QCoreApplication.translate("Dialog", u"75-2", None))
        self.Button1001.setText(QCoreApplication.translate("Dialog", u"100-1", None))
        self.Button6102.setText(QCoreApplication.translate("Dialog", u"610-2", None))
        self.Button2803.setText(QCoreApplication.translate("Dialog", u"280-3", None))
        self.Button4001.setText(QCoreApplication.translate("Dialog", u"400-1", None))
        self.Button6101.setText(QCoreApplication.translate("Dialog", u"610-1", None))
        self.ButtonExit.setText("")
#if QT_CONFIG(shortcut)
        self.ButtonExit.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.Button2002.setText(QCoreApplication.translate("Dialog", u"200-2", None))
        self.Button3001.setText(QCoreApplication.translate("Dialog", u"300-1", None))
        self.Button2801.setText(QCoreApplication.translate("Dialog", u"280-1", None))
        self.Button3002.setText(QCoreApplication.translate("Dialog", u"300-2", None))
        self.Button2001.setText(QCoreApplication.translate("Dialog", u"200-1", None))
        self.Button3501.setText(QCoreApplication.translate("Dialog", u"350-1", None))
        self.Button5501.setText(QCoreApplication.translate("Dialog", u"550-1", None))
        self.Button3101.setText(QCoreApplication.translate("Dialog", u"310-1", None))
        self.Button17001.setText(QCoreApplication.translate("Dialog", u"1700-1", None))
        self.Button4501.setText(QCoreApplication.translate("Dialog", u"450-1", None))
        self.Button5001.setText(QCoreApplication.translate("Dialog", u"500-1", None))
        self.Button5002.setText(QCoreApplication.translate("Dialog", u"500-2", None))
        self.Button17002.setText(QCoreApplication.translate("Dialog", u"1700-2", None))
        self.Button1802.setText(QCoreApplication.translate("Dialog", u"180-2", None))
        self.Button751.setText(QCoreApplication.translate("Dialog", u"75-1", None))
        self.Button4002.setText(QCoreApplication.translate("Dialog", u"400-2", None))
        self.Button2004.setText(QCoreApplication.translate("Dialog", u"200-4", None))
        self.Button1801.setText(QCoreApplication.translate("Dialog", u"180-1", None))
        self.Button2802.setText(QCoreApplication.translate("Dialog", u"280-2", None))
        self.Button2003.setText(QCoreApplication.translate("Dialog", u"200-3", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Husky", None))
        self.Button1301.setText(QCoreApplication.translate("Dialog", u"130-1", None))
        self.Button3502.setText(QCoreApplication.translate("Dialog", u"350-2", None))
        self.Button2501.setText(QCoreApplication.translate("Dialog", u"250-1", None))
        self.Button753.setText(QCoreApplication.translate("Dialog", u"75-3", None))
    # retranslateUi

