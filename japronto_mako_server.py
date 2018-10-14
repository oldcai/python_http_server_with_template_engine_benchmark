from japronto import Application
from mako.template import Template

template = Template("""
 <HTML>
 <HEAD><TITLE>${ title }</TITLE></HEAD>
 <BODY>
${ post_content }
 </BODY>
 </HTML>""")


def hello(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = template.render(**context)
    return request.Response(text=t)


app = Application()
app.router.add_route('/', hello)
app.run(worker_num=1, port=8000)


"""
~ » wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.86ms   11.46ms 162.36ms   97.73%
    Req/Sec     4.52k   769.48     5.85k    78.00%
  180404 requests in 10.08s, 29.25MB read
Requests/sec:  17903.16
Transfer/sec:      2.90MB
"""