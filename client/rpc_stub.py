import json


class RPCStub(object):
    def __getattr__(self, item):
        def yoo(*args ,**kwargs):
            d = {
                'method_name': item,
                'method_args': args,
                'method_kwargs': kwargs,
                }
            self.send(json.dumps(d).encode('utf-8'))

        setattr(self, item, yoo)
        return yoo
