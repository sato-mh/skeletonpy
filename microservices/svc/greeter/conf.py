import os

GREETER_ADDRESS = os.environ.get('GREETER_ADDRESS', '0.0.0.0:5050')
IP_ADDRESS = GREETER_ADDRESS.split(':')[0]
PORT = int(GREETER_ADDRESS.split(':')[1])
