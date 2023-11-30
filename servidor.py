import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola!'

if __name__ == '__main__':
    if len(sys.argv)>1:
        app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))
    else:
        app.run(host='0.0.0.0', port=80)
    
