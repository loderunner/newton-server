from flask import Flask, request, make_response
from flask.json import dumps as json
from newton import solve

app = Flask(__name__)

@app.route("/newton", methods=['POST'])
def newton():
    try:
        s = solve(request.json['coeffs'], request.json['x0'])
        return json({'solution' : s})
    except RuntimeError as e:
        return make_response(unicode(e), 404)

if __name__ == "__main__":
    app.run()