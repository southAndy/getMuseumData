from flask import Flask

app = Flask(__name__)

# todo 如何新增巢狀路由


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello, World!'


@app.route('/news/')
def news():
    return 'The news page'


@app.route('/exhibitions/')
def exhibitions():
    return 'The exhibitions page'


# todo 新增後台管理系統
@app.route('/register')
def about():
    return 'The about page'


@app.route('/login')
def login():
    return 'The login page'
