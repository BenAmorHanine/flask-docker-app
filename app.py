from flask import Flask
app = Flask(__name__)

# Root route
@app.route('/')
def hello_world():
    return 'Hello, Docker World!'

# About route
@app.route('/about')
def about():
    return 'This is the About page for our Dockerized Flask app.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

