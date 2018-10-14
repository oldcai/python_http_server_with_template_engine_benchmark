from japronto import Application
import tenjin
from tenjin.helpers import *
from tenjin.html import text2html

engine = tenjin.Engine(path=['views'], preprocess=True)


def hello(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = engine.render('t.pyhtml', context)
    return request.Response(text=t)


app = Application()
app.router.add_route('/', hello)
app.run(worker_num=1, port=8000)


"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.23ms    1.72ms  42.41ms   95.65%
    Req/Sec     7.87k     0.92k   10.10k    73.00%
  313753 requests in 10.03s, 49.67MB read
Requests/sec:  31273.63
Transfer/sec:      4.95MB
"""