class App():
    def __init__(self, scope):
        assert scope['type'] == 'http'
        self.scope = scope

    async def __call__(self, receive, send):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': b'Hello, world!',
        })




"""
~ » uvicorn uvicorn_str_app:App > /dev/null 2>&1 &
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    11.80ms    3.15ms  30.32ms   51.76%
    Req/Sec     2.12k   166.54     2.61k    74.00%
  85085 requests in 10.07s, 12.17MB read
Requests/sec:   8451.67
Transfer/sec:      1.21MB
"""
