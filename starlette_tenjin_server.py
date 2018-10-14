from starlette.applications import Starlette
from starlette.responses import Response
import uvicorn
import tenjin
from tenjin.helpers import *
from tenjin.html import text2html

app = Starlette()
app.debug = False
engine = tenjin.Engine(path=['views'], preprocess=True)


@app.route('/')
def homepage(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = engine.render('t.pyhtml', context)
    return Response(t)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)


"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    19.51ms    6.36ms  88.10ms   75.68%
    Req/Sec     1.30k   174.69     1.71k    67.25%
  51967 requests in 10.08s, 8.87MB read
Requests/sec:   5157.15
Transfer/sec:      0.88MB
"""
