class Data:
    def __init__(self, data, ip_server):
        self.ip = ip_server
        self.data = data


class Router:
    def __init__(self):
        self.servers = {}
        self.buffer = []

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        server = self.servers.pop(server.ip, False)
        if server:
            server.router = None

    def send_data(self):
        while self.buffer:
            data = self.buffer.pop()
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)


class Server:
    number_server = 1

    def __init__(self):
        self.ip = Server.number_server
        self.router = None
        self.buffer = []
        Server.number_server += 1

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        res = self.buffer[:]
        self.buffer.clear()
        return res

    def get_ip(self):
        return self.ip
