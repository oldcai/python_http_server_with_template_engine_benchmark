from vibora import Vibora, Request
from vibora.templates import TemplateEngine, Template
from vibora.responses import Response

app = Vibora()
engine = TemplateEngine()

template = Template("""
 <HTML>
 <HEAD><TITLE>{{ title }}</TITLE></HEAD>
 <BODY>
{{ post_content}}
 </BODY>
 </HTML>""")

engine.add_template(template, ['benchmark'])
engine.compile_templates(verbose=False)


@app.route('/')
async def homepage(request: Request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = await engine.render('benchmark', **context)
    return Response(t.encode('utf-8'), headers={'content-type': 'html'})

app.run(port=8000)

"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    19.00ms   38.54ms 357.26ms   95.68%
    Req/Sec     2.14k   395.40     2.87k    85.79%
  83215 requests in 10.06s, 14.76MB read
Requests/sec:   8275.23
Transfer/sec:      1.47MB
"""