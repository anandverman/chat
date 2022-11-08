import socket
import threading

client=None
ADDR=None
# msg=None
recvQ=[]
recvQLock=threading.Lock()
# msglock=threading.Lock()

# def init_client_socket(client):
#     client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def return_msg():
    # global msg
    if recvQ==[]:
        return ""
    msg=recvQ[0]
    recvQLock.acquire()
    recvQ.pop(0)
    recvQLock.release()
    # if msg=="" or msg.isspace():
    #     return ""
    # msglock.acquire()
    # message= msg
    # msg=""
    # msglock.release()
    return msg


def connect_client_socket(address):
    global client
    # global msg
    global recvQ
    msg="hello"
    recvQ=[]
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(address)
        t1=threading.Thread(target=communicate)
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

def communicate():
    # global msg
    global client
    while True:
        if not client:
            return
        # msglock.acquire()
        msg=bytes.decode(client.recv(2000))   #if no message is received it is empty string
        # msglock.release()
        if msg=="" or msg.isspace():
            continue
        recvQLock.acquire()
        recvQ.append(msg)
        recvQLock.release()
        print('\n'+msg+"\nEnter message to send to server: ",end="")

def disconnect():
    global client
    if not client:
        return
    # client.send(bytes("", 'utf-8'))
    client.close()
    print("Disconnected")