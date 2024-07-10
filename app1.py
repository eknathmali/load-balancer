from flask import Flask

app = Flask(__name__)

@app.route('/load')
def home():
    return "Hello from app2 loader!"

if __name__ == '__main__':
    app.run(port=5000)
