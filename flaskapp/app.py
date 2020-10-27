from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

app = Flask(__name__)


@app.route("/index")
def index():
    return "Index Page", 200


@app.route("/health")
def health():
    return "I am healthy", 200


@app.route("/error")
def error():
    return "Internal Server Error!", 500

# provide app"s version and deploy environment/config name to set a gauge
# metric
register_metrics(app, app_version="v0.1", app_config="workshop")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

run_simple(hostname="0.0.0.0", port=5000, application=dispatcher)
