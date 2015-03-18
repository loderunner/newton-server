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