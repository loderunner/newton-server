# newton-server
Simple Flask app server to solve polynomial equations using Newton's method

## Getting started

Install [pip](https://pip.pypa.io/en/latest/installing.html) and [virtualenv](http://virtualenv.readthedocs.org/en/latest/installation.html) if you haven't already. Then type:

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

## Troubleshooting

If you encounter problems while installing SciPy, you may be missing a few dependencies, like [BLAS](http://www.netlib.org/blas/) and [LAPACK](http://www.netlib.org/lapack/). This will most likely happen if you are running Debian or Ubuntu. Try to install the dependencies with apt-get:

```shell
apt-get install libblas-dev liblapack-dev gfortran
```

and run the `bootstrap.sh` script again.

## Licence

newton-server: Simple Flask app server to solve polynomial equations using Newton's method
Copyright (c) 2015 Charles Francoise

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
