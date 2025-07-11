from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "h1, have updated this"

if __name__ == '__main__':
    app.run()
