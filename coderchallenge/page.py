# page.py

from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(
    host='redis-db',
    port=6379,
    decode_responses=True
)


@app.route('/')
def hello_world():
    # Increment page visit counter
    visits = r.incr('visits')

    return f'Hello, World! This page has been visited {visits} times'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)