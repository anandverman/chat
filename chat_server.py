#!/home/anand/python_venv/bin/python

# server to handle multiple clients and display their message on console with message a message queue
import socket
import threading
import signal, sys

msgQlock=threading.Lock()
clients={}
msgQ=[]

server=None

def broadcast(br_msg, sender):
    for addr, client in clients.items():
        if(addr==sender):
            continue
        client.send(bytes(br_msg, 'utf-8'))
        print(f"Sending to {addr}")

def clearQ():
    global msgQ
    while True:
        if msgQ ==[]:
            continue
        msgQlock.acquire()
        broadcast(msgQ[0][1], msgQ[0][0])
        msgQ.pop(0)
        msgQlock.release()
        

def fillQ(br_msg, addr):
    global msgQ
    msgQlock.acquire()
    msgQ.append([addr, br_msg])
    msgQlock.release()

def communicate(conn, addr):
    conn.send(bytes(f"Welcome to chat!",'utf-8'))
    msg="a"
    while len(msg):
        # if not conn:
        #     print("Bye")
        #     break
        try:
            msg=bytes.decode(conn.recv(2000))
            if(msg):
                print(f"{addr} sent: {msg}")
                br_msg=f"<{addr}>: {msg}"
                fillQ(br_msg, addr)
                # broadcast(br_msg, addr) 
        except:
            continue
    print(f"Client {addr} disconnected.")       
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
    t2=threading.Thread(target=clearQ, daemon=True)
    t2.start()
    while True:
        conn, addr= server.accept()
        clients[addr]=conn
        print(f"Connected to {addr}")
        t1=threading.Thread(target=communicate, args=(conn, addr ), daemon=True)
        t1.start()
        