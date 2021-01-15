import os, socket
import pickle




if __name__ == '__main__':
    host = "127.0.0.1"
    port = 12346
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b"Data request car data")
    # Receive no more than 1024 bytes
    data = s.recv(2048)

    for elt in pickle.loads(data):
        print("----[not encoded]", elt)

    s.close()
