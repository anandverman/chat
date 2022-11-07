import socket
import threading

client=None
ADDR=None
msg=None
msglock=threading.Lock()

# def init_client_socket(client):
#     client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def return_msg():
    global msg
    if msg=="" or msg.isspace():
        return ""
    msglock.acquire()
    message= msg
    msg=""
    msglock.release()
    return message


def connect_client_socket(address):
    global client
    global msg
    msg="hello"
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(address)
        t1=threading.Thread(target=communicate, args=(client,), daemon=True)
        t1.start()
        # print(f"{client.family()}")
        return True
    except:
        print("Connection to server failed.")
        return False
    
def send_to_server(msg):
    global client
    if not client:
        print("Unable to send message.")
    client.send(bytes(msg, 'utf-8'))

def communicate(conn):
    global msg
    while True:
        msglock.acquire()
        msg=bytes.decode(conn.recv(2000))   #if no message is received it is empty string
        msglock.release()
        if msg=="":
            continue
        print('\n'+msg+"\nEnter message to send to server: ",end="")

def disconnect():
    global client
    client.close()