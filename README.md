# Python Fast Web Framework Benckmark

We know python can be extremely fast after the release of uvloop, but which is the best one to choose? Let's see.


I've made some benchmark test for the fast http engines combine with fast template engines.


## Benchmark Results

Tests were run on a 2.9 GHz Intel Core i5 CPU of a iMac, all HTTP engines use only 1 worker to process.

You can reproduce it if you feel like.

Python version: 3.6.6

Benchmark commend: `wrk -c 100 -t 4 http://0.0.0.0:8000 -d 10`


Note: Values in table are Requests/sec

|               | tenjin    | jinja2    | mako       | cheetah    | vibora
|:-------------:|:---------:|:---------:|:----------:|:----------:|:-------:|
| **japronto**  | 31273.63  | 28123.94  | 17903.16   | -          | 25645.10
| **vibora**    | 7727.74   | 8398.26   | -          | -          | 8275.23
| **starlette** | 5157.15
| **sanic**     | 4174.97   | 913.88    | -          | 3104.93    | 825.61
| **aiohttp**   | 3414.13
| **quart**     | 757.58


#### HTTP Engines

##### Fastest First Order

- [japronto](https://github.com/squeaky-pl/japronto)
- [vibora](https://github.com/vibora-io/vibora)
- [starlette](https://github.com/encode/starlette)
- [sanic](https://github.com/huge-success/sanic)
- [aiohttp](https://github.com/aio-libs/aiohttp)
- [quart](https://gitlab.com/pgjones/quart)

##### Most Stars First Order

- sanic
- japronto
- vibora
- aiohttp
- quart
- starlette


#### Template Engines

##### Fastest First Order

- tenjin ([homepage](http://www.kuwata-lab.com/tenjin/) or on [github](https://github.com/kwatch/tenjin/tree/python))
- [jinja2](https://github.com/pallets/jinja)
- [mako](https://github.com/zzzeek/mako)

##### Most Stars First Order

- jinja2
- mako
- tenjin

