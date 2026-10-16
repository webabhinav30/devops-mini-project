from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total requests received')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    time.sleep(random.uniform(0.01, 0.2))
    return "Hello from the CI/CD deployed app!"

@app.route('/health')
def health():
    return {"status": "ok"}, 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
