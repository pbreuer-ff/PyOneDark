# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(994, 631)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(432, 288))
        self.welcome_base.setMaximumSize(QSize(432, 288))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(432, 288))
        self.logo.setMaximumSize(QSize(432, 288))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(0, -1, -1, -1)
        self.page_2_frame = QFrame(self.page_2)
        self.page_2_frame.setObjectName(u"page_2_frame")
        self.page_2_frame.setMinimumSize(QSize(0, 500))
        self.page_2_frame.setMaximumSize(QSize(16777215, 500))
        self.page_2_frame.setLayoutDirection(Qt.LeftToRight)
        self.page_2_frame.setFrameShape(QFrame.NoFrame)
        self.page_2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.page_2_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page_2_contents = QVBoxLayout()
        self.page_2_contents.setSpacing(10)
        self.page_2_contents.setObjectName(u"page_2_contents")
        self.p2_svg_astro_frame = QFrame(self.page_2_frame)
        self.p2_svg_astro_frame.setObjectName(u"p2_svg_astro_frame")
        self.p2_svg_astro_frame.setMinimumSize(QSize(0, 200))
        self.p2_svg_astro_frame.setMaximumSize(QSize(16777215, 200))
        self.p2_svg_astro_frame.setFrameShape(QFrame.NoFrame)
        self.p2_svg_astro_frame.setFrameShadow(QFrame.Raised)
        self.p2_svg_astro_layout = QVBoxLayout(self.p2_svg_astro_frame)
        self.p2_svg_astro_layout.setSpacing(0)
        self.p2_svg_astro_layout.setObjectName(u"p2_svg_astro_layout")
        self.p2_svg_astro_layout.setContentsMargins(0, 0, 0, 0)

        self.page_2_contents.addWidget(self.p2_svg_astro_frame)

        self.p2_label_conn_status = QLabel(self.page_2_frame)
        self.p2_label_conn_status.setObjectName(u"p2_label_conn_status")
        self.p2_label_conn_status.setMinimumSize(QSize(0, 20))
        self.p2_label_conn_status.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(10)
        self.p2_label_conn_status.setFont(font)
        self.p2_label_conn_status.setAlignment(Qt.AlignCenter)

        self.page_2_contents.addWidget(self.p2_label_conn_status)

        self.p2_icon_conn_status_frame = QFrame(self.page_2_frame)
        self.p2_icon_conn_status_frame.setObjectName(u"p2_icon_conn_status_frame")
        self.p2_icon_conn_status_frame.setMinimumSize(QSize(0, 100))
        self.p2_icon_conn_status_frame.setMaximumSize(QSize(16777215, 100))
        self.p2_icon_conn_status_frame.setFrameShape(QFrame.NoFrame)
        self.p2_icon_conn_status_frame.setFrameShadow(QFrame.Raised)
        self.p2_icon_conn_status_layout = QVBoxLayout(self.p2_icon_conn_status_frame)
        self.p2_icon_conn_status_layout.setSpacing(0)
        self.p2_icon_conn_status_layout.setObjectName(u"p2_icon_conn_status_layout")
        self.p2_icon_conn_status_layout.setContentsMargins(0, 0, 0, 0)

        self.page_2_contents.addWidget(self.p2_icon_conn_status_frame)

        self.p2_toggle_conn_frame = QFrame(self.page_2_frame)
        self.p2_toggle_conn_frame.setObjectName(u"p2_toggle_conn_frame")
        self.p2_toggle_conn_frame.setMinimumSize(QSize(0, 100))
        self.p2_toggle_conn_frame.setMaximumSize(QSize(16777215, 100))
        self.p2_toggle_conn_frame.setFrameShape(QFrame.NoFrame)
        self.p2_toggle_conn_frame.setFrameShadow(QFrame.Raised)
        self.p2_toggle_conn_layout = QVBoxLayout(self.p2_toggle_conn_frame)
        self.p2_toggle_conn_layout.setSpacing(0)
        self.p2_toggle_conn_layout.setObjectName(u"p2_toggle_conn_layout")
        self.p2_toggle_conn_layout.setContentsMargins(0, 0, 0, 0)

        self.page_2_contents.addWidget(self.p2_toggle_conn_frame)


        self.verticalLayout_3.addLayout(self.page_2_contents)


        self.page_2_layout.addWidget(self.page_2_frame)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        font1 = QFont()
        font1.setPointSize(16)
        self.empty_page_label.setFont(font1)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4_layout = QVBoxLayout(self.page_4)
        self.page_4_layout.setSpacing(5)
        self.page_4_layout.setObjectName(u"page_4_layout")
        self.page_4_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_4)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_4_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_5_layout = QVBoxLayout(self.page_5)
        self.page_5_layout.setObjectName(u"page_5_layout")
        self.empty_page_label1 = QLabel(self.page_5)
        self.empty_page_label1.setObjectName(u"empty_page_label1")
        self.empty_page_label1.setFont(font1)
        self.empty_page_label1.setAlignment(Qt.AlignCenter)

        self.page_5_layout.addWidget(self.empty_page_label1)

        self.pages.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_6_layout = QVBoxLayout(self.page_6)
        self.page_6_layout.setObjectName(u"page_6_layout")
        self.empty_page_label2 = QLabel(self.page_6)
        self.empty_page_label2.setObjectName(u"empty_page_label2")
        self.empty_page_label2.setFont(font1)
        self.empty_page_label2.setAlignment(Qt.AlignCenter)

        self.page_6_layout.addWidget(self.empty_page_label2)

        self.pages.addWidget(self.page_6)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome to Flylapse", None))
        self.p2_label_conn_status.setText(QCoreApplication.translate("MainPages", u"Disconnected", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.empty_page_label1.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
        self.empty_page_label2.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi

