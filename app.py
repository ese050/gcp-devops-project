from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <div style="text-align: center;">
        <h1 style="text-transform: uppercase; font-weight: bold;">Hello, From Ese</h1>
        <p>Welcome to my DevOps Flask app</p>
    </div>
    '''
if __name__ == '__main__':
    app.run()