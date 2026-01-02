from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <h1>GUL NİHAL ARİKAYMAK'S Flask CI/CD Demo 🚀</h1>
    <p>This application is deployed on an Azure Virtual Machine.</p>
    <ul>
      <li>🐳 Containerized with Docker</li>
      <li>⚙️ Managed and deployed using Coolify</li>
      <li>🔁 Connected to GitHub for automatic CI/CD</li>
    </ul>
    <p>Every push to the GitHub repository triggers an automatic redeploy.</p>
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
