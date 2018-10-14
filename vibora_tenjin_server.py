from vibora import Vibora, Request
from vibora.responses import Response

import tenjin
from tenjin.helpers import *
from tenjin.html import text2html

app = Vibora()

engine = tenjin.Engine(path=['views'], preprocess=True)


@app.route('/')
async def homepage(request: Request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = engine.render('t.pyhtml', context)
    return Response(t.encode('utf-8'), headers={'content-type': 'html'})

app.run(port=8000)

"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.69ms   30.47ms 291.26ms   94.89%
    Req/Sec     1.99k   527.86     2.92k    80.46%
  77909 requests in 10.08s, 13.52MB read
Requests/sec:   7727.74
Transfer/sec:      1.34MB
"""