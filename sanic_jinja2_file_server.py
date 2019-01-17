from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic()

jinja = SanicJinja2(app, pkg_path='views')


@app.route('/')
@jinja.template('tmpl.jinja2')
async def homepage(request):
    return {
        'title': 'Blog Post Test',
        'contents': "Foo\nBar\nBaz",
    }


if __name__ == '__main__':
    app.run(port=8000)

"""
~ » wrk -c 100 -t 4 http://localhost:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    25.97ms    8.34ms  61.07ms   55.64%
    Req/Sec     0.97k   119.56     1.39k    71.00%
  38694 requests in 10.07s, 7.20MB read
Requests/sec:   3840.84
Transfer/sec:    731.41KB
"""
