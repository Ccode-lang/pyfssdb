import socket

class db(object):
    def __init__(self, ip : str):
        self.ip = ip
    # Send message to server and collect output
    def send_msg(self, msg : str):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(20)
        sock.connect((self.ip, 4626))
        sock.send(msg.encode())
        backmsg = sock.recv(1024).decode()
        sock.close()
        return backmsg
    # Create dictionary
    def create_dict(self, name):
        return self.send_msg(f"CREATED {name}")
    # Delete dictionary
    def delete_dict(self, name):
        return self.send_msg(f"DELETED {name}")
    # Write data point
    def write_point(self, dname, pname, data):
        return self.send_msg(f"WRITEP {dname} {pname} {data}")
    # Delete data point
    def delete_point(self, dname, pname):
        return self.send_msg(f"DELETEP {dname} {pname}")
    # Read data point
    def read_point(self, dname, pname):
        return self.send_msg(f"READP {dname} {pname}")
    # PING command
    def ping(self):
        return self.send_msg("PING")
    # Powerdown
    def powerdown(self):
        return self.send_msg("POWERDOWN")