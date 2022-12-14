# import sys
from chatui import Ui_MainWindow
from PySide6 import QtWidgets
from message_labels import send_msgbox,recv_msgbox
from net_ui_interface import *
# import threading

class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sendmsgList=[]
        self.recvmsgList=[]
        self.ip=None
        self.port=None
        global msg

        #page 1 widget actions
        self.submit_button.clicked.connect(self.submit_button_click_handler)
        self.name_edit.returnPressed.connect(self.username_label.setText(self.name_edit.text()))
        #page 2 widget actions
        self.back_button.clicked.connect(self.back_button_click_handler)
        self.typemessage_edit.returnPressed.connect(self.send_button_click_handler)
        self.send_button.clicked.connect(self.received_msg_handler)

    ##Page 1 widget functions
    def submit_button_click_handler(self):
        name=self.name_edit.text()
        self.username_label.setText(name)
        
        # if not connect_to_server(addr):
        #     self.show_error()       
        #send name(name)
        self.getserveraddr()
        if connect_client_socket((self.ip,self.port)):
            self.result_edit.setText("Connection Successful")
            self.stackedWidget.setCurrentIndex(1)
            waitthread=threading.Thread(target=self.waitformsg)
            waitthread.start()

        else:
            self.result_edit.setText("Connection Failed.")
        self.username_label.setText(f"{name} on {self.ip}")

    def getserveraddr(self):
        addr=self.serveraddr_edit.text().split(':')
        addr=('anand-pc','2002')
        self.ip=addr[0]
        try:
            self.port=int(addr[1])
        except:
            print("No port")
        print(f"{self.ip}:{self.port}")

    def waitformsg(self):                   ##Network dependent functions
        print(f"message is: {self.msg}")
        pass
        # while True: 
        #     if self.message=="":
        #         continue
        #     pass

    ##Page 2 widget functions
    def widget_delete(self, widget):
       # here you will delete your widget
       parent_layout = widget.parent().layout()
       parent_layout.removeWidget(self) # remove the widget from its parent layout
       widget.deleteLater() # lets Qt knows it needs to delete this widget from the GUI
       del widget

    def back_button_click_handler(self):
        self.clrmessages()
        disconnect()
        self.stackedWidget.setCurrentIndex(0)
    
    def clrmessages(self):
        for msg_box in self.sendmsgList:
            self.widget_delete(msg_box.sendmsg_label)
        for msg_box in self.recvmsgList:
            self.widget_delete(msg_box.recvmsg_label)
        self.sendmsgList=[]

    def send_button_click_handler(self):        ###
        msg=self.typemessage_edit.text()
        if msg=="" or msg.isspace():
            return
        self.typemessage_edit.setText("")
        self.display_sendmsg(msg)

    def received_msg_handler(self):             ###
        msg=self.typemessage_edit.text()
        if msg=="" or msg.isspace():
            return
        self.typemessage_edit.setText("")
        self.display_recvmsg(msg)

    def display_sendmsg(self, msg):
        self.sendmsgList.append(send_msgbox(self.scrollAreaWidgetContents))
        self.sendmsgList[-1].sendmsg_label.setText(msg)
        self.gridLayout_10.addWidget(self.sendmsgList[-1].sendmsg_label)
        print(f"send: {msg}")

    def display_recvmsg(self, msg):
        self.recvmsgList.append(recv_msgbox(self.scrollAreaWidgetContents))
        self.recvmsgList[-1].recvmsg_label.setText(msg)
        self.gridLayout_10.addWidget(self.recvmsgList[-1].recvmsg_label)
        print(f"recv: {msg}")

    ##Network dependent functions






# if __name__=="__main__":
#     app=QtWidgets.QApplication([])
#     window=UI()
#     window.show()
#     sys.exit(app.exec())
