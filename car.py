import os, socket
import pickle
from cryptography.fernet import Fernet




if __name__ == '__main__':

    id = Fernet.generate_key()
    host = "127.0.0.1"
    port = 12346
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(id)
    # Receive no more than 1024 bytes
    data = s.recv(2048)

    for elt in pickle.loads(data):
        print("----[not encoded]", elt)

    s.close()
