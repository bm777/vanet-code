import os, sys, socket
import cryptography, hashlib
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
import pickle

class RSU():

    def __init__(self, data):
        self.RSU0 = data[0]
        self.IDta = data[1]
        self.private = data[2]
        self.shared = data[3]



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

        pass

    def hs(self, data):
        hash = int.from_bytes(sha512("{}".format(data).encode()).digest(), byteorder='big')
        k = self.genkey()
        signature = pow(hash, k.d, k.n)
        return signature


def get_env():
    return [os_environ["PUBLIC"],
            os_environ["SHARED"],
            os_environ["PRIVATE"],
            os_environ["IDta"],
            os_environ["RSU0"] ]

if __name__ == '__main__':

    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b"Data request RSU data")
    # Receive no more than 1024 bytes
    data = s.recv(2048)

    s.close()

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("Receive from TA .............................................")
    local_data = []
    for elt in pickle.loads(data):
        if type(elt) == type("".encode()):
            print("----[not encoded]",elt.decode())
            local_data.append(elt.decode())
        else:
            print("----[encoded]", elt)
            local_data.append(elt)

    ####### setting data #############

    os_environ = {}
    os_environ['PUBLIC'] = local_data[0]
    # print("{}".format(local_data[2].exportKey()), file=prv_file)
    os_environ['SHARED'] = local_data[1]
    os_environ['PRIVATE'] = local_data[2]
    os_environ['IDta'] = local_data[3]
    os_environ['RSU0'] = local_data[4]
    rsu = RSU([os_environ['RSU0'], os_environ['IDta'], os_environ['PRIVATE'], os_environ['SHARED']])

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n')

    port2 = 12346
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port2))
    s.listen(5)
    print("Server RSU launched ...")
    while  True:
        conn2, addr = s.accept()
        print('Connected by', addr)
        data_id = conn2.recv(2048)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")


        data = [data_id.decode(), os_environ["RSU0"]]
        print("=============== data sent to car: ", data)
        data = pickle.dumps(data)

        conn2.sendall(data)
        conn2.close()

    # print(get_env())
