from flask import Flask
import socket
app = Flask(__name__)
hostname=socket.gethostname()

@app.route('/')
def hello_name():
	return f'Instance name :- {hostname}'

if __name__ == '__main__':
		app.run()
