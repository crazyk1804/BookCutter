import sys
from PyQt6 import QtWidgets

from book_cutter_app.gui.ui_controller.win_main_controller import WIN_MainController


if __name__ == "__main__":
	# print(get_working_path())
	# stylesheet = open('resource/style.qss', 'r').read()

	app = QtWidgets.QApplication(sys.argv)
	# app.setStyleSheet(stylesheet)
	ui = WIN_MainController()
	ui.show()
	sys.exit(app.exec())