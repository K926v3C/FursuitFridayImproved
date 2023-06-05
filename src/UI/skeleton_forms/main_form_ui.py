# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_download = QAction(MainWindow)
        self.action_download.setObjectName(u"action_download")
        self.action_change_folder = QAction(MainWindow)
        self.action_change_folder.setObjectName(u"action_change_folder")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_exit_app = QAction(MainWindow)
        self.action_exit_app.setObjectName(u"action_exit_app")
        self.action_change_topic = QAction(MainWindow)
        self.action_change_topic.setObjectName(u"action_change_topic")
        self.action_select_all = QAction(MainWindow)
        self.action_select_all.setObjectName(u"action_select_all")
        self.action_filter_by_user = QAction(MainWindow)
        self.action_filter_by_user.setObjectName(u"action_filter_by_user")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.checkBox_1 = QCheckBox(self.centralwidget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_1, 1, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_3, 1, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_5, 3, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_6, 3, 2, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)

        self.checkBox_7 = QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_7, 5, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.centralwidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_8, 5, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.centralwidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox_9, 5, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(70, 20, 70, -1)
        self.prev_button = QPushButton(self.centralwidget)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.prev_button)

        self.page_indicator = QLabel(self.centralwidget)
        self.page_indicator.setObjectName(u"page_indicator")
        self.page_indicator.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.page_indicator)

        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.next_button)


        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(267, 126, 149, 167))
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.prev_button, self.next_button)
        QWidget.setTabOrder(self.next_button, self.checkBox_1)
        QWidget.setTabOrder(self.checkBox_1, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.checkBox_4)
        QWidget.setTabOrder(self.checkBox_4, self.checkBox_5)
        QWidget.setTabOrder(self.checkBox_5, self.checkBox_6)
        QWidget.setTabOrder(self.checkBox_6, self.checkBox_7)
        QWidget.setTabOrder(self.checkBox_7, self.checkBox_8)
        QWidget.setTabOrder(self.checkBox_8, self.checkBox_9)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_select_all)
        self.menu.addAction(self.action_filter_by_user)
        self.menu.addAction(self.action_download)
        self.menu.addAction(self.action_change_folder)
        self.menu.addAction(self.action_change_topic)
        self.menu.addSeparator()
        self.menu.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FursuitFridaylmproved", None))
        self.action_download.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4e0b\u8f7d", None))
#if QT_CONFIG(shortcut)
        self.action_download.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_change_folder.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u4e0b\u8f7d\u4f4d\u7f6e\u2026\u2026", None))
#if QT_CONFIG(shortcut)
        self.action_change_folder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_exit_app.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u2026\u2026", None))
#if QT_CONFIG(tooltip)
        self.action_exit_app.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u672c\u5e94\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_exit_app.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.action_change_topic.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u8bdd\u9898\u2026\u2026", None))
        self.action_select_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
#if QT_CONFIG(shortcut)
        self.action_select_all.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_filter_by_user.setText(QCoreApplication.translate("MainWindow", u"\u6309\u7528\u6237\u540d\u8fc7\u6ee4", None))
#if QT_CONFIG(shortcut)
        self.action_filter_by_user.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.prev_button.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
#if QT_CONFIG(accessibility)
        self.menuBar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

