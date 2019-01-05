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
    Latency     8.36ms   21.28ms 238.68ms   90.64%
    Req/Sec    24.86k     9.49k   61.23k    74.81%
  986678 requests in 10.02s, 86.57MB read
Requests/sec:  98475.98
Transfer/sec:      8.64MB
"""
