from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/get-user", methods=['GET'])
def get_user():
    return "<h1>GET USER SUCCESSFUL</h1>"


@app.route("/add-user", methods=['POST'])
def add_user():
    print(request.url)
    return "request successful"


@app.route('/login-user', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.get_json(force=True))
        return post_handler()
    else:
        return get_handler()


def post_handler():
    return "<p>post response</p>"


def get_handler():
    return "<p>get response</p>"
