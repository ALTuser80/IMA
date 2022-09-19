from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return ("Welcome to omars test API, Contact us at +17828008103")

if __name__ == "__main__":
