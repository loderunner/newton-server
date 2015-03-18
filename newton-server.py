# newton-server: Simple Flask app server to solve polynomial equations using Newton's method
# Copyright (c) 2015 Charles Francoise
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, request, make_response
from flask.json import dumps as json
from newton import solve

app = Flask(__name__)

@app.route("/newton", methods=['POST'])
def newton():
    try:
        data = request.get_json(force=True)
        s = solve(data['coeffs'], data['x0'])
        res = make_response(json({'solution' : s}))
        res.headers['Content-Type'] = 'application/json; charset=utf-8'
        return res
    except RuntimeError as e:
        return make_response(unicode(e), 404)

if __name__ == "__main__":
    app.run()