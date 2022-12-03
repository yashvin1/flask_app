from flask import Flask
import socket
app = Flask(__name__)
hostname=socket.gethostname()
IP=socket.gethostbyaddr()

@app.route('/')
def hello_name():
	return f'Instance name :- {hostname}{IP}'

if __name__ == '__main__':
      app.run()
