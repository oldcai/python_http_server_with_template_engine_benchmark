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
Running 10s test @ http://0.0.0.0:8000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    27.70ms    7.93ms  84.41ms   63.05%
    Req/Sec     0.90k   124.95     1.18k    69.70%
  36149 requests in 10.05s, 7.72MB read
Requests/sec:   3596.00
Transfer/sec:    786.63KB
"""