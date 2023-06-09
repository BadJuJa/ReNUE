# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(988, 557)
        MainWindow.setMinimumSize(QtCore.QSize(900, 550))
        MainWindow.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "font: 75 13pt \"Century Gothic\";\n"
            "selection-background-color: rgb(188, 188, 188);\n"
            "selection-color: rgb(0, 0, 0);\n"
            "border-color: rgb(15, 15, 15);\n"
            "background-color: rgb(63, 63, 63);\n"
            "alternate-background-color: rgb(188, 188, 188);\n"
            "QMenuBar::item:selected {\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0);\n"
            "}"
        )
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self._centralwidget = QtWidgets.QWidget(MainWindow)
        self._centralwidget.setObjectName("_centralwidget")
        self._central_widget_gridLayout = QtWidgets.QGridLayout(self._centralwidget)
        self._central_widget_gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self._central_widget_gridLayout.setContentsMargins(0, 0, 0, 0)
        self._central_widget_gridLayout.setSpacing(0)
        self._central_widget_gridLayout.setObjectName("_central_widget_gridLayout")
        self._centralwidget_grips = QtWidgets.QWidget(self._centralwidget)
        self._centralwidget_grips.setAutoFillBackground(False)
        self._centralwidget_grips.setObjectName("_centralwidget_grips")
        self._centralwidget_grips_gridLayout = QtWidgets.QGridLayout(self._centralwidget_grips)
        self._centralwidget_grips_gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self._centralwidget_grips_gridLayout.setContentsMargins(0, 0, 0, 0)
        self._centralwidget_grips_gridLayout.setSpacing(0)
        self._centralwidget_grips_gridLayout.setObjectName("_centralwidget_grips_gridLayout")
        self.centralwidget = QtWidgets.QWidget(self._centralwidget_grips)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget_gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.centralwidget_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget_gridLayout.setSpacing(0)
        self.centralwidget_gridLayout.setObjectName("centralwidget_gridLayout")
        self.widget_timeline = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_timeline.sizePolicy().hasHeightForWidth())
        self.widget_timeline.setSizePolicy(sizePolicy)
        self.widget_timeline.setMinimumSize(QtCore.QSize(0, 35))
        self.widget_timeline.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widget_timeline.setObjectName("widget_timeline")
        self.centralwidget_gridLayout.addWidget(self.widget_timeline, 2, 0, 1, 1)
        self.title_bar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar.setObjectName("title_bar")
        self.title_bar_horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.title_bar_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar_horizontalLayout.setSpacing(0)
        self.title_bar_horizontalLayout.setObjectName("title_bar_horizontalLayout")
        self.button_menu = QtWidgets.QPushButton(self.title_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_menu.sizePolicy().hasHeightForWidth())
        self.button_menu.setSizePolicy(sizePolicy)
        self.button_menu.setMinimumSize(QtCore.QSize(100, 30))
        self.button_menu.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(60, 60, 60);\n"
            "border-bottom-right-radius: 10%;\n"
            "border: 1px solid rgb(188, 188, 188);\n"
            "font-size: 16pt;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0);\n""}"
        )
        self.button_menu.setObjectName("button_menu")
        self.title_bar_horizontalLayout.addWidget(self.button_menu)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title_bar_horizontalLayout.addItem(spacerItem)
        self.widget_header_buttons = QtWidgets.QWidget(self.title_bar)
        self.widget_header_buttons.setMinimumSize(QtCore.QSize(90, 30))
        self.widget_header_buttons.setMaximumSize(QtCore.QSize(30, 30))
        self.widget_header_buttons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_header_buttons.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(60, 60, 60);\n"
            "border: 0px solid rgb(188, 188, 188);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0);\n""}"
        )
        self.widget_header_buttons.setObjectName("widget_header_buttons")
        self.widget_header_buttons_horizontalLayout = QtWidgets.QHBoxLayout(self.widget_header_buttons)
        self.widget_header_buttons_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_header_buttons_horizontalLayout.setSpacing(0)
        self.widget_header_buttons_horizontalLayout.setObjectName("widget_header_buttons_horizontalLayout")
        self.button_minimize = QtWidgets.QPushButton(self.widget_header_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minimize.sizePolicy().hasHeightForWidth())
        self.button_minimize.setSizePolicy(sizePolicy)
        self.button_minimize.setMinimumSize(QtCore.QSize(30, 30))
        self.button_minimize.setMaximumSize(QtCore.QSize(30, 30))
        self.button_minimize.setStyleSheet(
            "QPushButton {\n"
            "border-bottom-left-radius: 10%;\n"
            "border-bottom-right-radius: 10%;\n""}"
        )
        self.button_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_minimize.setIcon(icon)
        self.button_minimize.setIconSize(QtCore.QSize(24, 24))
        self.button_minimize.setObjectName("button_minimize")
        self.widget_header_buttons_horizontalLayout.addWidget(self.button_minimize)
        self.button_maximize = QtWidgets.QPushButton(self.widget_header_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_maximize.sizePolicy().hasHeightForWidth())
        self.button_maximize.setSizePolicy(sizePolicy)
        self.button_maximize.setMinimumSize(QtCore.QSize(30, 30))
        self.button_maximize.setMaximumSize(QtCore.QSize(30, 30))
        self.button_maximize.setStyleSheet(
            "QPushButton {\n"
            "border-bottom-left-radius: 10%;\n"
            "border-bottom-right-radius: 10%;\n""}"
        )
        self.button_maximize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_maximize.setIcon(icon1)
        self.button_maximize.setIconSize(QtCore.QSize(24, 24))
        self.button_maximize.setObjectName("button_maximize")
        self.widget_header_buttons_horizontalLayout.addWidget(self.button_maximize)
        self.button_exit = QtWidgets.QPushButton(self.widget_header_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy)
        self.button_exit.setMinimumSize(QtCore.QSize(30, 30))
        self.button_exit.setMaximumSize(QtCore.QSize(30, 30))
        self.button_exit.setStyleSheet(
            "QPushButton {\n"
            "border-bottom-left-radius: 10%;\n""}"
        )
        self.button_exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/assets/close-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_exit.setIcon(icon2)
        self.button_exit.setIconSize(QtCore.QSize(48, 48))
        self.button_exit.setObjectName("button_exit")
        self.widget_header_buttons_horizontalLayout.addWidget(self.button_exit)
        self.title_bar_horizontalLayout.addWidget(self.widget_header_buttons)
        self.centralwidget_gridLayout.addWidget(self.title_bar, 0, 0, 1, 1)
        self.widget_bottom = QtWidgets.QWidget(self.centralwidget)
        self.widget_bottom.setObjectName("widget_bottom")
        self.widget_bottom_horizontalLayout = QtWidgets.QHBoxLayout(self.widget_bottom)
        self.widget_bottom_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_bottom_horizontalLayout.setSpacing(0)
        self.widget_bottom_horizontalLayout.setObjectName("widget_bottom_horizontalLayout")
        self.widget_tabs = QtWidgets.QWidget(self.widget_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_tabs.sizePolicy().hasHeightForWidth())
        self.widget_tabs.setSizePolicy(sizePolicy)
        self.widget_tabs.setMinimumSize(QtCore.QSize(500, 200))
        self.widget_tabs.setObjectName("widget_tabs")
        self.widget_tabs_horizontalLayout = QtWidgets.QHBoxLayout(self.widget_tabs)
        self.widget_tabs_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_tabs_horizontalLayout.setSpacing(4)
        self.widget_tabs_horizontalLayout.setObjectName("widget_tabs_horizontalLayout")
        self.widget_left_buttons = QtWidgets.QWidget(self.widget_tabs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left_buttons.sizePolicy().hasHeightForWidth())
        self.widget_left_buttons.setSizePolicy(sizePolicy)
        self.widget_left_buttons.setMinimumSize(QtCore.QSize(120, 0))
        self.widget_left_buttons.setMaximumSize(QtCore.QSize(120, 16777215))
        self.widget_left_buttons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_left_buttons.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(60, 60, 60);\n"
            "border: 1px solid rgb(188, 188, 188);\n"
            "border-left: 0px solid;\n"
            "border-top-right-radius: 10%;\n"
            "border-bottom-right-radius: 10%;\n"
            "font-size: 16pt;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0);\n"
            "}\n"
            )
        self.widget_left_buttons.setObjectName("widget_left_buttons")
        self.widget_left_buttons_verticalLayout = QtWidgets.QVBoxLayout(self.widget_left_buttons)
        self.widget_left_buttons_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_left_buttons_verticalLayout.setSpacing(5)
        self.widget_left_buttons_verticalLayout.setObjectName("widget_left_buttons_verticalLayout")
        self.button_all_audio = QtWidgets.QPushButton(self.widget_left_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_all_audio.sizePolicy().hasHeightForWidth())
        self.button_all_audio.setSizePolicy(sizePolicy)
        self.button_all_audio.setStyleSheet("")
        self.button_all_audio.setCheckable(False)
        self.button_all_audio.setAutoExclusive(False)
        self.button_all_audio.setAutoDefault(False)
        self.button_all_audio.setObjectName("button_all_audio")
        self.widget_left_buttons_verticalLayout.addWidget(self.button_all_audio)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget_left_buttons)
        self.lcdNumber.setStyleSheet("border: 0px")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setObjectName("lcdNumber")
        self.widget_left_buttons_verticalLayout.addWidget(self.lcdNumber)
        self.button_playlists = QtWidgets.QPushButton(self.widget_left_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_playlists.sizePolicy().hasHeightForWidth())
        self.button_playlists.setSizePolicy(sizePolicy)
        self.button_playlists.setStyleSheet("")
        self.button_playlists.setObjectName("button_playlists")
        self.widget_left_buttons_verticalLayout.addWidget(self.button_playlists)
        self.button_add_playlist = QtWidgets.QPushButton(self.widget_left_buttons)
        self.button_add_playlist.setEnabled(True)
        self.button_add_playlist.setStyleSheet("")
        self.button_add_playlist.setObjectName("button_add_playlist")
        self.widget_left_buttons_verticalLayout.addWidget(self.button_add_playlist)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.widget_left_buttons_verticalLayout.addItem(spacerItem1)
        self.widget_tabs_horizontalLayout.addWidget(self.widget_left_buttons)
        self.tabWidget_main = QtWidgets.QTabWidget(self.widget_tabs)
        self.tabWidget_main.setAutoFillBackground(False)
        self.tabWidget_main.setStyleSheet(
            "QTabBar {\n"
            "font: 13pt \"Century Gothic\";\n"
            "border: 0px solid;\n"
            "width: 1px;\n"
            "}\n"
            "QTabBar:tab {\n"
            "font: 13pt \"Century Gothic\";\n"
            "background-color: rgb(63, 63, 63);\n"
            "width: 0px;\n"
            "}\n"
            "QTabBar:tab:hover {\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0)\n"
            "}\n"
            "QTabBar:tab:selected {\n"
            "background-color: rgb(160, 160, 160);\n"
            "color: rgb(12, 12, 12);\n"
            "}\n"
            "QTabWidget::pane {}")
        self.tabWidget_main.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_main.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_main.setIconSize(QtCore.QSize(0, 0))
        self.tabWidget_main.setUsesScrollButtons(False)
        self.tabWidget_main.setObjectName("tabWidget_main")
        self.tab_all_audio = QtWidgets.QWidget()
        self.tab_all_audio.setObjectName("tab_all_audio")
        self.tab_all_songs_gridLayout = QtWidgets.QGridLayout(self.tab_all_audio)
        self.tab_all_songs_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_all_songs_gridLayout.setSpacing(0)
        self.tab_all_songs_gridLayout.setObjectName("tab_all_songs_gridLayout")
        self.tableWidget_all_audio = QtWidgets.QTableWidget(self.tab_all_audio)
        self.tableWidget_all_audio.setMinimumSize(QtCore.QSize(501, 0))
        self.tableWidget_all_audio.setStyleSheet(
            "QHeaderView {\n"
            "    background: transparent;\n"
            "    border: 0px solid;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    background-color: rgb(63, 63, 63);\n"
            "    color: white;\n"
            "    border: 0px solid;\n"
            "}\n"
            "QTableCornerButton::section {\n"
            "    background-color: rgb(63,63, 63);\n"
            "    border: 0px solid;\n"
            "}")
        self.tableWidget_all_audio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_all_audio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_all_audio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_all_audio.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_all_audio.setTabKeyNavigation(False)
        self.tableWidget_all_audio.setDragDropOverwriteMode(False)
        self.tableWidget_all_audio.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_all_audio.setShowGrid(False)
        self.tableWidget_all_audio.setObjectName("tableWidget_all_audio")
        self.tableWidget_all_audio.setColumnCount(1)
        self.tableWidget_all_audio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_all_audio.setHorizontalHeaderItem(0, item)
        self.tableWidget_all_audio.horizontalHeader().setVisible(False)
        self.tableWidget_all_audio.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_all_audio.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_all_audio.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_all_audio.verticalHeader().setVisible(False)
        self.tableWidget_all_audio.verticalHeader().setHighlightSections(False)
        self.tab_all_songs_gridLayout.addWidget(self.tableWidget_all_audio, 0, 0, 1, 1)
        self.tabWidget_main.addTab(self.tab_all_audio, "")
        self.tab_all_playlists = QtWidgets.QWidget()
        self.tab_all_playlists.setObjectName("tab_all_playlists")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_all_playlists)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_playlists_table = QtWidgets.QTableWidget(self.tab_all_playlists)
        self.tableWidget_playlists_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_playlists_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_playlists_table.setTabKeyNavigation(False)
        self.tableWidget_playlists_table.setProperty("showDropIndicator", False)
        self.tableWidget_playlists_table.setDragDropOverwriteMode(False)
        self.tableWidget_playlists_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_playlists_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_playlists_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_playlists_table.setObjectName("tableWidget_playlists_table")
        self.tableWidget_playlists_table.setColumnCount(0)
        self.tableWidget_playlists_table.setRowCount(0)
        self.tableWidget_playlists_table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tableWidget_playlists_table, 0, 1, 1, 1)
        self.tabWidget_main.addTab(self.tab_all_playlists, "")
        self.widget_tabs_horizontalLayout.addWidget(self.tabWidget_main)
        self.widget_bottom_horizontalLayout.addWidget(self.widget_tabs)
        self.widget_current_playlist = QtWidgets.QWidget(self.widget_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_current_playlist.sizePolicy().hasHeightForWidth())
        self.widget_current_playlist.setSizePolicy(sizePolicy)
        self.widget_current_playlist.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_current_playlist.setObjectName("widget_current_playlist")
        self.widget_current_playlist_verticalLayout = QtWidgets.QVBoxLayout(self.widget_current_playlist)
        self.widget_current_playlist_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_current_playlist_verticalLayout.setSpacing(0)
        self.widget_current_playlist_verticalLayout.setObjectName("widget_current_playlist_verticalLayout")
        self.label_currently_playing = QtWidgets.QLabel(self.widget_current_playlist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_currently_playing.sizePolicy().hasHeightForWidth())
        self.label_currently_playing.setSizePolicy(sizePolicy)
        self.label_currently_playing.setMinimumSize(QtCore.QSize(250, 30))
        self.label_currently_playing.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_currently_playing.setFont(font)
        self.label_currently_playing.setStyleSheet(
            "QLabel {\n"
            "background-color: rgb(60, 60, 60);\n"
            "border: 1px solid rgb(188, 188, 188);\n"
            "border-left: 2px solid rgb(188, 188, 188);\n"
            "font-size: 16pt;\n"
            "}")
        self.label_currently_playing.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currently_playing.setObjectName("label_currently_playing")
        self.widget_current_playlist_verticalLayout.addWidget(self.label_currently_playing)
        self.listWidget_current_playlist = QtWidgets.QListWidget(self.widget_current_playlist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_current_playlist.sizePolicy().hasHeightForWidth())
        self.listWidget_current_playlist.setSizePolicy(sizePolicy)
        self.listWidget_current_playlist.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget_current_playlist.setStyleSheet(
            "QListWidget:item:selected {\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0);\n"
            "}")
        self.listWidget_current_playlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_current_playlist.setProperty("showDropIndicator", False)
        self.listWidget_current_playlist.setProperty("isWrapping", False)
        self.listWidget_current_playlist.setWordWrap(True)
        self.listWidget_current_playlist.setObjectName("listWidget_current_playlist")
        self.widget_current_playlist_verticalLayout.addWidget(self.listWidget_current_playlist)
        self.widget_bottom_horizontalLayout.addWidget(self.widget_current_playlist)
        self.centralwidget_gridLayout.addWidget(self.widget_bottom, 3, 0, 1, 1)
        self.widget_player = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_player.sizePolicy().hasHeightForWidth())
        self.widget_player.setSizePolicy(sizePolicy)
        self.widget_player.setMinimumSize(QtCore.QSize(0, 90))
        self.widget_player.setMaximumSize(QtCore.QSize(16777215, 90))
        self.widget_player.setObjectName("widget_player")
        self.widget_player_gridLayout = QtWidgets.QGridLayout(self.widget_player)
        self.widget_player_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_player_gridLayout.setSpacing(0)
        self.widget_player_gridLayout.setObjectName("widget_player_gridLayout")
        self.widget_audio_info = QtWidgets.QWidget(self.widget_player)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_audio_info.sizePolicy().hasHeightForWidth())
        self.widget_audio_info.setSizePolicy(sizePolicy)
        self.widget_audio_info.setMinimumSize(QtCore.QSize(350, 90))
        self.widget_audio_info.setMaximumSize(QtCore.QSize(16777215, 90))
        self.widget_audio_info.setObjectName("widget_audio_info")
        self.widget_song_info_horizontalLayout = QtWidgets.QHBoxLayout(self.widget_audio_info)
        self.widget_song_info_horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget_song_info_horizontalLayout.setSpacing(10)
        self.widget_song_info_horizontalLayout.setObjectName("widget_song_info_horizontalLayout")
        self.label_audio_icon = QtWidgets.QLabel(self.widget_audio_info)
        self.label_audio_icon.setMinimumSize(QtCore.QSize(80, 80))
        self.label_audio_icon.setMaximumSize(QtCore.QSize(80, 80))
        self.label_audio_icon.setText("")
        self.label_audio_icon.setObjectName("label_audio_icon")
        self.widget_song_info_horizontalLayout.addWidget(self.label_audio_icon)
        self.label_audio_name = QtWidgets.QLabel(self.widget_audio_info)
        self.label_audio_name.setMinimumSize(QtCore.QSize(0, 80))
        self.label_audio_name.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_audio_name.setText("")
        self.label_audio_name.setWordWrap(True)
        self.label_audio_name.setObjectName("label_audio_name")
        self.widget_song_info_horizontalLayout.addWidget(self.label_audio_name)
        self.widget_player_gridLayout.addWidget(self.widget_audio_info, 0, 0, 1, 1)
        self.widget_audio_parameters = QtWidgets.QWidget(self.widget_player)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_audio_parameters.sizePolicy().hasHeightForWidth())
        self.widget_audio_parameters.setSizePolicy(sizePolicy)
        self.widget_audio_parameters.setMinimumSize(QtCore.QSize(350, 90))
        self.widget_audio_parameters.setMaximumSize(QtCore.QSize(16777215, 90))
        self.widget_audio_parameters.setStyleSheet("border: 0px solid")
        self.widget_audio_parameters.setObjectName("widget_audio_parameters")
        self.widget_song_parameters_horizontalLayout = QtWidgets.QHBoxLayout(self.widget_audio_parameters)
        self.widget_song_parameters_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_song_parameters_horizontalLayout.setSpacing(0)
        self.widget_song_parameters_horizontalLayout.setObjectName("widget_song_parameters_horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.widget_song_parameters_horizontalLayout.addItem(spacerItem2)
        self.tabWidget_audio_parameters = QtWidgets.QTabWidget(self.widget_audio_parameters)
        self.tabWidget_audio_parameters.setMinimumSize(QtCore.QSize(350, 90))
        self.tabWidget_audio_parameters.setMaximumSize(QtCore.QSize(350, 90))
        self.tabWidget_audio_parameters.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_audio_parameters.setStyleSheet(
            "QTabBar {\n"
            "font: 13pt \"Century Gothic\";\n"
            "border: 0px solid;\n"
            "}\n"
            "QTabBar:tab {\n"
            "font: 13pt \"Century Gothic\";\n"
            "background-color: rgb(63, 63, 63);\n"
            "height: 0px;\n"
            "}\n"
            "QTabBar:tab:hover {\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0)\n"
            "}\n"
            "QTabBar:tab:selected {\n"
            "background-color: rgb(160, 160, 160);\n"
            "color: rgb(12, 12, 12);\n"
            "}\n"
            "QTabWidget::pane {}")
        self.tabWidget_audio_parameters.setIconSize(QtCore.QSize(0, 0))
        self.tabWidget_audio_parameters.setUsesScrollButtons(False)
        self.tabWidget_audio_parameters.setObjectName("tabWidget_audio_parameters")
        self.tab_audio_parameters_sliders = QtWidgets.QWidget()
        self.tab_audio_parameters_sliders.setStyleSheet("border: 0px solid;")
        self.tab_audio_parameters_sliders.setObjectName("tab_audio_parameters_sliders")
        self.tab_song_parameters_sliders_gridLayout = QtWidgets.QGridLayout(self.tab_audio_parameters_sliders)
        self.tab_song_parameters_sliders_gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.tab_song_parameters_sliders_gridLayout.setContentsMargins(2, 0, 5, 0)
        self.tab_song_parameters_sliders_gridLayout.setHorizontalSpacing(5)
        self.tab_song_parameters_sliders_gridLayout.setVerticalSpacing(0)
        self.tab_song_parameters_sliders_gridLayout.setObjectName("tab_song_parameters_sliders_gridLayout")
        self.horizontalSlider_volume = QtWidgets.QSlider(self.tab_audio_parameters_sliders)
        self.horizontalSlider_volume.setMinimumSize(QtCore.QSize(0, 60))
        self.horizontalSlider_volume.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.horizontalSlider_volume.setFont(font)
        self.horizontalSlider_volume.setMaximum(100)
        self.horizontalSlider_volume.setProperty("value", 100)
        self.horizontalSlider_volume.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_volume.setInvertedControls(False)
        self.horizontalSlider_volume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_volume.setTickInterval(10)
        self.horizontalSlider_volume.setObjectName("horizontalSlider_volume")
        self.tab_song_parameters_sliders_gridLayout.addWidget(self.horizontalSlider_volume, 0, 0, 1, 1)
        self.label_volume_slider = QtWidgets.QLabel(self.tab_audio_parameters_sliders)
        self.label_volume_slider.setMinimumSize(QtCore.QSize(0, 40))
        self.label_volume_slider.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_volume_slider.setFont(font)
        self.label_volume_slider.setStyleSheet(
            "QLabel {\n"
            "background-color: rgb(60, 60, 60);\n"
            "}")
        self.label_volume_slider.setObjectName("label_volume_slider")
        self.tab_song_parameters_sliders_gridLayout.addWidget(self.label_volume_slider, 0, 2, 1, 1)
        self.tab_song_parameters_sliders_gridLayout.setRowStretch(0, 1)
        self.tabWidget_audio_parameters.addTab(self.tab_audio_parameters_sliders, "")
        self.widget_song_parameters_horizontalLayout.addWidget(self.tabWidget_audio_parameters)
        self.widget_player_gridLayout.addWidget(self.widget_audio_parameters, 0, 2, 1, 1)
        self.audio_control_buttons = QtWidgets.QWidget(self.widget_player)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audio_control_buttons.sizePolicy().hasHeightForWidth())
        self.audio_control_buttons.setSizePolicy(sizePolicy)
        self.audio_control_buttons.setMinimumSize(QtCore.QSize(200, 90))
        self.audio_control_buttons.setMaximumSize(QtCore.QSize(200, 90))
        self.audio_control_buttons.setObjectName("audio_control_buttons")
        self.song_control_buttons_gridLayout = QtWidgets.QGridLayout(self.audio_control_buttons)
        self.song_control_buttons_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.song_control_buttons_gridLayout.setHorizontalSpacing(10)
        self.song_control_buttons_gridLayout.setVerticalSpacing(0)
        self.song_control_buttons_gridLayout.setObjectName("song_control_buttons_gridLayout")
        self.widget_restore_repeat_shuffle = QtWidgets.QWidget(self.audio_control_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_restore_repeat_shuffle.sizePolicy().hasHeightForWidth())
        self.widget_restore_repeat_shuffle.setSizePolicy(sizePolicy)
        self.widget_restore_repeat_shuffle.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_restore_repeat_shuffle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_restore_repeat_shuffle.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(60, 60, 60);\n"
            "border: 1px solid rgb(188, 188, 188);\n"
            "border-radius: 15%;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0);\n"
            "}")
        self.widget_restore_repeat_shuffle.setObjectName("widget_restore_repeat_shuffle")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_restore_repeat_shuffle)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(17)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_stop = QtWidgets.QPushButton(self.widget_restore_repeat_shuffle)
        self.button_stop.setMaximumSize(QtCore.QSize(30, 30))
        self.button_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_stop.setStyleSheet("")
        self.button_stop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/assets/stop-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_stop.setIcon(icon3)
        self.button_stop.setIconSize(QtCore.QSize(30, 30))
        self.button_stop.setObjectName("button_stop")
        self.gridLayout_2.addWidget(self.button_stop, 0, 0, 1, 1)
        self.button_repeat = QtWidgets.QPushButton(self.widget_restore_repeat_shuffle)
        self.button_repeat.setMaximumSize(QtCore.QSize(30, 30))
        self.button_repeat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_repeat.setStyleSheet("")
        self.button_repeat.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/assets/repeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_repeat.setIcon(icon4)
        self.button_repeat.setIconSize(QtCore.QSize(32, 32))
        self.button_repeat.setObjectName("button_repeat")
        self.gridLayout_2.addWidget(self.button_repeat, 0, 1, 1, 1)
        self.button_shuffle = QtWidgets.QPushButton(self.widget_restore_repeat_shuffle)
        self.button_shuffle.setMaximumSize(QtCore.QSize(30, 30))
        self.button_shuffle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_shuffle.setStyleSheet("")
        self.button_shuffle.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/assets/shuffle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_shuffle.setIcon(icon5)
        self.button_shuffle.setIconSize(QtCore.QSize(32, 32))
        self.button_shuffle.setObjectName("button_shuffle")
        self.gridLayout_2.addWidget(self.button_shuffle, 0, 2, 1, 1)
        self.song_control_buttons_gridLayout.addWidget(self.widget_restore_repeat_shuffle, 1, 0, 1, 2)
        self.widget_prev_play_next = QtWidgets.QWidget(self.audio_control_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_prev_play_next.sizePolicy().hasHeightForWidth())
        self.widget_prev_play_next.setSizePolicy(sizePolicy)
        self.widget_prev_play_next.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_prev_play_next.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_prev_play_next.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(60, 60, 60);\n"
            "border: 1px solid rgb(188, 188, 188);\n"
            "border-radius: 20%;\n"
            "font-size: 14pt;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(188, 188, 188);\n"
            "color: rgb(0, 0, 0);\n"
            "}")
        self.widget_prev_play_next.setObjectName("widget_prev_play_next")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_prev_play_next)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_previous_audio = QtWidgets.QPushButton(self.widget_prev_play_next)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_previous_audio.sizePolicy().hasHeightForWidth())
        self.button_previous_audio.setSizePolicy(sizePolicy)
        self.button_previous_audio.setMinimumSize(QtCore.QSize(40, 40))
        self.button_previous_audio.setMaximumSize(QtCore.QSize(40, 40))
        self.button_previous_audio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_previous_audio.setStyleSheet("")
        self.button_previous_audio.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/assets/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_previous_audio.setIcon(icon6)
        self.button_previous_audio.setIconSize(QtCore.QSize(40, 40))
        self.button_previous_audio.setObjectName("button_previous_audio")
        self.gridLayout.addWidget(self.button_previous_audio, 0, 0, 1, 1)
        self.button_play_pause = QtWidgets.QPushButton(self.widget_prev_play_next)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_play_pause.sizePolicy().hasHeightForWidth())
        self.button_play_pause.setSizePolicy(sizePolicy)
        self.button_play_pause.setMinimumSize(QtCore.QSize(50, 50))
        self.button_play_pause.setMaximumSize(QtCore.QSize(50, 50))
        self.button_play_pause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_play_pause.setStyleSheet("QPushButton {border-radius: 25%;}")
        self.button_play_pause.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/assets/play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_play_pause.setIcon(icon7)
        self.button_play_pause.setIconSize(QtCore.QSize(48, 48))
        self.button_play_pause.setObjectName("button_play_pause")
        self.gridLayout.addWidget(self.button_play_pause, 0, 1, 1, 1)
        self.button_next_audio = QtWidgets.QPushButton(self.widget_prev_play_next)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_next_audio.sizePolicy().hasHeightForWidth())
        self.button_next_audio.setSizePolicy(sizePolicy)
        self.button_next_audio.setMinimumSize(QtCore.QSize(40, 40))
        self.button_next_audio.setMaximumSize(QtCore.QSize(40, 40))
        self.button_next_audio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_next_audio.setStyleSheet("")
        self.button_next_audio.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/assets/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_next_audio.setIcon(icon8)
        self.button_next_audio.setIconSize(QtCore.QSize(40, 40))
        self.button_next_audio.setObjectName("button_next_audio")
        self.gridLayout.addWidget(self.button_next_audio, 0, 2, 1, 1)
        self.song_control_buttons_gridLayout.addWidget(self.widget_prev_play_next, 0, 0, 1, 2)
        self.widget_player_gridLayout.addWidget(self.audio_control_buttons, 0, 1, 1, 1)
        self.widget_player_gridLayout.setColumnStretch(0, 1)
        self.widget_player_gridLayout.setColumnStretch(1, 1)
        self.widget_player_gridLayout.setColumnStretch(2, 1)
        self.centralwidget_gridLayout.addWidget(self.widget_player, 1, 0, 1, 1)
        self._centralwidget_grips_gridLayout.addWidget(self.centralwidget, 0, 0, 1, 1)
        self._central_widget_gridLayout.addWidget(self._centralwidget_grips, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self._centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setMinimumSize(QtCore.QSize(0, 5))
        self.statusBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")

        self.retranslateUi(MainWindow)
        self.tabWidget_main.setCurrentIndex(0)
        self.tabWidget_audio_parameters.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_menu.setText(_translate("MainWindow", "Меню"))
        self.button_all_audio.setText(_translate("MainWindow", "Все файлы"))
        self.button_playlists.setText(_translate("MainWindow", "Плейлисты"))
        self.button_add_playlist.setText(_translate("MainWindow", "Добавить"))
        self.tableWidget_all_audio.setSortingEnabled(True)
        item = self.tableWidget_all_audio.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_all_audio),
                                       _translate("MainWindow", "Page"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_all_playlists),
                                       _translate("MainWindow", "Page"))
        self.label_currently_playing.setText(_translate("MainWindow", "ТЕКУЩИЙ ПЛЕЙЛИСТ"))
        self.label_volume_slider.setText(_translate("MainWindow", "ГРОМКОСТЬ"))
        self.tabWidget_audio_parameters.setTabText(
            self.tabWidget_audio_parameters.indexOf(self.tab_audio_parameters_sliders),
            _translate("MainWindow", "Tab 2"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))


import resources_rc
