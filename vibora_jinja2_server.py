from vibora import Vibora, Request, Response
from jinja2 import Template

app = Vibora()

template = Template("""
 <HTML>
 <HEAD><TITLE>{{ title }}</TITLE></HEAD>
 <BODY>
{{ post_content}}
 </BODY>
 </HTML>""")


@app.route('/')
async def homepage(request: Request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = template.render(context)
    return Response(t.encode('utf-8'), headers={'content-type': 'html'})

app.run(port=8000)

"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.40ms   14.99ms 215.15ms   98.20%
    Req/Sec     2.13k   329.37     3.13k    78.54%
  84344 requests in 10.04s, 14.96MB read
Requests/sec:   8398.26
Transfer/sec:      1.49MB
"""