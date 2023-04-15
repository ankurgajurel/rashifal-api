from flask import Flask, jsonify, abort, request
from flask_limiter import Limiter

import json
import all_data

app = Flask(__name__)
limiter = Limiter(
    app,
    default_limits=["100 per day", "10 per hour"]
)

@app.route('/')
def index():
    return 'you are using rashifal api'

@app.route('/daily/<rashi>')
@limiter.limit("10 per minute")
def daily(rashi):
    return json.dumps(all_data.get_daily(rashi))

@app.route('/monthly/<rashi>')
def monthly(rashi):
    return json.dumps(all_data.get_monthly(rashi))

@app.route('/yearly/<rashi>')
def yearly(rashi):
    return json.dumps(all_data.get_yearly(rashi))

@app.errorhandler(429)
def rate_limit_exceeded(e):
    retry_after = e.description
    return jsonify({
        "error": "Rate limit exceeded. Try again in %s seconds." % retry_after
    }), 429

@limiter.request_filter
def get_remote_address():
    """Extracts the remote address from the request object."""
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    return request.remote_addr

if __name__ == "__main__":
    app.run(debug=True, port=9991)
