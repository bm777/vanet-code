import os, sys, socket

class TA():

    def __init__(self):
        self.RSU0 = ""
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
        import random
        alphacode = ["a", "b", "c", "1", "2", "3", "4", ]
        tmp = ""
        for i in range(10):
            index = random.randint(0, len(alphacode)-1)
            tmp += alphacode[index]

        self.set_RSU0(tmp)


if __name__ == '__main__':

    ta = TA()
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
        ta.refresh()
        conn.sendall(ta.get_RSU0().encode() + b": from server")
        print("=================================================")
        conn.close()
