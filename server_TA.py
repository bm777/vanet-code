import os, sys, socket

class TA():

    def __init__(self):
        RSU0 = ""
        IDta = ""
        private = ""
        shared = ""


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


if __name__ == '__main__':

    host = "192.168.8.101"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("Server launched ...")

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        if not data: break
        print("======= data = ", data.decode())
        print("=================================================")
        conn.sendall(data + b"from server")
        conn.close()
