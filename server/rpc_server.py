from tcp_server import Server
from json_decode import JSONRPC
from rpc_stub import RPCStub


class RPCServer(Server, JSONRPC, RPCStub):
    def __init__(self):
        # 调用 RPCServer 的 父类的方法, 在python3中super()括号内的参数可以不填,其默认值就是这个
        super(RPCServer, self).__init__()

    def loop(self):
        self.bind_listen(5000)
        while True:
            self.accept_recv_close()

    def on_msg(self, data):
        self.load_data(data)
        self.call_method()
