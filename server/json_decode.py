import json


class JSONRPC(object):
    def __init__(self):
        self.data = None

    def load_data(self, data):
        # 将 bytes 转成 str ,
        # 用 json loads 读取 str 数据
        self.data = json.loads(data.decode('utf-8'))

    def call_method(self):
        method_name = self.data['method_name']
        method_args = self.data['method_args']
        method_kwargs = self.data['method_kwargs']

        getattr(self, method_name)(*method_args, **method_kwargs)
