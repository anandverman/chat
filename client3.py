#!/home/anand/python_venv/bin/python

#corresponding client for server3
import socket
import threading

def communicate(conn):
    while True:
        msg=bytes.decode(conn.recv(2000))   #if no message is received it is empty string
        if msg=="":
            continue
        print('\n'+msg+"\nEnter message to send to server: ",end="")


if __name__=='__main__':
    ADDR=(socket.gethostname(), 2002)
    client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(client.connect(ADDR))
    print(f"Connected to server {ADDR}")
    print(f"Server says {bytes.decode(client.recv(2000))}")
    t1=threading.Thread(target=communicate, args=(client,), daemon=True)
    t1.start()
    msg="a"
    while len(msg):
        msg=input("Enter message to send to server: ")
        client.send(bytes(msg, 'utf-8'))
    client.close()