from japronto import Application


def hello(request):
    return request.Response(text='Hello world!')


app = Application()
app.router.add_route('/', hello)
app.run(worker_num=4, port=8000)


"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    14.82ms   31.59ms 250.18ms   86.95%
    Req/Sec    26.69k    12.10k   60.36k    65.25%
  1039348 requests in 10.08s, 91.19MB read
Requests/sec: 103071.08
Transfer/sec:      9.04MB
"""
