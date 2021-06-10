import zeep

wsdl = 'http://localhost:3333/?wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.get_fibonacci(25)) 