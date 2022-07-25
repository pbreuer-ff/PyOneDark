# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 798)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_settings = QWidget()
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_settings_layout_ = QVBoxLayout(self.menu_settings)
        self.menu_settings_layout_.setSpacing(5)
        self.menu_settings_layout_.setObjectName(u"menu_settings_layout_")
        self.menu_settings_layout_.setContentsMargins(5, 5, 5, 5)
        self.menu_settings_frame = QFrame(self.menu_settings)
        self.menu_settings_frame.setObjectName(u"menu_settings_frame")
        self.menu_settings_frame.setFrameShape(QFrame.NoFrame)
        self.menu_settings_frame.setFrameShadow(QFrame.Raised)
        self.menu_settings_layout = QVBoxLayout(self.menu_settings_frame)
        self.menu_settings_layout.setSpacing(0)
        self.menu_settings_layout.setObjectName(u"menu_settings_layout")
        self.menu_settings_layout.setContentsMargins(0, 0, 0, 0)

        self.menu_settings_layout_.addWidget(self.menu_settings_frame, 0, Qt.AlignTop)

        self.menus.addWidget(self.menu_settings)
        self.menu_help = QWidget()
        self.menu_help.setObjectName(u"menu_help")
        self.menu_help_layout_ = QVBoxLayout(self.menu_help)
        self.menu_help_layout_.setSpacing(5)
        self.menu_help_layout_.setObjectName(u"menu_help_layout_")
        self.menu_help_layout_.setContentsMargins(5, 5, 5, 5)
        self.menu_help_frame = QFrame(self.menu_help)
        self.menu_help_frame.setObjectName(u"menu_help_frame")
        self.menu_help_frame.setFrameShape(QFrame.NoFrame)
        self.menu_help_frame.setFrameShadow(QFrame.Raised)
        self.menu_help_layout = QVBoxLayout(self.menu_help_frame)
        self.menu_help_layout.setSpacing(0)
        self.menu_help_layout.setObjectName(u"menu_help_layout")
        self.menu_help_layout.setContentsMargins(0, 0, 0, 0)

        self.menu_help_layout_.addWidget(self.menu_help_frame, 0, Qt.AlignTop)

        self.menus.addWidget(self.menu_help)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
    # retranslateUi

