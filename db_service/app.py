import redis
from flask import Flask

app = Flask(__name__)

# Connect to Redis database
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def get_counter():
    count = redis_client.get('counter')
    if count:
        return f"Counter: {int(count)}"
    else:
        return "Counter not found"

@app.route('/increment')
def increment_counter():
    count = redis_client.incr('counter')
    return f"Counter incremented to: {count}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')