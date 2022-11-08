#!/home/anand/python_venv/bin/python

from uifunction import UI
from PySide6 import QtWidgets

import socket
import sys
import net_ui_interface


def main():
    app=QtWidgets.QApplication([])
    window=UI()
    # window=chatApp()
    window.show()
    # net_ui_interface.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sys.exit(app.exec())

main()