from client import Client
from rpc_stub import RPCStub


class RPCClient(Client, RPCStub):
    def __init__(self):
        super(RPCClient, self).__init__()
