from aiohttp import web
import tenjin
from tenjin.helpers import *
from tenjin.html import text2html

app = web.Application()
engine = tenjin.Engine(path=['views'], preprocess=True)


async def hello(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = engine.render('t.pyhtml', context)
    return web.Response(text=t)


app.add_routes([web.get('/', hello)])
web.run_app(app, port=8000)


"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    29.35ms    6.35ms  78.86ms   92.17%
    Req/Sec     0.86k   147.23     1.01k    85.00%
  34413 requests in 10.08s, 7.78MB read
Requests/sec:   3414.13
Transfer/sec:    790.20KB
"""