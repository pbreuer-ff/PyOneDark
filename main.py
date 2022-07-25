# ///////////////////////////////////////////////////////////////
#
# GUI based on template 'PyOneDark' by: Wanderson M. Pimenta
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
import functools
import qasync
import asyncio

# IMPORT APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
from program import *

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# FOR 4K MONITOR: SET 'os.environ["QT_SCALE_FACTOR"] = "2"'


# MAIN WINDOW
# ///////////////////////////////////////////////////////////////

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # START PROGRAM
        # ///////////////////////////////////////////////////////////////
        program1 = program()

        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self, program1)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check function by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove selection if clicked by "btn_close_left_column"
        if btn.objectName() != "lm_btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get title bar btn and reset active
        top_settings = MainFunctions.get_title_bar_btn(
            self, "titlemenu_btn_monitor")
        top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # PAGE 1
        if btn.objectName() == "lm_btn_page_1":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

            self.ui.active_page = 1

            # Show/hide
            self.ui.left_menu.show_help(True)
            self.ui.left_menu.show_settings(False)
            self.ui.title_bar.show_monitor(self.ui.program.connected)

            # Update settings/help
            MainFunctions.update_left_column(self, True, False, btn)

        # PAGE 2
        if btn.objectName() == "lm_btn_page_2":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

            self.ui.active_page = 2

            # Show/hide
            self.ui.left_menu.show_help(True)
            self.ui.left_menu.show_settings(False)
            self.ui.title_bar.show_monitor(self.ui.program.connected)

            # Update settings/help
            MainFunctions.update_left_column(self, True, False, btn)

        # PAGE 3
        if btn.objectName() == "lm_btn_page_3":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

            self.ui.active_page = 3

            # Show/hide
            self.ui.left_menu.show_help(True)
            self.ui.left_menu.show_settings(True)
            self.ui.title_bar.show_monitor(self.ui.program.connected)

            # Update settings/help
            MainFunctions.update_left_column(self, True, True, btn)

        # PAGE 4
        if btn.objectName() == "lm_btn_page_4":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 4
            MainFunctions.set_page(self, self.ui.load_pages.page_4)

            self.ui.active_page = 4

            # Show/hide
            self.ui.left_menu.show_help(True)
            self.ui.left_menu.show_settings(True)
            self.ui.title_bar.show_monitor(self.ui.program.connected)

            # Update settings/help
            MainFunctions.update_left_column(self, True, True, btn)

        # PAGE 5
        if btn.objectName() == "lm_btn_page_5":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 5
            MainFunctions.set_page(self, self.ui.load_pages.page_5)

            self.ui.active_page = 5

            # Show/hide
            self.ui.left_menu.show_help(True)
            self.ui.left_menu.show_settings(False)
            self.ui.title_bar.show_monitor(self.ui.program.connected)

            # Update settings/help
            MainFunctions.update_left_column(self, True, False, btn)

        # PAGE 6
        if btn.objectName() == "lm_btn_page_6":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 6
            MainFunctions.set_page(self, self.ui.load_pages.page_6)

            self.ui.active_page = 6

            # Show/hide
            self.ui.left_menu.show_help(True)
            self.ui.left_menu.show_settings(True)
            self.ui.title_bar.show_monitor(self.ui.program.connected)

            # Update settings/help
            MainFunctions.update_left_column(self, True, True, btn)
    

        # BOTTOM: HELP
        if btn.objectName() == "lm_btn_help":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show/hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show/hide
                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change left column menu
            if btn.objectName() != "btn_close_left_column":
                """ TODO: call different menu depending on active page
                menu = getattr(self.ui.left_column.menus, 'page_' + str(self.ui.active_page) + '_settings') """
                menu = self.ui.left_column.menus.menu_help

                title = "Help: "
                for btn in self.ui.left_menu.findChildren(QPushButton):
                    settings_btn_id = "lm_btn_page_" + str(self.ui.active_page)
                    if btn.objectName() == settings_btn_id:
                        title = title + btn.text()

                MainFunctions.set_left_column_menu(
                    self,
                    menu,
                    title,
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # BOTTOM: SETTINGS
        if btn.objectName() == "lm_btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show/hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show/hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change left column menu
            if btn.objectName() != "btn_close_left_column":
                """ TODO: call different menu depending on active page
                menu = getattr(self.ui.left_column.menus, 'page_' + str(self.ui.active_page) + '_settings') """
                menu = self.ui.left_column.menus.menu_settings

                title = "Settings: "
                for btn in self.ui.left_menu.findChildren(QPushButton):
                    settings_btn_id = "lm_btn_page_" + str(self.ui.active_page)
                    if btn.objectName() == settings_btn_id:
                        title = title + btn.text()

                MainFunctions.set_left_column_menu(
                    self,
                    menu,
                    title,
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == "titlemenu_btn_monitor":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show/hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show/hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn
            top_settings = MainFunctions.get_left_menu_btn(
                self, "lm_btn_settings")
            top_settings.set_active_tab(False)

        # DEBUG
        print(f"{btn.objectName()} clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check function by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"{btn.objectName()} released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


async def main():

    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()

    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = QApplication.instance()
    app.setWindowIcon(QIcon("./images/freefly_logo.ico"))
    if hasattr(app, "aboutToQuit"):
        # clean up if gui app wants to quit
        getattr(app, "aboutToQuit").connect(
            functools.partial(close_future, future, loop)
        )

    window = MainWindow()

    await future
    return True


if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)
