from sanic import Sanic
from sanic.response import html
from jinja2 import Template
app = Sanic()

template = Template("""
 <HTML>
 <HEAD><TITLE>{{ title }}</TITLE></HEAD>
 <BODY>
{{ contents }}
 </BODY>
 </HTML>""")


@app.route('/')
async def homepage(request):
    context = {
        'title': 'Blog Post Test',
        'contents': "Foo\nBar\nBaz",
    }
    t = template.render(context)
    return html(t)


app.run(debug=True, port=8000)

"""
~ » wrk -c 100 -t 4 http://localhost:8000 -d 10
Running 10s test @ http://localhost:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   117.50ms   76.33ms 612.01ms   93.65%
    Req/Sec   244.11     93.25   474.00     66.94%
  9179 requests in 10.04s, 1.82MB read
Requests/sec:    913.88
Transfer/sec:    185.63KB
"""
