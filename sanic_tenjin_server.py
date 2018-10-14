from sanic import Sanic
from sanic.response import html

import tenjin
from tenjin.helpers import *
from tenjin.html import text2html

app = Sanic()

engine = tenjin.Engine(path=['views'], preprocess=True)


@app.route('/')
async def homepage(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = engine.render('t.pyhtml', context)
    return html(t)

app.run(port=8000)

"""
Running 10s test @ http://localhost:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    28.39ms   29.22ms 269.25ms   95.13%
    Req/Sec     1.08k   250.88     1.53k    83.03%
  42155 requests in 10.10s, 8.20MB read
Requests/sec:   4174.97
Transfer/sec:    831.73KB
"""