from flask import Flask
import platform

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world from %s!\n" % platform.uname().machine

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
