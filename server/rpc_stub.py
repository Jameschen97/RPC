class RPCStub(object):
    def __init__(self):
        pass

    def foo(self, a, b, c):
        print("foo:", a, b, c)
        return self

    def bar(self, a, b, c=10):
        print("bar:", a, b, c)
        return self