import os, sys, socket
import cryptography, hashlib, rsa
import pickle
from hashlib import sha512
from cryptography.fernet import Fernet


class TA():

    def __init__(self):
        self.RSU0 = Fernet.generate_key()      # OK
        self.IDta = ""
        self.private = ""
        self.shared = ""

    def __str__(self):
        return "__TA class__"

    def __del__(self):
        del self
    ############################## getters
    def get_RSU0(self):
        return self.RSU0

    def get_IDta(self):
        return self.IDta

    def get_private(self):
        return self.private

    def get_shared(self):
        return self.shared

    ############################## setters
    def set_RSU0(self, tmp):
        if tmp != self.RSU0:
            self.RSU0 = tmp

    def set_IDta(self, tmp):
        if tmp != self.IDta:
            self.IDta = tmp

    def set_private(self, tmp):
        if tmp != self.private:
            self.private = tmp

    def set_shared(self, tmp):
        if tmp != self.shared:
            self.shared = tmp

    ####################################################### functions
    def refresh(self):
        # key = Fernet.generate_key()
        # public and private key
        public, private = rsa.newkeys(512)
        # generate shared key

        shared = Fernet.generate_key()

        return [public, shared, private]

    def cupdate(self):
        return self.refresh()

    public = ""
    def hs(self, data):
        hash = int.from_bytes(sha512("{}".format(data).encode()).digest(), byteorder='big')
        k = self.genkey()
        public = (hex(k.n), hex(k.e))
        signature = pow(hash, k.d, k.n)
        return signature

    def sign(self, cupdate):

        # hashed = [rsa.encrypt(hashlib.sha256("{}".format(h).encode()).hexdigest(), cupdate[2]) for h in cupdate]
        hashed = ["{}".format(self.hs(h)).encode() for h in cupdate]
        return hashed

    def genkey(self):
        from Crypto.PublicKey import RSA
        return RSA.generate(bits=1024)


if __name__ == '__main__':

    ta = TA()
    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("Server launched ...")

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(2048)
        if not data: break
        print("======= data = ", data.decode())
        tmp = ta.cupdate()
        signed = ta.sign(tmp)
        final = tmp
        for sign in signed:
            final.append(sign)
        final.append(ta.IDta)
        final.append(ta.RSU0)
        data = pickle.dumps(final)

        conn.sendall(data)
        print("=================================================")
        ta.set_RSU0(tmp[0])
        ta.set_shared(tmp[1])
        ta.set_private(tmp[2])
        conn.close()
