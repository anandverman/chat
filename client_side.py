import socket
import threading

class clientside:

    def __init__(self):
        self.client=None
        self.ADDR=None
        self.msg=None
        self.msglock=threading.Lock()

    # def init_client_socket(client):
    #     client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def return_msg(self):
        # global msg
        if msg=="" or msg.isspace():
            return ""
        self.msglock.acquire()
        message= msg
        msg=""
        self.msglock.release()
        return message


    def connect_client_socket(self, address):
        # global client
        # global msg
        msg="hello"
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect(address)
            t1=threading.Thread(target=self.communicate, args=(self.client,), daemon=True)
            t1.start()
            # print(f"{client.family()}")
            return True
        except:
            print("Connection to server failed.")
            return False
        
    def send_to_server(self, msg):
        # global client
        if not self.client:
            print("Unable to send message.")
        self.client.send(bytes(msg, 'utf-8'))

    def communicate(self, conn):
        # global msg
        while True:
            self.msglock.acquire()
            msg=bytes.decode(conn.recv(2000))   #if no message is received it is empty string
            self.msglock.release()
            if msg=="":
                continue
            print('\n'+msg+"\nEnter message to send to server: ",end="")

    def disconnect(self, ):
        # global client
        self.client.close()

