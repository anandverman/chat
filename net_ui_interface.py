import socket
import threading

client=None
ADDR=None
msg=None


# def init_client_socket(client):
#     client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_client_socket(address):
    global client
    global msg
    msg="hello"
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(address)
        t1=threading.Thread(target=communicate, args=(client,), daemon=True)
        # print(f"{client.family()}")
        return True
    except:
        print("Connection to server failed.")
        return False
    

def communicate(conn):
    global msg
    while True:
        msg=bytes.decode(conn.recv(2000))   #if no message is received it is empty string
        if msg=="":
            continue
        print('\n'+msg+"\nEnter message to send to server: ",end="")

def disconnect():
    global client
    client.close()