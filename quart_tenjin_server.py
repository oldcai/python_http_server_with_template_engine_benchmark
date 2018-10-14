from quart import Quart

import tenjin
from tenjin.helpers import *
from tenjin.html import text2html
app = Quart(__name__)

engine = tenjin.Engine(path=['views'], preprocess=True)


@app.route('/')
async def homepage():
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = engine.render('t.pyhtml', context)
    return t


if __name__ == '__main__':
    app.run(port=8000)


"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   132.63ms   34.30ms 332.20ms   92.31%
    Req/Sec   198.79     74.66   252.00     76.14%
  7599 requests in 10.03s, 1.62MB read
Requests/sec:    757.58
Transfer/sec:    164.98KB
"""
