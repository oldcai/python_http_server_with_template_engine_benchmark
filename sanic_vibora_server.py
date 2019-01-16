from sanic import Sanic
from sanic.response import html
from vibora.templates import TemplateEngine, Template

app = Sanic()
engine = TemplateEngine()

template = Template("""
 <HTML>
 <HEAD><TITLE>{{ title }}</TITLE></HEAD>
 <BODY>
{{ contents }}
 </BODY>
 </HTML>""")

engine.add_template(template, ['benchmark'])
engine.compile_templates(verbose=False)


@app.route('/')
async def homepage(request):
    context = {
        'title': 'Blog Post Test',
        'contents': "Foo\nBar\nBaz",
    }
    t = await engine.render('benchmark', **context)
    return html(t)


app.run(port=8000)

"""
~ » wrk -c 100 -t 4 http://localhost:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    21.28ms    5.12ms  56.02ms   75.93%
    Req/Sec     1.18k   146.43     1.53k    64.39%
  47082 requests in 10.05s, 9.34MB read
Requests/sec:   4682.98
Transfer/sec:      0.93MB
"""
