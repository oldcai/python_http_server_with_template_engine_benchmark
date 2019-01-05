import japronto_jinja2
import jinja2
from japronto import Application


@japronto_jinja2.template('tmpl.jinja2')
async def hello(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    return context


app = Application()
japronto_jinja2.setup(app, loader=jinja2.FileSystemLoader('views/'))
app.router.add_route('/', hello)
app.run(worker_num=1, port=8000)

"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.03ms    1.05ms  14.31ms   80.37%
    Req/Sec     3.56k   176.54     4.04k    67.25%
  142164 requests in 10.03s, 22.64MB read
Requests/sec:  14173.93
Transfer/sec:      2.26MB
"""
