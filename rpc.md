
## 1. tcp server tcp client

    tcp server 
        bind accept recv parse call
    tcp client 
        connect send data
    
## 2. function name function args function kwargs
    
    json
    {
        'function_name':name,
        'function_args':args,
        'function_kwargs':kwargs
    }
    
## 3. client

    c.foo(1, 2, 3)

    send
    {
        'function_name':'foo',
        'function_args':(1,2,3),
        'function_kwargs':{}
    }

    __getattr__ pack

## 4. server

    recv json
    {
        'function_name':'foo',
        'function_args':(1,2,3),
        'function_kwargs':{}
    }

    getattr(self, 'foo')
    getattr(self, 'foo')(*args, **kwargs)
