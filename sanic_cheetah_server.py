from sanic import Sanic
from sanic.response import html
from Cheetah.Template import Template
templateDef = """
 <HTML>
 <HEAD><TITLE>$title</TITLE></HEAD>
 <BODY>
<?py echo(post_content) ?>
 ## this is a single-line Cheetah comment and won't appear in the output
 #* This is a multi-line comment and won't appear in the output
    blah, blah, blah
 *#
 </BODY>
 </HTML>"""


app = Sanic()


@app.route('/')
async def homepage(request):
    context = {
        'title': 'Blog Post Test',
        'post_content': "Foo\nBar\nBaz",
    }
    t = Template(templateDef, searchList=[context])
    return html(t)

app.run(port=8000)

"""
~ » wrk -c 100 -t 4 http://localhost:8000 -d 10
Running 10s test @ http://localhost:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    35.67ms   28.23ms 261.57ms   95.99%
    Req/Sec   788.82    177.17     1.13k    83.67%
  31083 requests in 10.01s, 6.64MB read
Requests/sec:   3104.93
Transfer/sec:    679.20KB
"""