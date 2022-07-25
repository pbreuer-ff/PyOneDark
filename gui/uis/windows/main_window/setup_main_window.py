# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

# IMPORT APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
from program import *

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////


class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "leftmenu_btn_page_1",
            "btn_text": "Start",
            "btn_tooltip": "Start",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_connect.svg",
            "btn_id": "leftmenu_btn_page_2",
            "btn_text": "Connect",
            "btn_tooltip": "Connect",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_film.svg",
            "btn_id": "leftmenu_btn_page_3",
            "btn_text": "Plan",
            "btn_tooltip": "Plan",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_path.svg",
            "btn_id": "leftmenu_btn_page_4",
            "btn_text": "Edit",
            "btn_tooltip": "Edit",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_play_menu.svg",
            "btn_id": "leftmenu_btn_page_5",
            "btn_text": "Fly",
            "btn_tooltip": "Fly",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_save.svg",
            "btn_id": "leftmenu_btn_page_6",
            "btn_text": "Review",
            "btn_tooltip": "Review",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "leftmenu_btn_settings",
            "btn_text": "Settings",
            "btn_tooltip": "Open settings",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "leftmenu_btn_help",
            "btn_text": "Help",
            "btn_tooltip": "Help",
            "show_top": False,
            "is_active": False
        }

    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_monitoring.svg",
            "btn_id": "titlemenu_btn_monitor",
            "btn_tooltip": "Monitor",
            "is_active": False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(
                self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(
                self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD TITLE
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Flylapse")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        self.ui.active_page = 1

        # TODO make dep on active page
        """ MainFunctions.set_left_col_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_col_menu(self, self.ui.right_column.menu_1) """

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ///////////////////////////////////////////////////////////////
        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # BTN 2
        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # BTN 3 - Default QPushButton
        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # ///////////////////////////////////////////////////////////////
        # PAGES
        # ///////////////////////////////////////////////////////////////

        # PAGE 1
        # ///////////////////////////////////////////////////////////////

        # SVG: FF LOGO
        file = Functions.set_svg_image("freefly_logo.svg")
        size = QSvgRenderer(file)
        self.p1_svg_logo = QSvgWidget(file)
        self.p1_svg_logo.setFixedSize(size.defaultSize())

        self.ui.load_pages.p1_svg_logo_layout.addWidget(
            self.p1_svg_logo)

        # LABEL: WELCOME
        self.p1_label_welcome = QLabel()
        self.p1_label_welcome.setText('Welcome to Flylapse')
        self.p1_label_welcome.setStyleSheet("font-size: 20pt;")

        self.ui.load_pages.p1_label_welcome_layout.addWidget(
            self.p1_label_welcome)

        # BUTTON: START CONNECTION
        self.p1_btn_start_conn = PyPushButton(
            text="Start Connection",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.p1_btn_start_conn.setMinimumHeight(40)

        self.ui.load_pages.p1_btn_start_conn_layout.addWidget(
            self.p1_btn_start_conn, Qt.AlignCenter, Qt.AlignTop)

        # PAGE 2
        # ///////////////////////////////////////////////////////////////

        # SVG
        file = Functions.set_svg_image("astro_side_on.svg")
        size = QSvgRenderer(file)
        self.p2_svg_astro = QSvgWidget(file)
        self.p2_svg_astro.setFixedSize(size.defaultSize())

        self.ui.load_pages.p2_svg_astro_layout.addWidget(
            self.p2_svg_astro)

        # LABEL
        self.p2_label_conn_status = QLabel()
        self.p2_label_conn_status.setText('Connected')
        self.p2_label_conn_status.setStyleSheet("font-size: 16pt;")

        self.ui.load_pages.p2_label_conn_status_layout.addWidget(
            self.p2_label_conn_status)

        # TOGGLE
        self.p2_toggle_conn = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"],
        )
        self.p2_toggle_conn.setChecked(True)

        self.ui.load_pages.p2_toggle_conn_layout.addWidget(
            self.p2_toggle_conn)

        # PAGE 3
        # ///////////////////////////////////////////////////////////////

        # LABEL: KF NO
        self.p3_label_capture = QLabel()
        self.p3_label_capture.setStyleSheet("font-size: 20pt;")
        self.p3_label_capture.setText('Capture Keyframe X')

        self.ui.load_pages.p3_label_capture_layout.addWidget(
            self.p3_label_capture)

        # LABEL: TARGET TIME
        self.p3_label_time = QLabel()
        self.p3_label_time.setStyleSheet("font-size: 16pt;")
        self.p3_label_time.setText('Target Time:')

        self.ui.load_pages.p3_label_time_layout.addWidget(self.p3_label_time)

        # LABEL: TIME
        self.p3_label_time_value = QLabel()
        self.p3_label_time_value.setStyleSheet("font-size: 12pt;")
        self.p3_label_time_value.setText('XX')

        self.ui.load_pages.p3_label_time_value_layout.addWidget(
            self.p3_label_time_value)

        # LABEL: TIME VALUE
        self.p3_label_time_value_min = QLabel()
        self.p3_label_time_value_min.setStyleSheet("font-size: 12pt;")
        self.p3_label_time_value_min.setText('min.')

        self.ui.load_pages.p3_label_time_value_layout.addWidget(
            self.p3_label_time_value_min)

        # SLIDER
        self.p3_slider_time = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.p3_slider_time.setOrientation(Qt.Horizontal)
        self.p3_slider_time.setMinimumWidth(200)
        self.p3_slider_time.setMaximumWidth(300)

        self.ui.load_pages.p3_slider_time_layout.addWidget(
            self.p3_slider_time)

        # BUTTON
        self.p3_btn_capture = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_add.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Capture Keyframe",
            width=100,
            height=100,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )

        self.ui.load_pages.p3_btn_capture_layout.addWidget(
            self.p3_btn_capture)

        # TABLE
        self.p3_table_keyframes = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.p3_table_keyframes.setColumnCount(8)
        self.p3_table_keyframes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.p3_table_keyframes.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        self.p3_table_keyframes.setSelectionBehavior(
            QAbstractItemView.SelectRows)

        # COLUMN HEADERS
        self.p3_table_keyframes_col_1 = QTableWidgetItem()
        self.p3_table_keyframes_col_1.setTextAlignment(Qt.AlignCenter)
        self.p3_table_keyframes_col_1.setText("Time [s]")

        self.p3_table_keyframes_col_2 = QTableWidgetItem()
        self.p3_table_keyframes_col_2.setTextAlignment(Qt.AlignCenter)
        self.p3_table_keyframes_col_2.setText("North [m]")

        self.p3_table_keyframes_col_3 = QTableWidgetItem()
        self.p3_table_keyframes_col_3.setTextAlignment(Qt.AlignCenter)
        self.p3_table_keyframes_col_3.setText("East [m]")

        self.p3_table_keyframes_col_4 = QTableWidgetItem()
        self.p3_table_keyframes_col_4.setTextAlignment(Qt.AlignCenter)
        self.p3_table_keyframes_col_4.setText("Relalt [m]")

        self.p3_table_keyframes_col_5 = QTableWidgetItem()
        self.p3_table_keyframes_col_5.setTextAlignment(Qt.AlignCenter)
        self.p3_table_keyframes_col_5.setText("Pan [deg]")

        self.p3_table_keyframes_col_6 = QTableWidgetItem()
        self.p3_table_keyframes_col_6.setTextAlignment(Qt.AlignCenter)
        self.p3_table_keyframes_col_6.setText("Tilt [deg]")

        self.p3_table_keyframes_col_7 = QTableWidgetItem()
        self.p3_table_keyframes_col_7.setTextAlignment(Qt.AlignCenter)
        self.p3_table_keyframes_col_7.setText("Ease In")

        self.p3_table_keyframes_col_8 = QTableWidgetItem()
        self.p3_table_keyframes_col_8.setTextAlignment(Qt.AlignCenter)
        self.p3_table_keyframes_col_8.setText("Ease Out")

        # SET COLUMN
        self.p3_table_keyframes.setHorizontalHeaderItem(
            0, self.p3_table_keyframes_col_1)
        self.p3_table_keyframes.setHorizontalHeaderItem(
            1, self.p3_table_keyframes_col_2)
        self.p3_table_keyframes.setHorizontalHeaderItem(
            2, self.p3_table_keyframes_col_3)
        self.p3_table_keyframes.setHorizontalHeaderItem(
            3, self.p3_table_keyframes_col_4)
        self.p3_table_keyframes.setHorizontalHeaderItem(
            4, self.p3_table_keyframes_col_5)
        self.p3_table_keyframes.setHorizontalHeaderItem(
            5, self.p3_table_keyframes_col_6)
        self.p3_table_keyframes.setHorizontalHeaderItem(
            6, self.p3_table_keyframes_col_7)
        self.p3_table_keyframes.setHorizontalHeaderItem(
            7, self.p3_table_keyframes_col_8)

        for row in range(9):
            temp = row

            # insert row after previous one
            row_number = self.p3_table_keyframes.rowCount()
            self.p3_table_keyframes.insertRow(row_number)

            # TODO: should the vars below be members?

            # Time [s]
            time = QTableWidgetItem()
            time.setTextAlignment(Qt.AlignCenter)
            time.setText(str(temp + 1))
            self.p3_table_keyframes.setItem(row_number, 0, time)

            # North [m]
            north = QTableWidgetItem()
            north.setTextAlignment(Qt.AlignCenter)
            north.setText(str(temp + 2))
            self.p3_table_keyframes.setItem(row_number, 1, north)

            # East [m]
            east = QTableWidgetItem()
            east.setTextAlignment(Qt.AlignCenter)
            east.setText(str(temp + 3))
            self.p3_table_keyframes.setItem(row_number, 2, east)

            # Relalt [m]
            relalt = QTableWidgetItem()
            relalt.setTextAlignment(Qt.AlignCenter)
            relalt.setText(str(temp + 4))
            self.p3_table_keyframes.setItem(row_number, 3, relalt)

            # Pan [deg]
            pan = QTableWidgetItem()
            pan.setTextAlignment(Qt.AlignCenter)
            pan.setText(str(temp + 5))
            self.p3_table_keyframes.setItem(row_number, 4, pan)

            # Tilt [deg]
            tilt = QTableWidgetItem()
            tilt.setTextAlignment(Qt.AlignCenter)
            tilt.setText(str(temp + 6))
            self.p3_table_keyframes.setItem(row_number, 5, tilt)

            # Ease In
            easein = QTableWidgetItem()
            easein.setTextAlignment(Qt.AlignCenter)
            easein.setText("Yes")
            self.p3_table_keyframes.setItem(row_number, 6, easein)

            # Ease Out
            easeout = QTableWidgetItem()
            easeout.setTextAlignment(Qt.AlignCenter)
            easeout.setText("Yes")
            self.p3_table_keyframes.setItem(row_number, 7, easeout)

        self.ui.load_pages.p3_table_keyframes_layout.addWidget(
            self.p3_table_keyframes)

        # LABEL: START POS
        self.p3_label_home_pos = QLabel()
        self.p3_label_home_pos.setText('Start Position')

        self.ui.load_pages.p3_label_home_pos_layout.addWidget(
            self.p3_label_home_pos)

        # LABEL: START POS LAT
        self.p3_label_home_pos_lat = QLabel()
        self.p3_label_home_pos_lat.setText('Latitude [deg]')

        self.ui.load_pages.p3_label_home_pos_lat_layout.addWidget(
            self.p3_label_home_pos_lat)

        # LABEL: START POS LAT VALUE
        self.p3_label_home_pos_lat_value = QLabel()
        self.p3_label_home_pos_lat_value.setText('XXXX')

        self.ui.load_pages.p3_label_home_pos_lat_layout.addWidget(
            self.p3_label_home_pos_lat_value)

        # LABEL: START POS LONG
        self.p3_label_home_pos_long = QLabel()
        self.p3_label_home_pos_long.setText('Longitude [deg]')

        self.ui.load_pages.p3_label_home_pos_long_layout.addWidget(
            self.p3_label_home_pos_long)

        # LABEL: START POS LONG VALUE
        self.p3_label_home_pos_long_value = QLabel()
        self.p3_label_home_pos_long_value.setText('XXXX')

        self.ui.load_pages.p3_label_home_pos_long_layout.addWidget(
            self.p3_label_home_pos_long_value)

        # LABEL: START POS ALT
        self.p3_label_home_pos_alt = QLabel()
        self.p3_label_home_pos_alt.setText('Altitude [m]')

        self.ui.load_pages.p3_label_home_pos_alt_layout.addWidget(
            self.p3_label_home_pos_alt)

        # LABEL: START POS ALT VALUE
        self.p3_label_home_pos_alt_value = QLabel()
        self.p3_label_home_pos_alt_value.setText('XXXX')

        self.ui.load_pages.p3_label_home_pos_alt_layout.addWidget(
            self.p3_label_home_pos_alt_value)

        # BUTTON
        self.p3_btn_upload = PyPushButton(
            text="Upload...",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.p3_btn_upload.setMinimumHeight(40)

        self.ui.load_pages.p3_btn_upload_layout.addWidget(
            self.p3_btn_upload)

        # PAGE 4
        # ///////////////////////////////////////////////////////////////

        # LABEL: POSITION
        self.p4_label_pos_graph = QLabel()
        self.p4_label_pos_graph.setText('Position')

        self.ui.load_pages.p4_label_pos_graph_layout.addWidget(
            self.p4_label_pos_graph)

        # BUTTON: NORTH
        self.p4_btns_pos_north_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_n.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="North",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_pos_graph_layout.addWidget(
            self.p4_btns_pos_north_graph)

        # BUTTON: EAST
        self.p4_btns_pos_east_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_e.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="East",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_pos_graph_layout.addWidget(
            self.p4_btns_pos_east_graph)

        # BUTTON: RELALT
        self.p4_btns_pos_relalt_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_altitude.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Altitude",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_pos_graph_layout.addWidget(
            self.p4_btns_pos_relalt_graph)

        # ///////////////////////////////////////////////////////////////

        # LABEL: VELOCITY
        self.p4_label_vel_graph = QLabel()
        self.p4_label_vel_graph.setText('Velocity')

        self.ui.load_pages.p4_label_vel_graph_layout.addWidget(
            self.p4_label_vel_graph)

        # BUTTON: NORTH
        self.p4_btns_vel_north_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_n.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="North",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_vel_graph_layout.addWidget(
            self.p4_btns_vel_north_graph)

        # BUTTON: EAST
        self.p4_btns_vel_east_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_e.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="East",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_vel_graph_layout.addWidget(
            self.p4_btns_vel_east_graph)

        # BUTTON: RELALT
        self.p4_btns_vel_relalt_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_altitude.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Altitude",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_vel_graph_layout.addWidget(
            self.p4_btns_vel_relalt_graph)

        # ///////////////////////////////////////////////////////////////

        # LABEL: ACCELERATION
        self.p4_label_accel_graph = QLabel()
        self.p4_label_accel_graph.setText('Acceleration')

        self.ui.load_pages.p4_label_accel_graph_layout.addWidget(
            self.p4_label_accel_graph)

        # BUTTON: NORTH
        self.p4_btns_accel_north_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_n.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="North",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_accel_graph_layout.addWidget(
            self.p4_btns_accel_north_graph)

        # BUTTON: EAST
        self.p4_btns_accel_east_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_e.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="East",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_accel_graph_layout.addWidget(
            self.p4_btns_accel_east_graph)

        # BUTTON: RELALT
        self.p4_btns_accel_relalt_graph = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_altitude.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Altitude",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_accel_graph_layout.addWidget(
            self.p4_btns_accel_relalt_graph)

        # ///////////////////////////////////////////////////////////////

        # LABEL: PREVIEW
        self.p4_label_prev = QLabel()
        self.p4_label_prev.setText('Preview')
        self.p4_label_prev.setStyleSheet("font-size: 20pt;")

        self.ui.load_pages.p4_prev_layout.addWidget(self.p4_label_prev)

        # BUTTON: REFRESH
        self.p4_btn_refresh = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_refresh.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Refresh",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )
        self.ui.load_pages.p4_prev_layout.addWidget(
            self.p4_btn_refresh)

        # GRAPH: PREVIEW
        self.p4_graph_prev = pg.PlotWidget()
        self.p4_graph_prev.setBackground(background=None)  # transparent
        pen = pg.mkPen(color=(255, 255, 255))  # white
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.p4_graph_prev.plot(time, values, pen=pen)
        self.p4_graph_prev.plot([3], [34], pen=pen, symbol='o', symbolSize=10, symbolBrush=(
            self.themes["app_color"]["dark_one"]))
        self.p4_graph_prev.setLabel('left', 'North [m]')
        self.p4_graph_prev.setLabel('bottom', 'East [m]')

        self.ui.load_pages.p4_graph_layout.addWidget(
            self.p4_graph_prev)

        # ///////////////////////////////////////////////////////////////

        # BUTTON: FIRST KF
        self.p4_btns_prev_first_kf = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_first.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="First",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )
        self.ui.load_pages.p4_btns_prev_layout.addWidget(
            self.p4_btns_prev_first_kf)

        # BUTTON: PREVIOUS KF
        self.p4_btns_prev_prev_kf = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_prev.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Previous",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )
        self.ui.load_pages.p4_btns_prev_layout.addWidget(
            self.p4_btns_prev_prev_kf)

        # BUTTON: NEXT KF
        self.p4_btns_prev_next_kf = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_next.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Next",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )
        self.ui.load_pages.p4_btns_prev_layout.addWidget(
            self.p4_btns_prev_next_kf)

        # BUTTON: LAST KF
        self.p4_btns_prev_last_kf = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_last.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Last",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )
        self.ui.load_pages.p4_btns_prev_layout.addWidget(
            self.p4_btns_prev_last_kf)

        # ///////////////////////////////////////////////////////////////

        # BUTTON: 2D
        self.p4_btns_2d3d_2d = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_2d.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="2D",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=True
        )

        self.ui.load_pages.p4_btns_2d3d_layout.addWidget(
            self.p4_btns_2d3d_2d)

        # BUTTON: 3D
        self.p4_btns_2d3d_3d = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_3d.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="3D",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_2d3d_layout.addWidget(
            self.p4_btns_2d3d_3d)

        # ///////////////////////////////////////////////////////////////

        # BUTTON: PAN
        self.p4_btns_pantilt_pan = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_pan.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Pan",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_pantilt_layout.addWidget(
            self.p4_btns_pantilt_pan)

        # BUTTON: TILT
        self.p4_btns_pantilt_tilt = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_tilt.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Tilt",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_btns_pantilt_layout.addWidget(
            self.p4_btns_pantilt_tilt)

    # ///////////////////////////////////////////////////////////////

        # LABEL: EDIT
        self.p4_label_edit = QLabel()
        self.p4_label_edit.setText('Edit')
        self.p4_label_edit.setStyleSheet("font-size: 20pt;")

        self.ui.load_pages.p4_edit_layout.addWidget(self.p4_label_edit)

        # BUTTON: SAVE
        self.p4_btn_save = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_save.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Save Changes",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )
        self.ui.load_pages.p4_edit_layout.addWidget(self.p4_btn_save)

        # ///////////////////////////////////////////////////////////////

        # LABEL: KEYFRAME
        self.p4_label_keyframe = QLabel()
        self.p4_label_keyframe.setText('Keyframe')
        self.p4_label_keyframe.setStyleSheet("font-size: 16pt;")

        self.ui.load_pages.p4_label_keyframe_layout.addWidget(
            self.p4_label_keyframe)

        # LABEL: KEYFRAME VALUE
        self.p4_label_keyframe_value = QLabel()
        self.p4_label_keyframe_value.setText('XX')
        self.p4_label_keyframe_value.setStyleSheet("font-size: 14pt;")

        self.ui.load_pages.p4_label_keyframe_layout.addWidget(
            self.p4_label_keyframe_value)

        # ///////////////////////////////////////////////////////////////

        # LABEL: EASE IN
        self.p4_label_easein = QLabel()
        self.p4_label_easein.setText('Ease In')

        self.ui.load_pages.p4_easein_layout.addWidget(self.p4_label_easein)

        # BUTTON: NO EASE IN
        self.p4_btn_easein_deact = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_noease.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="No Ease",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=True
        )

        self.ui.load_pages.p4_easein_layout.addWidget(
            self.p4_btn_easein_deact)

        # BUTTON: EASE IN
        self.p4_btn_easein_activ = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_easein.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Ease In",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_easein_layout.addWidget(
            self.p4_btn_easein_activ)

        # ///////////////////////////////////////////////////////////////

        # LABEL: EASE OUT
        self.p4_label_easeout = QLabel()
        self.p4_label_easeout.setText('Ease Out')

        self.ui.load_pages.p4_easeout_layout.addWidget(
            self.p4_label_easeout)

        # BUTTON: NO EASE OUT
        self.p4_btn_easeout_deact = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_noease.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="No Ease",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=True
        )

        self.ui.load_pages.p4_easeout_layout.addWidget(
            self.p4_btn_easeout_deact)

        # BUTTON: EASE OUT
        self.p4_btn_easeout_activ = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_easeout.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Ease Out",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )

        self.ui.load_pages.p4_easeout_layout.addWidget(
            self.p4_btn_easeout_activ)

        # ///////////////////////////////////////////////////////////////

        # LABEL: POSITION
        self.p4_label_position = QLabel()
        self.p4_label_position.setText('Position [m]')

        self.ui.load_pages.p4_label_position_layout.addWidget(
            self.p4_label_position)

        # TODO: fix sep lines, make sliders from lineedits N SLIDER VALUE

        # LINEEDIT: NORTH
        self.p4_lineedit_pos_north = PyLineEdit(
            text="XXX",
            place_holder_text="0",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )

        self.p4_lineedit_pos_north.setMinimumHeight(30)
        self.p4_lineedit_pos_north.setMinimumWidth(60)
        self.p4_lineedit_pos_north.setMaximumWidth(60)

        self.ui.load_pages.p4_lineedit_pos_n_layout.addWidget(
            self.p4_lineedit_pos_north)

        # LABEL: NORTH
        self.p4_label_pos_north = QLabel()
        self.p4_label_pos_north.setText('N')

        self.ui.load_pages.p4_lineedit_pos_n_layout.addWidget(
            self.p4_label_pos_north)

        # LINEEDIT: EAST
        self.p4_lineedit_pos_east = PyLineEdit(
            text="XXX",
            place_holder_text="0",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )

        self.p4_lineedit_pos_east.setMinimumHeight(30)
        self.p4_lineedit_pos_east.setMinimumWidth(60)
        self.p4_lineedit_pos_east.setMaximumWidth(60)

        self.ui.load_pages.p4_lineedit_pos_e_layout.addWidget(
            self.p4_lineedit_pos_east)

        # LABEL: EAST
        self.p4_label_pos_east = QLabel()
        self.p4_label_pos_east.setText('E')

        self.ui.load_pages.p4_lineedit_pos_e_layout.addWidget(
            self.p4_label_pos_east)

        # LINEEDIT: RELALT
        self.p4_lineedit_pos_relalt = PyLineEdit(
            text="XXX",
            place_holder_text="0",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )

        self.p4_lineedit_pos_relalt.setMinimumHeight(30)
        self.p4_lineedit_pos_relalt.setMinimumWidth(60)
        self.p4_lineedit_pos_relalt.setMaximumWidth(60)

        self.ui.load_pages.p4_lineedit_pos_relalt_layout.addWidget(
            self.p4_lineedit_pos_relalt)

        # LABEL: RELALT
        self.p4_label_pos_relalt = QLabel()
        self.p4_label_pos_relalt.setText('Alt')

        self.ui.load_pages.p4_lineedit_pos_relalt_layout.addWidget(
            self.p4_label_pos_relalt)

        # ///////////////////////////////////////////////////////////////

        # LABEL: ORIENTATION
        self.p4_label_orientation = QLabel()
        self.p4_label_orientation.setText('Orientation [deg]')

        self.ui.load_pages.p4_label_orientation_layout.addWidget(
            self.p4_label_orientation)

        # LINEEDIT: PAN
        self.p4_lineedit_orientation_pan = PyLineEdit(
            text="XXX",
            place_holder_text="enter",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )

        self.p4_lineedit_orientation_pan.setMinimumHeight(30)
        self.p4_lineedit_orientation_pan.setMinimumWidth(60)
        self.p4_lineedit_orientation_pan.setMaximumWidth(60)

        self.ui.load_pages.p4_lineedit_orientation_pan_layout.addWidget(
            self.p4_lineedit_orientation_pan)

        # LABEL: PAN
        self.p4_label_orientation_pan = QLabel()
        self.p4_label_orientation_pan.setText('Pan')

        self.ui.load_pages.p4_lineedit_orientation_pan_layout.addWidget(
            self.p4_label_orientation_pan)

        # LINEEDIT: TILT
        self.p4_lineedit_orientation_tilt = PyLineEdit(
            text="XXX",
            place_holder_text="enter",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )

        self.p4_lineedit_orientation_tilt.setMinimumHeight(30)
        self.p4_lineedit_orientation_tilt.setMinimumWidth(60)
        self.p4_lineedit_orientation_tilt.setMaximumWidth(60)

        self.ui.load_pages.p4_lineedit_orientation_tilt_layout.addWidget(
            self.p4_lineedit_orientation_tilt)

        # LABEL: TILT
        self.p4_label_orientation_tilt = QLabel()
        self.p4_label_orientation_tilt.setText('Tilt')

        self.ui.load_pages.p4_lineedit_orientation_tilt_layout.addWidget(
            self.p4_label_orientation_tilt)

        # ///////////////////////////////////////////////////////////////

        # LABEL: TIME
        self.p4_label_time = QLabel()
        self.p4_label_time.setStyleSheet("font-size: 10pt;")
        self.p4_label_time.setText('Time [min]')

        self.ui.load_pages.p4_time_layout.addWidget(self.p4_label_time)

        # LABEL: TIME VALUE
        self.p4_label_time_value = QLabel()
        self.p4_label_time_value.setText('XX')

        self.ui.load_pages.p4_time_layout.addWidget(self.p4_label_time_value)

        # SLIDER: TIME
        self.p4_slider_time = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.p4_slider_time.setOrientation(Qt.Horizontal)

        self.ui.load_pages.p4_time_layout.addWidget(self.p4_slider_time)

        # ///////////////////////////////////////////////////////////////

        # BUTTON: EXPORT
        self.p4_btn_export = PyPushButton(
            text="Export...",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.p4_btn_export.setMinimumHeight(40)

        self.ui.load_pages.p4_bottom_layout.addWidget(
            self.p4_btn_export)

        # PAGE 5
        # ///////////////////////////////////////////////////////////////

        # CIRCULAR PROGRESS
        self.p5_progress = PyCircularProgress(
            value=80,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["text_title"],
            font_size=14,
            bg_color=self.themes["app_color"]["dark_four"]
        )
        self.p5_progress.setFixedSize(200, 200)

        self.ui.load_pages.p5_progress_layout.addWidget(
            self.p5_progress)

        # ///////////////////////////////////////////////////////////////

        # LABEL: TIME REMAINING
        self.p5_label_time = QLabel()
        self.p5_label_time.setText('Remaining:')
        self.p5_label_time.setStyleSheet("font-size: 12pt;")

        self.ui.load_pages.p5_label_time_rem_layout.addWidget(
            self.p5_label_time)

        # LABEL: TIME REMAINING VALUE
        self.p5_label_time_value = QLabel()
        self.p5_label_time_value.setText('XX:XX')
        self.p5_label_time_value.setStyleSheet("font-size: 12pt;")

        self.ui.load_pages.p5_label_time_rem_layout.addWidget(
            self.p5_label_time_value)

        # ///////////////////////////////////////////////////////////////

        # BUTTON: START PAUSE/CONTINUE
        self.p4_btns_control_startpauseresume = PyIconButton(
            # icon_stop.svg, icon_resume.svg
            icon_path=Functions.set_svg_icon("icon_play.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Start",  # Pause, Resume
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )
        self.ui.load_pages.p5_btns_control_layout.addWidget(
            self.p4_btns_control_startpauseresume)

        # BUTTON: STOP
        self.p4_btns_control_stop = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_stop.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Stop",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )
        self.ui.load_pages.p5_btns_control_layout.addWidget(
            self.p4_btns_control_stop)

        # ///////////////////////////////////////////////////////////////

        # LABEL: MONITOR
        self.p5_label_monitor = QLabel()
        self.p5_label_monitor.setText('Monitor')
        self.p5_label_monitor.setStyleSheet("font-size: 20pt;")

        self.ui.load_pages.p5_label_monitor_layout.addWidget(
            self.p5_label_monitor)

        # ///////////////////////////////////////////////////////////////

        # GRAPH: 2D
        self.p5_graphs_2d = pg.PlotWidget()
        self.p5_graphs_2d.setBackground(background=None)  # transparent
        pen = pg.mkPen(color=(255, 255, 255))  # white
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.p5_graphs_2d.plot(time, values, pen=pen)
        self.p5_graphs_2d.setTitle("2D Position")
        self.p5_graphs_2d.setLabel('left', 'North [m]')
        self.p5_graphs_2d.setLabel('bottom', 'East [m]')

        self.ui.load_pages.p5_graphs_layout.addWidget(
            self.p5_graphs_2d)

        # GRAPH: RELALT
        self.p5_graphs_relalt = pg.PlotWidget()
        self.p5_graphs_relalt.setBackground(background=None)  # transparent
        pen = pg.mkPen(color=(255, 255, 255))  # white
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.p5_graphs_relalt.plot(time, values, pen=pen)
        self.p5_graphs_relalt.setTitle("Rel. Altitude")
        self.p5_graphs_relalt.setLabel('left', 'Rel. Altitude [m]')
        self.p5_graphs_relalt.setLabel('bottom', 'Time [s]')

        self.ui.load_pages.p5_graphs_layout.addWidget(
            self.p5_graphs_relalt)

        # ///////////////////////////////////////////////////////////////

        # BUTTON: EXPORT LOG
        self.p5_btn_export = PyPushButton(
            text="Export Log...",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.p5_btn_export.setMinimumHeight(40)

        self.ui.load_pages.p5_bottom_layout.addWidget(
            self.p5_btn_export)

        # PAGE 6
        # ///////////////////////////////////////////////////////////////

        # BUTTON: IMPORT LOG
        self.p6_btn_import = PyPushButton(
            text="Import Log...",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.p6_btn_import.setMinimumHeight(40)

        self.ui.load_pages.p6_btn_import_layout.addWidget(
            self.p6_btn_import)

        # ///////////////////////////////////////////////////////////////

        # LABEL: REVIEWING FILE
        self.p6_label_review_file = QLabel()
        self.p6_label_review_file.setText('Review')
        self.p6_label_review_file.setStyleSheet("font-size: 20pt;")

        self.ui.load_pages.p6_label_review_layout.addWidget(
            self.p6_label_review_file)

        # LABEL: LOG
        self.p6_label_review_file_name_prefix = QLabel()
        self.p6_label_review_file_name_prefix.setText('Log')
        self.p6_label_review_file_name_prefix.setStyleSheet("font-size: 12pt;")

        self.ui.load_pages.p6_label_review_file_layout.addWidget(
            self.p6_label_review_file_name_prefix)
        
        # LABEL: FILENAME
        self.p6_label_review_file_name = QLabel()
        self.p6_label_review_file_name.setText('XX.csv')
        self.p6_label_review_file_name.setStyleSheet("font-size: 12pt;")

        self.ui.load_pages.p6_label_review_file_layout.addWidget(
            self.p6_label_review_file_name)

        # ///////////////////////////////////////////////////////////////

        # GRAPH: PREVIEW
        self.p6_graph = pg.PlotWidget()
        self.p6_graph.setBackground(background=None)  # transparent
        pen = pg.mkPen(color=(255, 255, 255))  # white
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.p6_graph.plot(time, values, pen=pen)
        self.p6_graph.plot(time, values, pen=pen, symbol='o', symbolSize=10, symbolBrush=(
            self.themes["app_color"]["dark_one"]))
        self.p6_graph.setLabel('left', 'North [m]')
        self.p6_graph.setLabel('bottom', 'East [m]')

        self.ui.load_pages.p6_graph_layout.addWidget(
            self.p6_graph)

        # ///////////////////////////////////////////////////////////////

        # LABEL: RAW DATA
        self.p6_label_table = QLabel()
        self.p6_label_table.setText('Raw Data')
        self.p6_label_table.setStyleSheet("font-size: 12pt;")

        self.ui.load_pages.p6_label_table_layout.addWidget(self.p6_label_table)

        # ///////////////////////////////////////////////////////////////

        # TABLE
        self.p6_table = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.p6_table.setColumnCount(34)
        self.p6_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.p6_table.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        self.p6_table.setSelectionBehavior(
            QAbstractItemView.SelectRows)

        # COLUMN HEADERS
        self.p6_table_col_1 = QTableWidgetItem()
        self.p6_table_col_1.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_1.setText("current_kf_id")

        self.p6_table_col_2 = QTableWidgetItem()
        self.p6_table_col_2.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_2.setText("current_kf_time")

        self.p6_table_col_3 = QTableWidgetItem()
        self.p6_table_col_3.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_3.setText("time")

        self.p6_table_col_4 = QTableWidgetItem()
        self.p6_table_col_4.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_4.setText("param")

        self.p6_table_col_5 = QTableWidgetItem()
        self.p6_table_col_5.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_5.setText("north_m_sp")

        self.p6_table_col_6 = QTableWidgetItem()
        self.p6_table_col_6.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_6.setText("north_m")

        self.p6_table_col_7 = QTableWidgetItem()
        self.p6_table_col_7.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_7.setText("north_m_s_sp")

        self.p6_table_col_8 = QTableWidgetItem()
        self.p6_table_col_8.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_8.setText("north_m_s")

        self.p6_table_col_9 = QTableWidgetItem()
        self.p6_table_col_9.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_9.setText("north_m_s_cmd")

        self.p6_table_col_10 = QTableWidgetItem()
        self.p6_table_col_10.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_10.setText("north_m_s2_sp")

        self.p6_table_col_11 = QTableWidgetItem()
        self.p6_table_col_11.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_11.setText("east_m_sp")

        self.p6_table_col_12 = QTableWidgetItem()
        self.p6_table_col_12.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_12.setText("east_m_s_sp")

        self.p6_table_col_13 = QTableWidgetItem()
        self.p6_table_col_13.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_13.setText("east_m_s")

        self.p6_table_col_14 = QTableWidgetItem()
        self.p6_table_col_14.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_14.setText("east_m_s_cmd")

        self.p6_table_col_15 = QTableWidgetItem()
        self.p6_table_col_15.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_15.setText("east_m_s2_sp")

        self.p6_table_col_16 = QTableWidgetItem()
        self.p6_table_col_16.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_16.setText("down_m_sp")

        self.p6_table_col_17 = QTableWidgetItem()
        self.p6_table_col_17.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_17.setText("down_m")

        self.p6_table_col_18 = QTableWidgetItem()
        self.p6_table_col_18.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_18.setText("down_m_s_sp")

        self.p6_table_col_19 = QTableWidgetItem()
        self.p6_table_col_19.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_19.setText("down_m_s")

        self.p6_table_col_20 = QTableWidgetItem()
        self.p6_table_col_20.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_20.setText("down_m_s_cmd")

        self.p6_table_col_21 = QTableWidgetItem()
        self.p6_table_col_21.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_21.setText("down_m_s2_sp")

        self.p6_table_col_22 = QTableWidgetItem()
        self.p6_table_col_22.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_22.setText("yaw_deg")

        self.p6_table_col_23 = QTableWidgetItem()
        self.p6_table_col_23.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_23.setText("yaw_deg_cmd")

        self.p6_table_col_24 = QTableWidgetItem()
        self.p6_table_col_24.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_24.setText("lat_deg")

        self.p6_table_col_25 = QTableWidgetItem()
        self.p6_table_col_25.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_25.setText("long_deg")

        self.p6_table_col_26 = QTableWidgetItem()
        self.p6_table_col_26.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_26.setText("relalt_m")

        self.p6_table_col_27 = QTableWidgetItem()
        self.p6_table_col_27.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_27.setText("pan_deg_sp")

        self.p6_table_col_28 = QTableWidgetItem()
        self.p6_table_col_28.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_28.setText("pan_deg")

        self.p6_table_col_29 = QTableWidgetItem()
        self.p6_table_col_29.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_29.setText("pan_deg_s_sp")

        self.p6_table_col_30 = QTableWidgetItem()
        self.p6_table_col_30.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_30.setText("pan_deg_s_cmd")

        self.p6_table_col_31 = QTableWidgetItem()
        self.p6_table_col_31.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_31.setText("tilt_deg_sp")

        self.p6_table_col_32 = QTableWidgetItem()
        self.p6_table_col_32.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_32.setText("tilt_deg")

        self.p6_table_col_33 = QTableWidgetItem()
        self.p6_table_col_33.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_33.setText("tilt_deg_s_sp")

        self.p6_table_col_34 = QTableWidgetItem()
        self.p6_table_col_34.setTextAlignment(Qt.AlignCenter)
        self.p6_table_col_34.setText("tilt_deg_s_cmd")

        # SET COLUMN
        self.p6_table.setHorizontalHeaderItem(0, self.p6_table_col_1)
        self.p6_table.setHorizontalHeaderItem(1, self.p6_table_col_2)
        self.p6_table.setHorizontalHeaderItem(2, self.p6_table_col_3)
        self.p6_table.setHorizontalHeaderItem(3, self.p6_table_col_4)
        self.p6_table.setHorizontalHeaderItem(4, self.p6_table_col_5)
        self.p6_table.setHorizontalHeaderItem(5, self.p6_table_col_6)
        self.p6_table.setHorizontalHeaderItem(6, self.p6_table_col_7)
        self.p6_table.setHorizontalHeaderItem(7, self.p6_table_col_8)
        self.p6_table.setHorizontalHeaderItem(8, self.p6_table_col_9)
        self.p6_table.setHorizontalHeaderItem(9, self.p6_table_col_10)
        self.p6_table.setHorizontalHeaderItem(10, self.p6_table_col_11)
        self.p6_table.setHorizontalHeaderItem(11, self.p6_table_col_12)
        self.p6_table.setHorizontalHeaderItem(12, self.p6_table_col_13)
        self.p6_table.setHorizontalHeaderItem(13, self.p6_table_col_14)
        self.p6_table.setHorizontalHeaderItem(14, self.p6_table_col_15)
        self.p6_table.setHorizontalHeaderItem(15, self.p6_table_col_16)
        self.p6_table.setHorizontalHeaderItem(16, self.p6_table_col_17)
        self.p6_table.setHorizontalHeaderItem(17, self.p6_table_col_18)
        self.p6_table.setHorizontalHeaderItem(18, self.p6_table_col_19)
        self.p6_table.setHorizontalHeaderItem(19, self.p6_table_col_20)
        self.p6_table.setHorizontalHeaderItem(20, self.p6_table_col_21)
        self.p6_table.setHorizontalHeaderItem(21, self.p6_table_col_22)
        self.p6_table.setHorizontalHeaderItem(22, self.p6_table_col_23)
        self.p6_table.setHorizontalHeaderItem(23, self.p6_table_col_24)
        self.p6_table.setHorizontalHeaderItem(24, self.p6_table_col_25)
        self.p6_table.setHorizontalHeaderItem(25, self.p6_table_col_26)
        self.p6_table.setHorizontalHeaderItem(26, self.p6_table_col_27)
        self.p6_table.setHorizontalHeaderItem(27, self.p6_table_col_28)
        self.p6_table.setHorizontalHeaderItem(28, self.p6_table_col_29)
        self.p6_table.setHorizontalHeaderItem(29, self.p6_table_col_30)
        self.p6_table.setHorizontalHeaderItem(30, self.p6_table_col_31)
        self.p6_table.setHorizontalHeaderItem(31, self.p6_table_col_32)
        self.p6_table.setHorizontalHeaderItem(32, self.p6_table_col_33)
        self.p6_table.setHorizontalHeaderItem(33, self.p6_table_col_34)

        for row in range(9):
            temp = row

            # insert row after previous one
            row_number = self.p6_table.rowCount()
            self.p6_table.insertRow(row_number)

            # TODO: should the var below be a member?

            for col in range(34):

                entry = QTableWidgetItem()
                entry.setTextAlignment(Qt.AlignCenter)
                entry.setText(str(temp + 1))
                self.p6_table.setItem(row_number, col, entry)

        self.ui.load_pages.p6_table_layout.addWidget(
            self.p6_table)

        # ///////////////////////////////////////////////////////////////
        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_col_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(
            lambda: MainFunctions.set_right_col_menu(self, self.ui.right_column.menu_1))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(
                self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(
                5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(
                self.width() - 20, self.height() - 20, 15, 15)
