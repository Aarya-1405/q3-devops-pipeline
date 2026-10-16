
from flask import Flask, jsonify, Response
from prometheus_client import (
    Counter,
    generate_latest,
    CONTENT_TYPE_LATEST
)

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total application requests",
    ["endpoint"]
)


@app.route("/")
def home():
    REQUEST_COUNT.labels(endpoint="/").inc()
    return jsonify({
        "application": "End-to-End DevOps Demo",
        "message": "Application is running successfully"
    })


@app.route("/health")
def health():
    REQUEST_COUNT.labels(endpoint="/health").inc()
    return jsonify({"status": "healthy"})


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

