from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.primitive import UnsignedInteger, String
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11

class HelloWorldService(ServiceBase):
    @srpc(UnsignedInteger, _returns=String)
    def get_fibonacci(n):
        x = ['0']
        while int(x[-1]) < n:
            if int(x[-1]) == 0:
                x.append('1')
            else:
                x.append(str(int(x[-1])+int(x[-2])))
        x.pop()
        return ('').join(x)

if __name__=='__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    app = Application([HelloWorldService], tns='spyne.examples.hello', in_protocol=Soap11(), out_protocol=Soap11())
    wsgi_app = WsgiApplication(app)
    server = make_server('0.0.0.0', 3333, wsgi_app)

    print("listening to http://127.0.0.1:3333")
    print("wsdl is at: http://localhost:3333/?wsdl")

    server.serve_forever()