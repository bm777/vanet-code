import os, sys, socket
import cryptography, hashlib
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
import pickle

class RSU():

    def __init__(self, data):
        RSU0 = data[0]
        IDta = data[1]
        private = data[2]
        shared = data[3]


    def get_RSU0(self):
        return self.RSU0

    def get_IDta(self):
        return self.IDta

    def get_private(self):
        return self.private

    def get_shared(self):
        return self.shared

    ##############################
    def set_RSU0(self, tmp):
        if tmp != self.RSU0:
            selft.RSU0 = tmp

    def set_IDta(self, tmp):
        if tmp != self.IDta:
            selft.IDta = tmp

    def set_private(self, tmp):
        if tmp != self.private:
            selft.private = tmp

    def set_shared(self, tmp):
        if tmp != self.shared:
            selft.shared = tmp

    ############################################ functions
    def compare(self, data, ):

        fef

    def hs(self, data):
        hash = int.from_bytes(sha512("{}".format(data).encode()).digest(), byteorder='big')
        k = self.genkey()
        signature = pow(hash, k.d, k.n)
        return signature

if __name__ == '__main__':

    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b"Data request RSU data")
    # Receive no more than 1024 bytes
    data = s.recv(2048)

    s.close()

    print("The time got from the server is ")

    for elt in pickle.loads(data):
        print("----",elt)
