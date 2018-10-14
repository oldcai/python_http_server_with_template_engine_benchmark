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


app.run(debug=True, port=8000)

"""
~ » wrk -c 100 -t 4 http://localhost:8000 -d 10
Running 10s test @ http://localhost:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   122.78ms   52.24ms 434.83ms   83.29%
    Req/Sec   218.27     72.39   475.00     75.91%
  8278 requests in 10.03s, 1.64MB read
Requests/sec:    825.61
Transfer/sec:    167.70KB
"""
