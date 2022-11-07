#!/home/anand/python_venv/bin/python

# server to handle multiple clients and display their message on console
import socket
import threading
import signal, sys

clients={}
msgQ={}

server=None

def broadcast(br_msg, sender):
    for addr, client in clients.items():
        if(addr==sender):
            continue
        client.send(bytes(br_msg, 'utf-8'))
        print(f"Sending to {addr}")

    

def communicate(conn, addr):
    conn.send(bytes(f"Welcome to chat!",'utf-8'))
    msg="a"
    while len(msg):
        msg=bytes.decode(conn.recv(2000))
        if(msg):
            print(msg)
            br_msg=f"<{addr[0]}> {msg}"
            broadcast(br_msg, addr)
        
    conn.close()
    del clients[addr]

def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!\nClosing Server Socket')
    global server
    for _,conn in clients.items():
        conn.close()
    server.close()
    sys.exit(0)


if __name__=='__main__':
    SERVERADDR=(socket.gethostname(), 2002)
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SERVERADDR)
    server.listen(1)
    print(f"Socket is Listening at {SERVERADDR}")
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        conn, addr= server.accept()
        clients[addr]=conn
        # lock.acquire()
        print(f"Connected to {addr[0]}")
        t1=threading.Thread(target=communicate, args=(conn, addr ), daemon=True)
        t1.start()