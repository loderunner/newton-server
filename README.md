# newton-server
Simple Flask app server to solve polynomial equations using newton's method

## Getting started

Install [pip](https://pip.pypa.io/en/latest/installing.html) and [virtualenv](http://virtualenv.readthedocs.org/en/latest/installation.html) if you haven't already.

```shell
./bootstrap.sh
```

You are now ready to run the `newton-server`

## Run the server

```shell
. env/bin/activate
python newton-server.py
```

## Solve a polynomial

The following request (performed with [httpie](https://github.com/jakubroztocil/httpie)) will request the solution for the equation: `-3x²+2x+1 = 0` with initial choice of x = 0.

```shell
http -v POST http://127.0.0.1:5000/newton "coeffs":='[1,2,-3]' "x0":='0'
```

Here is the HTTP exchange:

```
POST /newton HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate, compress
Content-Length: 31
Content-Type: application/json; charset=utf-8
Host: 127.0.0.1:5000
User-Agent: HTTPie/0.8.0

{
    "coeffs": [
        1, 
        2, 
        -3
    ], 
    "x0": 0
}
```

```
HTTP/1.0 200 OK
Content-Length: 34
Content-Type: text/html; charset=utf-8
Date: Wed, 18 Mar 2015 12:54:18 GMT
Server: Werkzeug/0.10.1 Python/2.7.6

{"solution": -0.33333333333333343}
```

If the server could not find a solution, a 404 status code is returned.

```shell
http -v POST http://127.0.0.1:5000/newton "coeffs":='[1,2,3]' "x0":='0'
```

```
POST /newton HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate, compress
Content-Length: 30
Content-Type: application/json; charset=utf-8
Host: 127.0.0.1:5000
User-Agent: HTTPie/0.8.0

{
    "coeffs": [
        1, 
        2, 
        3
    ], 
    "x0": 0
}
```

```
HTTP/1.0 404 NOT FOUND
Content-Length: 64
Content-Type: text/html; charset=utf-8
Date: Wed, 18 Mar 2015 12:58:31 GMT
Server: Werkzeug/0.10.1 Python/2.7.6

Failed to converge after 50 iterations, value is -0.319953277884
```
