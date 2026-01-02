from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "This Flask app is deployed on Azure using Docker & Coolify with GitHub-based CI/CD 🚀"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
