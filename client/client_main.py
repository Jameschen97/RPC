from rpc_client import RPCClient


c = RPCClient()
c.connect('127.0.0.1', 5000)
# c.bar(1, 2, c=6)
c.foo(1, 2, 3)
