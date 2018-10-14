from japronto import Application
from jinja2 import Template
template = Template("""
 <HTML>
 <HEAD><TITLE>{{ title }}</TITLE></HEAD>
 <BODY>
{{ post_content }}
 </BODY>
 </HTML>""")


def hello(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = template.render(context)
    return request.Response(text=t)


app = Application()
app.router.add_route('/', hello)
app.run(worker_num=1, port=8000)

"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.68ms    2.72ms  71.54ms   97.29%
    Req/Sec     7.07k     0.88k    9.61k    81.25%
  282074 requests in 10.03s, 45.73MB read
Requests/sec:  28123.94
Transfer/sec:      4.56MB
"""
