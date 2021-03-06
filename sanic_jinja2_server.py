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


app.run(port=8000)

"""
~ » wrk -c 100 -t 4 http://localhost:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    20.68ms    5.30ms  67.26ms   67.06%
    Req/Sec     1.21k   133.62     1.69k    67.42%
  48596 requests in 10.09s, 9.64MB read
Requests/sec:   4816.29
Transfer/sec:      0.96MB
"""
