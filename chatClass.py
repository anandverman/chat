from uifunction import UI
from client_side import clientside



class chatApp(UI, clientside):
    def __init__(self):
        super().__init__()
        
    #page 1 widget actions
        self.submit_button.clicked.connect(self.submit_button_click_handler)
        self.name_edit.returnPressed.connect(self.username_label.setText(self.name_edit.text()))
        #page 2 widget actions
        self.back_button.clicked.connect(self.back_button_click_handler)
        self.typemessage_edit.returnPressed.connect(self.send_button_click_handler)
        self.send_button.clicked.connect(self.send_button_click_handler)
    
    # Functions
    ##############################################################################################################
    def submit_button_click_handler(self):
        name=self.name_edit.text()
        self.username_label.setText(name)
        
        self.submit_button.clicked.connect(self.submit_button_click_handler)
        self.name_edit.returnPressed.connect(self.username_label.setText(self.name_edit.text()))
        #page 2 widget actions
        self.back_button.clicked.connect(self.back_button_click_handler)
        self.typemessage_edit.returnPressed.connect(self.send_button_click_handler)
        self.send_button.clicked.connect(self.send_button_click_handler)

    ##Page 1 widget functions
    def submit_button_click_handler(self):
        name=self.name_edit.text()
        self.username_label.setText(name)
        
        # if not connect_to_server(addr):
        #     self.show_error()       
        #send name(name)
        self.getserveraddr()
        if self.connect_client_socket((self.ip,self.port)):
            self.result_edit.setText("Connection Successful")
            self.stackedWidget.setCurrentIndex(1)
            recvthread=self.threading.Thread(target=self.getmsg)
            recvthread.start()

        else:
            self.result_edit.setText("Connection Failed.")
        self.username_label.setText(f"{name} on {self.ip}")

    # def getserveraddr(self):
    #     addr=self.serveraddr_edit.text().split(':')
    #     addr=('anand-pc','2002')
    #     self.ip=addr[0]
    #     try:
    #         self.port=int(addr[1])
    #     except:
    #         print("No port")
    #     print(f"{self.ip}:{self.port}")

    

        
    ##Page 2 widget functions
    # def widget_delete(self, widget):
    #    # here you will delete your widget
    #    parent_layout = widget.parent().layout()
    #    parent_layout.removeWidget(self) # remove the widget from its parent layout
    #    widget.deleteLater() # lets Qt knows it needs to delete this widget from the GUI
    #    del widget

    def back_button_click_handler(self):
        self.clrmessages()
        self.disconnect()
        self.stackedWidget.setCurrentIndex(0)
    
    # def clrmessages(self):
    #     for msg_box in self.sendmsgList:
    #         self.widget_delete(msg_box.sendmsg_label)
    #     # for msg_box in self.recvmsgList:
    #     #     self.widget_delete(msg_box.recvmsg_label)
    #     self.sendmsgList=[]
    #     self.recvmsgList=[]

    def send_button_click_handler(self):        ###
        msg=self.typemessage_edit.text()
        if msg=="" or msg.isspace():
            return
        self.send_to_server(msg)
        self.typemessage_edit.setText("")
        self.display_sendmsg(msg)

    # def received_msg_handler(self):             ###
    #     msg=self.typemessage_edit.text()
    #     if msg=="" or msg.isspace():
    #         return
    #     self.typemessage_edit.setText("")
    #     self.display_recvmsg(msg)

    def getmsg(self):                   ##Network dependent function
        while True:
            msg=self.return_msg()
            if msg=="":
                continue
            self.display_recvmsg(msg)

    # def display_sendmsg(self, msg):
    #     self.sendmsgList.append(self.send_msgbox(self.scrollAreaWidgetContents))
    #     self.sendmsgList[-1].sendmsg_label.setText(msg)
    #     self.gridLayout_10.addWidget(self.sendmsgList[-1].sendmsg_label)
    #     print(f"send: {msg}")

    # def display_recvmsg(self, msg):
    #     self.recvmsgList.append(self.recv_msgbox(self.scrollAreaWidgetContents))
    #     self.recvmsgList[-1].recvmsg_label.setText(msg)
    #     self.gridLayout_10.addWidget(self.recvmsgList[-1].recvmsg_label)
    #     print(f"recv: {msg}")
