"""
Hello-world Flask application.

A deliberately tiny web service used as the starting point for a
Kubernetes support training capstone. It exposes three simple routes
and reads its configuration from environment variables so it is easy
to later externalise into ConfigMaps and Secrets.
"""

import os

from flask import Flask, jsonify

app = Flask(__name__)

# Configuration is read from the environment with safe defaults so the
# app runs out of the box. See .env.example for the supported values.
APP_NAME = os.environ.get("APP_NAME", "starter-app")
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
GREETING = os.environ.get("GREETING", "Hello, world!")


@app.route("/")
def index():
    """Return a greeting and basic app info."""
    return jsonify(
        message=GREETING,
        app=APP_NAME,
        version=APP_VERSION,
    )


@app.route("/health")
def health():
    """Liveness/readiness check. Returns a simple OK response."""
    return jsonify(status="ok"), 200


@app.route("/version")
def version():
    """Return the app name and version."""
    return jsonify(app=APP_NAME, version=APP_VERSION)


if __name__ == "__main__":
    # Local development server only. In the container the app is served
    # by gunicorn (see Dockerfile) for a more production-like setup.
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
