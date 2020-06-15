from flask import Flask
from app import app

if __name__ == '__main__':
    port = 5000
    app.run(host="0.0.0.0", port=port, debug=True, )
