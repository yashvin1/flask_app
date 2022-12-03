from flask import Flask
import socket
app = Flask(__name__)
hostname=socket.gethostname()
ip_address = socket.gethostbyname(hostname)


@app.route('/')
def hello_name():
	return f'Instance name and ip_address :- {hostname}{ip_address}'

if __name__ == '__main__':
      app.run()
