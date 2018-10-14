from sanic import Sanic
from sanic.response import html

app = Sanic()


@app.route('/')
async def homepage(request):
    return html('')


app.run(port=8000)

"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    28.60ms   46.57ms 430.72ms   96.51%
    Req/Sec     1.21k   180.98     1.50k    80.41%
  46959 requests in 10.09s, 5.24MB read
Requests/sec:   4656.28
Transfer/sec:    532.02KB
"""