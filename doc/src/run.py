from flask import Flask, request, Response, render_template, redirect
app = Flask(__name__)


@app.route('/')
def response():
    return "URL Detector"


@app.route('/api', methods=['POST', 'GET'])
def Submit():
    if request.method == 'GET':
        return render_template("run.html")
    else:
        return redirect(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    app.debug = True