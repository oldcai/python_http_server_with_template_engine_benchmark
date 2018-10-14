from japronto import Application
from vibora.templates import TemplateEngine, Template


engine = TemplateEngine()
template = Template("""
 <HTML>
 <HEAD><TITLE>{{ title }}</TITLE></HEAD>
 <BODY>
{{ post_content }}
 </BODY>
 </HTML>""")

engine.add_template(template, ['benchmark'])
engine.compile_templates(verbose=False)


async def hello(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = await engine.render('benchmark', **context)
    return request.Response(text=t)


app = Application()
app.router.add_route('/', hello)
app.run(worker_num=1, port=8000)

"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.80ms    9.38ms 145.05ms   98.59%
    Req/Sec     6.45k     0.95k    7.97k    80.75%
  257036 requests in 10.02s, 41.67MB read
Requests/sec:  25645.10
Transfer/sec:      4.16MB
"""
