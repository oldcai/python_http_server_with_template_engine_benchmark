import uvicorn
from jinja2 import Template
from starlette.applications import Starlette
from starlette.responses import Response

app = Starlette()
app.debug = False


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
    return Response(t)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

"""
~ » wrk -c 100 -t 4 http://localhost:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    16.58ms    5.28ms  67.13ms   57.63%
    Req/Sec     1.51k   129.66     1.85k    72.00%
  60771 requests in 10.09s, 10.61MB read
Requests/sec:   6020.40
Transfer/sec:      1.05MB
"""
