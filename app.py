from flask import Flask, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

@app.route("/")
def index():
    ip = request.remote_addr
    ua = request.headers.get("User-Agent", "Unknown")
    return render_template("index.html", ip=ip, user_agent=ua)

if __name__ == "__main__":
    app.run()
