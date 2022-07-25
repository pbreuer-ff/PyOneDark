# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.menu_1_layout = QVBoxLayout(self.menu_1)
        self.menu_1_layout.setSpacing(5)
        self.menu_1_layout.setObjectName(u"menu_1_layout")
        self.menu_1_layout.setContentsMargins(5, 5, 5, 5)
        self.menu_telem_frame = QFrame(self.menu_1)
        self.menu_telem_frame.setObjectName(u"menu_telem_frame")
        self.menu_telem_frame.setFrameShape(QFrame.NoFrame)
        self.menu_telem_frame.setFrameShadow(QFrame.Raised)
        self.menu_telem_layout = QVBoxLayout(self.menu_telem_frame)
        self.menu_telem_layout.setSpacing(20)
        self.menu_telem_layout.setObjectName(u"menu_telem_layout")
        self.menu_telem_layout.setContentsMargins(0, 0, 0, 0)

        self.menu_1_layout.addWidget(self.menu_telem_frame, 0, Qt.AlignTop)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2_layout = QVBoxLayout(self.menu_2)
        self.menu_2_layout.setSpacing(5)
        self.menu_2_layout.setObjectName(u"menu_2_layout")
        self.menu_2_layout.setContentsMargins(5, 5, 5, 5)
        self.menu_emergency_frame = QFrame(self.menu_2)
        self.menu_emergency_frame.setObjectName(u"menu_emergency_frame")
        self.menu_emergency_frame.setFrameShape(QFrame.NoFrame)
        self.menu_emergency_frame.setFrameShadow(QFrame.Raised)
        self.menu_emergency_layout = QVBoxLayout(self.menu_emergency_frame)
        self.menu_emergency_layout.setSpacing(20)
        self.menu_emergency_layout.setObjectName(u"menu_emergency_layout")
        self.menu_emergency_layout.setContentsMargins(0, 0, 0, 0)

        self.menu_2_layout.addWidget(self.menu_emergency_frame, 0, Qt.AlignTop)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
    # retranslateUi

